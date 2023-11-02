from dotenv import load_dotenv
from opensearchpy import OpenSearch, RequestsHttpConnection
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import os


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


if __name__ == "__main__":

    load_dotenv()

    host = "search-server-search-sn3tyevnqczq4x7z7prx7aeq2m.eu-west-3.es.amazonaws.com"
    auth = (os.getenv('OPENSEARCH_USER'), os.getenv('OPENSEARCH_PASS'))

    # Create the client with SSL/TLS and hostname verification disabled.
    client = OpenSearch(
        hosts=[{'host': host, 'port': 443}],
        http_auth=auth,
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection
    )

    # Input text

    texto = 'Voy a realizar un estudio sobre el impacto del Covid19 sobre el turismo'

    # Generate
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

    model = ChatOpenAI(model="gpt-4", temperature=0)

    llm_chain = LLMChain(
        llm=model,
        prompt=prompt,
        #memory=memory
    )

    output_selector = llm_chain.run(input)
    parsed = output_parser.parse(output_selector)

    # Start experiment
    list_keywords = parsed['Variables']

    urls_list = []
    urls_check = []
    for keyword in list_keywords:
        output = search_keywords(client, keyword)
        if len(output) != 0 and output['url'] not in urls_check:
            urls_list.append(output)
            urls_check.append(output['url'])

    response = {"text": parsed['respuesta'], "variables": urls_list}

    print(response)
