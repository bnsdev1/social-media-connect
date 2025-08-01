"""LangGraph pipeline connecting modules."""

from typing import TypedDict, List, Dict
from langgraph.graph import StateGraph, START, END

from .trend_analysis import get_trending_topics
from .content_generation import generate_content
from .publisher import publish_to_platforms
from .config import APIConfig


class AgentState(TypedDict):
    domain: str
    topic: str
    length: str
    provider: str
    platforms: List[str]
    topics: List[str]
    content: str
    results: List[Dict]


def trend_node(state: AgentState) -> AgentState:
    state["topics"] = get_trending_topics(state["domain"])
    return state

def content_node(state: AgentState) -> AgentState:
    config = APIConfig()
    state["content"] = generate_content(state["topic"], state["length"], state["provider"], config)
    return state

def publish_node(state: AgentState) -> AgentState:
    config = APIConfig()
    state["results"] = publish_to_platforms(state["content"], state["platforms"], config)
    return state

def build_agent() -> StateGraph:
    graph = StateGraph(AgentState)
    graph.add_node("trend", trend_node)
    graph.add_node("content", content_node)
    graph.add_node("publish", publish_node)
    graph.add_edge(START, "trend")
    graph.add_edge("trend", "content")
    graph.add_edge("content", "publish")
    graph.add_edge("publish", END)
    return graph.compile()
