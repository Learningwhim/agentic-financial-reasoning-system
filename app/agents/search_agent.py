from app.tools.tavily_tool import tavily

def search(state):

    all_results = []

    for topic in state["search_topics"]:

        results = tavily.search(
            query=topic,
            max_results=3
        )

        all_results.extend(results["results"])

    return {
        "search_data": all_results
    }