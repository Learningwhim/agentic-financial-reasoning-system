from app.prompts.critic_prompt import CRITIC_PROMPT
from app.utils.llm import llm
from app.schemas.output import CriticOutput


def critic(state):

    bull = state["bull_case"]
    bear = state["bear_case"]

    prompt = CRITIC_PROMPT.format(
        bull_score=bull["score"],
        bull_confidence=bull["confidence"],
        bull_reasoning=bull["reasoning"],

        bear_score=bear["score"],
        bear_confidence=bear["confidence"],
        bear_reasoning=bear["reasoning"]
    )

    structured_llm = llm.with_structured_output(CriticOutput)

    response = structured_llm.invoke(prompt)

    return {
        "critique": response.model_dump(),
        "final_decision": response.recommendation
    }
