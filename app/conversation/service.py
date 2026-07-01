from typing import Dict, Any

from app.llm.llm import llm_service
from app.retrieval.semantic_search import semantic_search


class ConversationService:
    """
    Main Conversation Orchestrator

    Flow:
    User Query
        ↓
    LLM Analysis
        ↓
    Build Search Query
        ↓
    Semantic Search
        ↓
    Generate Final Response
    """

    def process(self, query: str) -> Dict[str, Any]:

        # ----------------------------------
        # Step 1 : Analyze User Query
        # ----------------------------------

        analysis = llm_service.analyze(query)

        # ----------------------------------
        # Step 2 : Build Search Query
        # ----------------------------------

        search_parts = []

        if analysis.get("role"):
            search_parts.append(analysis["role"])

        if analysis.get("job_level"):
            search_parts.append(analysis["job_level"])

        if analysis.get("purpose"):
            search_parts.append(analysis["purpose"])

        if analysis.get("assessment_type"):
            search_parts.append(analysis["assessment_type"])

        if analysis.get("experience"):
            search_parts.append(analysis["experience"])

        search_query = " ".join(search_parts).strip()

        if not search_query:
            search_query = query

        # ----------------------------------
        # Step 3 : Semantic Search
        # ----------------------------------

        recommendations = semantic_search.search(
            search_query,
            top_k=10
        )

        # ----------------------------------
        # Step 4 : Natural Language Response
        # ----------------------------------

        response = llm_service.generate_response(
            query=query,
            recommendations=recommendations
        )

        # ----------------------------------
        # Step 5 : Return
        # ----------------------------------

        return {
            "query": query,
            "analysis": analysis,
            "search_query": search_query,
            "recommendations": recommendations,
            "response": response
        }


conversation_service = ConversationService()