from app.prompts.bull_prompt import BULL_PROMPT
from app.utils.llm import llm
from app.schemas.output import BullOutput

structured_llm = llm.with_structured_output(BullOutput)

def bull(state):

    prompt = BULL_PROMPT.format(
        query=state["query"],
        search_data=state["search_data"]
    )

    response = structured_llm.invoke(prompt)

    return {
        "bull_case": response.model_dump()
    }