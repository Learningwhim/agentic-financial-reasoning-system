from app.utils.llm import llm
from app.schemas.output import BearOutput
from app.prompts.bear_prompt import BEAR_PROMPT

structured_llm = llm.with_structured_output(BearOutput)


def bear(state):

    prompt = BEAR_PROMPT.format(
        query=state["query"],
        search_data=state["search_data"]
    )
    response = structured_llm.invoke(prompt)

    return {
        "bear_case": response.model_dump()
    }