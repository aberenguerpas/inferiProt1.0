from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from opensearchpy import OpenSearch, RequestsHttpConnection
from dotenv import load_dotenv
from fastapi import FastAPI, Request
import json
import os


load_dotenv()
app = FastAPI()

# Create database client

host = "search-server-search-sn3tyevnqczq4x7z7prx7aeq2m.eu-west-3.es.amazonaws.com"
auth = (os.getenv('OPENSEARCH_USER'), os.getenv('OPENSEARCH_PASS'))
client = OpenSearch(
    hosts=[{'host': host, 'port': 443}],
    http_auth=auth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)

# Define models
llm_reason = ChatOpenAI(model="gpt-4", temperature=0.0)
llm_clas = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.0)
# Load prompts
f = open('prompts.json')
prompts = json.load(f)

# Define memory
memory = ConversationBufferMemory(memory_key="chat_history")


def search_keywords(client, keyword):
    query = {
        "query": {
            "bool": {
                "must": [{
                        "match": {
                            "title_es": {
                                "query": keyword,
                            }
                        }
                }]
            }
        }
    }
    resp = client.search(index="search-v1", size=1, body=query)
    data = {}
    for hit in resp['hits']['hits']:
        if hit['_score'] < 10:
            data['title'] = hit['_source']['title_es']
            data['url'] = 'http://inferia.io/details/'+hit['_id']

            #result.append(data)

    return data


def clas_topic(input, llm):

    response_schemas = [
        ResponseSchema(name="topic", description="Asigna un número a la temática al texto, teniendo en cuenta las respuestas anteriores, pudiendo ser 1 o 2 "),
    ]
    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
    format_instructions = output_parser.get_format_instructions()
    prompt = PromptTemplate(
        template=prompts[3]['prompt_template'],
        input_variables=["input"],
        partial_variables={"format_instructions": format_instructions}
    )

    llm_chain = LLMChain(
        llm=llm,
        prompt=prompt
    )

    output_selector = llm_chain.run(input)

    parsed = output_parser.parse(output_selector)

    return parsed['topic']


def generate_response(text, model):
    response_schemas = [
        ResponseSchema(name="respuesta", description="Respuesta al usuario con todo detalle"),
        ResponseSchema(name="Variables", description="Array de variables en el formato ['Var1','Var2','Var3'] y sin emoticonos")
    ]
    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

    format_instructions = output_parser.get_format_instructions()

    prompt = PromptTemplate(
        template="Eres un experto en ciencia de datos y analítica de datos e inteligencia artificial.Ofrece una lista de variables interesantes que puedan ser de utilidad para el objetivo definido.\nLa lista debe contener 10 elementos, usar emoticonos, un lenguage sencillo y directo y además, debe estar formateada en una lista HTML cómo en el siguiente ejemplo <ul><li><strong>📅Día:</strong> Es una variable interesantes porque influye en...</li><li><strong>🌍Pais:</strong> Dependiendo del pais se puede saber...</li></ul>\n.\n. Por otro lado, ofrece al usuario una tabla HTML con ejemplos del datos y usando únicamente 2 columnas \n{format_instructions} \nObjetivo: {input}\nRespuesta:",
        input_variables=["input"],
        partial_variables={"format_instructions": format_instructions}
    )
    llm_chain = LLMChain(
        llm=model,
        prompt=prompt,
        #memory=memory
    )

    output_selector = llm_chain.run(text)
    parsed = output_parser.parse(output_selector)

    return parsed

@app.post("/fallback/")
async def chatbot(data: Request):
    try:
        message = await data.json()
        print(message)
        res = clas_topic(message['data'], llm_clas)

        if int(res) == 2:
            return {'msj': {'text':'Lo siento😅 No te puedo ayudar a resolver ese tipo de preguntas. ¿Te puedo ayudar en algo más?'}}
        else:
            output_gen = generate_response(message['data'], llm_reason)
            #print(output)
            list_keywords = output_gen['Variables']

            urls_list = []
            urls_check = []
            for keyword in list_keywords:
                output = search_keywords(client, keyword)
                if len(output) != 0 and output['url'] not in urls_check:
                    urls_list.append(output)
                    urls_check.append(output['url'])

            response = {"text": output_gen['respuesta'], "variables": urls_list}
            print(response)
            return {'msj': response}

    except Exception as e:
        print(e)
        return {'msj': 'Ups... estoy teniendo problemas para pensar, mejor pregúntame un poco más tarde.'}
