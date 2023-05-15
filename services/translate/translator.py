from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


class Translator:

    def __init__(self):

        self.model_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-es-en")
        self.tokenizer_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-es-en")

        self.model_es = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-es")
        self.tokenizer_es = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-es")

        self.supported_langs = ['es', 'en']

    def translate(self, input_text, tgt_lang):

        split_text = input_text.split(".")
        translation = ""

        if tgt_lang not in self.supported_langs:
            return 'unsupported language: ' + tgt_lang

        if tgt_lang == 'en':
            for text in split_text:
                print(text)
                encoded_text = self.tokenizer_en(text, return_tensors='pt').input_ids
                generated_tokens = self.model_en.generate(encoded_text, max_new_tokens = 512)
                output_text_arr = self.tokenizer_en.batch_decode(generated_tokens,
                                                                truncate=True,
                                                                skip_special_tokens=True)
                translation += output_text_arr[0]+". "

        else:
            for text in split_text:
                encoded_text = self.tokenizer_es(input_text, return_tensors='pt').input_ids
                generated_tokens = self.model_es.generate(encoded_text, max_new_tokens = 512)
                output_text_arr = self.tokenizer_es.batch_decode(generated_tokens,
                                                                truncate=True,
                                                                skip_special_tokens=True)
                translation += output_text_arr[0]+". "

        if len(translation) > 0:
            return translation
        else:
            return 'Failed to generate output. Output Text Array is empty.'
