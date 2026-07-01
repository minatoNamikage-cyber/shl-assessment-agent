import json
import numpy as np

from app.embeddings.embedder import embedding_service


CATALOG_PATH = "app/data/catalog.json"

OUTPUT_PATH = "app/data/embeddings.npy"


def build_embeddings():

    print("Loading catalog...")

    with open(
        CATALOG_PATH,
        encoding="utf-8"
    ) as f:

        catalog = json.load(f)

    documents = []

    for item in catalog:

        text = " ".join(

            [

                item.get("name", ""),

                item.get("description", ""),

                " ".join(
                    item.get("keys", [])
                ),

                " ".join(
                    item.get("job_levels", [])
                ),

                " ".join(
                    item.get("languages", [])
                )

            ]

        )

        documents.append(text)

    print(f"Embedding {len(documents)} assessments...")

    embeddings = embedding_service.encode(
        documents
    )

    np.save(
        OUTPUT_PATH,
        embeddings
    )

    print("Embeddings Saved")

    print(embeddings.shape)


if __name__ == "__main__":

    build_embeddings()