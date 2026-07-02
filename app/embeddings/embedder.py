import requests
import numpy as np
from app.core.config import settings


class EmbeddingService:

    def __init__(self):
        self.url = (
            "https://router.huggingface.co/"
            "hf-inference/models/BAAI/bge-small-en-v1.5"
        )

        self.headers = {
            "Authorization": f"Bearer {settings.HF_TOKEN}"
        }

    def encode(self, texts):

        if isinstance(texts, str):
            texts = [texts]

        embeddings = []

        for text in texts:

            response = requests.post(
                self.url,
                headers=self.headers,
                json={
                    "inputs": text
                },
                timeout=60
            )

            response.raise_for_status()

            vector = response.json()

            embeddings.append(vector)

        return np.array(
            embeddings,
            dtype=np.float32
        )


embedding_service = EmbeddingService()
