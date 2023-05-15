"""Translate Microservice

This microservice allows get the translation from a text
"""

from fastapi import FastAPI
from pydantic import BaseModel
from translator import Translator

app = FastAPI()

print('\n\n')
print('='*100)
print('Starting Translator Service.....')
translator = Translator()
print('Translator Service Started')
print('='*100)
print('\n\n')


class Data(BaseModel):
    """
    Data model
    ---
    parameters:
      - input_text: translation input
        type: string
      - target_lang: target language
        type: string
    """
    input_text: str
    target_lang: str


@app.post('/translate/')
async def translate(data: Data):
    """
    Endpoint for Translation of input text to other language.
    ---
    parameters:
      - input_text: translation input
        type: string

      - target_lang: target language
        type: string
    responses:
      200:
        description: Translated text
    """
    out_txt = translator.translate(data.input_text, data.target_lang)

    return {"response": out_txt}


if __name__ == '__main__':
    app.run(debug=True)  # type: ignore
