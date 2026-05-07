from pydantic import BaseModel

class BullOutput(BaseModel):
    score: int
    confidence: float
    reasoning: str

class BearOutput(BaseModel):
    score: int
    confidence: float
    reasoning: str

class CriticOutput(BaseModel):
    recommendation: str
    confidence: float
    risk_level: str
    final_reasoning: str

class PlannerOutput(BaseModel):
    search_topics: list[str]