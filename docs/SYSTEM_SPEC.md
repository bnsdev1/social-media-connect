# System Specification

## Domain
Trending topics analysis and social publishing for verticals like AI and cloud.

## Core Functions
- **Trending Topic Analysis:** Aggregate trending topics using sources like Google Trends, Twitter/X, Reddit, and news APIs.
- **User Interface:** Allow users to configure API keys for LLM providers (OpenAI, Gemini, Claude) and social platforms.
- **Content Generation:** Generate brief or detailed posts using the selected LLM provider.
- **Publishing:** Schedule and publish posts to Instagram, LinkedIn, and Substack via their APIs.
- **Dashboard:** Review and manage published posts and scheduling status.

## Non‑Functional Requirements
- Modular architecture built with LangGraph nodes.
- Configurable via environment variables or UI inputs.
- Error handling and logging across modules.
- Simple Streamlit UI for local use.
- Test coverage for each module.
