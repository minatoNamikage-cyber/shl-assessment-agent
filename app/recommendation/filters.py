from typing import List

from app.models.catalog import CatalogItem


class FilterService:

    def filter_by_language(
        self,
        assessments: List[CatalogItem],
        language: str,
    ) -> List[CatalogItem]:

        return [
            assessment
            for assessment in assessments
            if language.lower()
            in " ".join(assessment.languages).lower()
        ]

    def filter_by_remote(
        self,
        assessments: List[CatalogItem],
        remote_required: bool,
    ) -> List[CatalogItem]:

        if not remote_required:
            return assessments

        return [
            assessment
            for assessment in assessments
            if assessment.remote.lower() == "yes"
        ]

    def filter_by_adaptive(
        self,
        assessments: List[CatalogItem],
        adaptive_required: bool,
    ) -> List[CatalogItem]:

        if not adaptive_required:
            return assessments

        return [
            assessment
            for assessment in assessments
            if assessment.adaptive.lower() == "yes"
        ]