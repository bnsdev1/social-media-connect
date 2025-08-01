from trend_agent.trend_analysis import get_trending_topics

def test_get_trending_topics():
    topics = get_trending_topics("ai")
    assert isinstance(topics, list)
    assert "Generative AI" in topics
