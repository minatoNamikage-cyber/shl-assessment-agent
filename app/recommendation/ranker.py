from typing import List

from app.models.catalog import CatalogItem


class Ranker:

    def rank(
        self,
        query: str,
        assessments: List[CatalogItem],
    ) -> List[CatalogItem]:

        query = query.lower()

        scored = []

        for assessment in assessments:

            score = 0

            if query in assessment.name.lower():
                score += 10

            if assessment.description:

                if query in assessment.description.lower():
                    score += 5

            for key in assessment.keys:

                if query in key.lower():
                    score += 8

            for level in assessment.job_levels:

                if query in level.lower():
                    score += 4

            scored.append((score, assessment))

        scored.sort(
            key=lambda x: x[0],
            reverse=True,
        )

        return [assessment for score, assessment in scored]