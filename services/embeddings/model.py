from sentence_transformers import SentenceTransformer


class SentenceTransformerMulti:

    def __init__(self):
        self.model = SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')
        self.dimensions = 768

    def getEmbedding(self, data):
        return self.model.encode(data)
