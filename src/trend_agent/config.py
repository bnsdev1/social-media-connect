"""Configuration utilities.

Loads API keys from environment variables or a .env file.
"""

from dataclasses import dataclass
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file if present

@dataclass
class APIConfig:
    openai_api_key: Optional[str] = os.getenv("OPENAI_API_KEY")
    gemini_api_key: Optional[str] = os.getenv("GEMINI_API_KEY")
    claude_api_key: Optional[str] = os.getenv("CLAUDE_API_KEY")
    instagram_token: Optional[str] = os.getenv("INSTAGRAM_TOKEN")
    linkedin_token: Optional[str] = os.getenv("LINKEDIN_TOKEN")
    substack_token: Optional[str] = os.getenv("SUBSTACK_TOKEN")
