from typing import List

from app.models.catalog import CatalogItem
from app.models.recommendation import Recommendation


class RecommendationBuilder:

    def build(
        self,
        assessments: List[CatalogItem],
    ) -> List[Recommendation]:

        recommendations = []

        for assessment in assessments[:10]:

            recommendation = Recommendation(

                name=assessment.name,

                url=assessment.link,

                reason="Recommended based on catalog relevance.",

                test_type=", ".join(assessment.keys),

                duration=assessment.duration,

                languages=assessment.languages,
            )

            recommendations.append(recommendation)

        return recommendations