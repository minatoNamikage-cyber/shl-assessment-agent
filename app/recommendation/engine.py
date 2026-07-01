from typing import List

from app.models.recommendation import Recommendation

from app.recommendation.search import SearchService
from app.recommendation.filters import FilterService
from app.recommendation.ranker import Ranker
from app.recommendation.builder import RecommendationBuilder


class RecommendationEngine:

    def __init__(self):

        self.search_service = SearchService()

        self.filter_service = FilterService()

        self.ranker = Ranker()

        self.builder = RecommendationBuilder()

    def recommend(
        self,
        query: str,
    ) -> List[Recommendation]:

        assessments = self.search_service.search(query)

        ranked = self.ranker.rank(
            query=query,
            assessments=assessments,
        )

        recommendations = self.builder.build(ranked)

        return recommendations


recommendation_engine = RecommendationEngine()