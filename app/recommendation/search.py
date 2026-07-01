from typing import List

from app.models.catalog import CatalogItem
from app.services.catalog_service import catalog_service


class SearchService:
    """
    Responsible only for searching the SHL catalog.
    No ranking.
    No filtering.
    """

    def search(self, query: str) -> List[CatalogItem]:

        query = query.lower().strip()

        results = []

        for assessment in catalog_service.get_all():

            searchable_text = " ".join(
                [
                    assessment.name,
                    assessment.description or "",
                    " ".join(assessment.keys),
                    " ".join(assessment.job_levels),
                    " ".join(assessment.languages),
                ]
            ).lower()

            if query in searchable_text:
                results.append(assessment)

        return results