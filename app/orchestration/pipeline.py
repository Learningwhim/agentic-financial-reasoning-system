from langgraph.graph import StateGraph, START, END

from app.schemas.state import GraphState
from app.agents.planner import planner
from app.agents.search_agent import search
from app.agents.bear import bear
from app.agents.bull import bull
from app.agents.critic import critic

graph = StateGraph(GraphState)

graph.add_node("planner", planner)
graph.add_node("search", search)
graph.add_node("bull", bull)
graph.add_node("bear", bear)
graph.add_node("critic", critic)

graph.add_edge(START, "planner")
graph.add_edge("planner", "search")

# parallel edges
graph.add_edge("search", "bull")
graph.add_edge("search", "bear")

graph.add_edge("bull", "critic")
graph.add_edge("bear", "critic")

graph.add_edge("critic", END)

app = graph.compile()
