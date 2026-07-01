from typing import List, Dict
import json

import numpy as np

from app.embeddings.embedder import embedding_service
from app.retrieval.faiss_index import faiss_index


class SemanticSearch:

    """
    Production Semantic Search Engine
    """

    def __init__(self):

        print("Loading FAISS Index...")

        self.index, self.metadata = faiss_index.load()

        with open(
            "app/data/catalog.json",
            encoding="utf-8"
        ) as f:

            self.catalog = json.load(f)

        self.catalog_lookup = {
            item["entity_id"]: item
            for item in self.catalog
        }

        print("Semantic Search Ready")

    # =============================================
    # Search
    # =============================================

    def search(
        self,
        query: str,
        top_k: int = 10
    ) -> List[Dict]:

        query_embedding = embedding_service.encode(
            query
        )

        query_embedding = query_embedding.astype(
            "float32"
        )

        scores, indices = self.index.search(
            query_embedding,
            top_k
        )

        results = []

        for score, idx in zip(
            scores[0],
            indices[0]
        ):

            if idx == -1:
                continue

            item = self.metadata[idx]

            catalog_item = self.catalog_lookup.get(
                item["entity_id"]
            )

            if catalog_item:

                catalog_item = catalog_item.copy()

                catalog_item["score"] = float(score)

                results.append(catalog_item)

        return results


semantic_search = SemanticSearch()