from trend_agent.publisher import publish_to_platforms
from trend_agent.config import APIConfig

def test_publish_to_platforms_missing_keys():
    config = APIConfig()
    results = publish_to_platforms("hello", ["instagram"], config)
    assert results[0]["status"] == "error"
