from trend_agent.content_generation import generate_content
from trend_agent.config import APIConfig

def test_generate_content_openai():
    config = APIConfig(openai_api_key="test")
    text = generate_content("Test Topic", "brief", "openai", config)
    assert "OpenAI" in text
