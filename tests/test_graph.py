from trend_agent.graph import build_agent


def test_build_agent_runs():
    graph = build_agent()
    initial_state = {
        "domain": "ai",
        "topic": "Generative AI",
        "length": "brief",
        "provider": "openai",
        "platforms": [],
        "topics": [],
        "content": "",
        "results": [],
    }
    final_state = graph.invoke(initial_state)
    assert "topics" in final_state
    assert "content" in final_state
