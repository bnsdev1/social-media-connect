"""Social platform publishing utilities."""

from typing import Dict, List
from .config import APIConfig

# Placeholder implementations. Replace with real API calls.

def publish_to_instagram(content: str, config: APIConfig) -> Dict:
    if not config.instagram_token:
        return {"status": "error", "detail": "Missing Instagram token"}
    return {"status": "success", "platform": "instagram", "content": content}

def publish_to_linkedin(content: str, config: APIConfig) -> Dict:
    if not config.linkedin_token:
        return {"status": "error", "detail": "Missing LinkedIn token"}
    return {"status": "success", "platform": "linkedin", "content": content}

def publish_to_substack(content: str, config: APIConfig) -> Dict:
    if not config.substack_token:
        return {"status": "error", "detail": "Missing Substack token"}
    return {"status": "success", "platform": "substack", "content": content}

def publish_to_platforms(content: str, platforms: List[str], config: APIConfig) -> List[Dict]:
    """Publish content to selected platforms."""
    responses = []
    for platform in platforms:
        if platform == "instagram":
            responses.append(publish_to_instagram(content, config))
        elif platform == "linkedin":
            responses.append(publish_to_linkedin(content, config))
        elif platform == "substack":
            responses.append(publish_to_substack(content, config))
    return responses
