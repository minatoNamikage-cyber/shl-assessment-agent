import json
import logging
from typing import Dict, Any

from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

from app.core.config import settings

load_dotenv()

logger = logging.getLogger(__name__)


class LLMService:
    """
    Production LLM Service

    Responsibilities
    ----------------
    1. Analyze conversation
    2. Generate final response
    3. Compare assessments
    """

    def __init__(self):

        self.llm = ChatMistralAI(
            model=settings.MODEL_NAME,
            api_key=settings.MISTRAL_API_KEY,
            temperature=0,
            max_retries=2,
        )

    # =====================================================
    # Analyze User Query
    # =====================================================

    def analyze(self, query: str) -> Dict[str, Any]:

        system_prompt = """
You are an SHL Assessment Recommendation AI.

Your task is ONLY to extract structured information from the user's request.

Do NOT answer the user.

Do NOT recommend assessments.

Return ONLY valid JSON.

Use EXACTLY this schema:

{{
    "intent": "",
    "role": "",
    "job_level": "",
    "experience": "",
    "purpose": "",
    "assessment_type": "",
    "clarification_needed": false
}}

Rules:

Intent MUST be one of:
- recommend
- compare
- refine
- clarify
- finalize

Purpose MUST be one of:
- Hiring
- Selection
- Development

Assessment_type MUST be one of:
- Technical
- Personality
- Cognitive
- Behavioural
- Situational Judgement
- Mixed

Job_level examples:
- Graduate
- Entry
- Junior
- Mid
- Senior
- Manager
- Director
- Executive
- CXO

Examples:

User:
We are hiring Senior Java Developers with 5 years experience.

Output:

{{
    "intent":"recommend",
    "role":"Java Developer",
    "job_level":"Senior",
    "experience":"5 years",
    "purpose":"Hiring",
    "assessment_type":"Technical",
    "clarification_needed":false
}}

User:
Need assessments for graduate management trainees.

Output:

{{
    "intent":"recommend",
    "role":"Graduate Management Trainee",
    "job_level":"Graduate",
    "experience":"",
    "purpose":"Hiring",
    "assessment_type":"Mixed",
    "clarification_needed":false
}}

If any important information is missing,
set clarification_needed=true.

Return ONLY JSON.
"""

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("human", "{query}")
            ]
        )

        chain = prompt | self.llm

        try:

            response = chain.invoke(
                {
                    "query": query
                }
            )

            content = response.content.strip()

            if content.startswith("```"):
                content = (
                    content.replace("```json", "")
                    .replace("```", "")
                    .strip()
                )

            return json.loads(content)

        except Exception as e:

            logger.exception(e)

            return {
                "intent": "unknown",
                "role": "",
                "experience": "",
                "purpose": "",
                "assessment_type": "",
                "clarification_needed": True
            }

    # =====================================================
    # Generate Natural Response
    # =====================================================

    def generate_response(
        self,
        query: str,
        recommendations: list
    ) -> str:

        system_prompt = """
You are an SHL Assessment Recommendation Assistant.

Use ONLY the supplied recommendations.

Do NOT invent assessments.

Keep response under 150 words.
"""

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                (
                    "human",
                    """
User Query:

{query}

Recommendations:

{recommendations}
"""
                )
            ]
        )

        chain = prompt | self.llm

        try:

            response = chain.invoke(
                {
                    "query": query,
                    "recommendations": json.dumps(
                        recommendations,
                        indent=2
                    )
                }
            )

            return response.content

        except Exception as e:

            logger.exception(e)

            return "Unable to generate response."

    # =====================================================
    # Compare Assessments
    # =====================================================

    def compare(
        self,
        assessment1: dict,
        assessment2: dict
    ) -> str:

        system_prompt = """
Compare the following two SHL assessments.

Mention:

- Purpose
- Duration
- Skills
- Best Use Case

Keep comparison concise.
"""

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                (
                    "human",
                    """
Assessment 1

{a1}

Assessment 2

{a2}
"""
                )
            ]
        )

        chain = prompt | self.llm

        try:

            response = chain.invoke(
                {
                    "a1": json.dumps(
                        assessment1,
                        indent=2
                    ),
                    "a2": json.dumps(
                        assessment2,
                        indent=2
                    )
                }
            )

            return response.content

        except Exception as e:

            logger.exception(e)

            return "Unable to compare assessments."


llm_service = LLMService()