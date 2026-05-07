from app.utils.llm import llm
from app.schemas.output import PlannerOutput
from app.prompts.planner_prompt import PLANNER_PROMPT

structured_llm = llm.with_structured_output(PlannerOutput)

def planner(state):

    prompt = PLANNER_PROMPT.format(
        query=state["query"]
    )

    response = structured_llm.invoke(prompt)

    return {
        "search_topics": response.search_topics
    }