from typing import TypedDict

class GraphState(TypedDict):
    query: str

    plan: str
    search_topics: list[str]
    search_data: str
    structured_knowledge: str

    bull_case: dict
    bear_case: dict

    critique: dict
    final_decision: str