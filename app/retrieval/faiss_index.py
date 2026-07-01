import os
import json
import pickle
import faiss
import numpy as np


class FAISSIndex:

    def __init__(self):

        self.catalog_path = "app/data/catalog.json"

        self.embedding_path = "app/data/embeddings.npy"

        self.index_path = "app/data/faiss.index"

        self.metadata_path = "app/data/metadata.pkl"

    # ===================================================
    # Build FAISS Index
    # ===================================================

    def build(self):

        print("Loading embeddings...")

        embeddings = np.load(self.embedding_path)

        embeddings = embeddings.astype("float32")

        dimension = embeddings.shape[1]

        print(f"Embedding Shape : {embeddings.shape}")

        index = faiss.IndexFlatIP(dimension)

        index.add(embeddings)

        faiss.write_index(
            index,
            self.index_path
        )

        print("FAISS index saved.")

        with open(
            self.catalog_path,
            "r",
            encoding="utf-8"
        ) as f:

            catalog = json.load(f)

        metadata = []

        for item in catalog:

            metadata.append(
                {
                    "entity_id": item["entity_id"],
                    "name": item["name"],
                    "url": item["link"]
                }
            )

        with open(
            self.metadata_path,
            "wb"
        ) as f:

            pickle.dump(
                metadata,
                f
            )

        print("Metadata Saved")

        print(f"Indexed {len(metadata)} assessments")

    # ===================================================
    # Load Index
    # ===================================================

    def load(self):

        index = faiss.read_index(
            self.index_path
        )

        with open(
            self.metadata_path,
            "rb"
        ) as f:

            metadata = pickle.load(f)

        return index, metadata


faiss_index = FAISSIndex()


if __name__ == "__main__":

    faiss_index.build()