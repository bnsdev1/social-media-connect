# Social Media Connect

This project demonstrates a modular agent for discovering trending topics, generating content using various LLM providers, and publishing to social media platforms.

## Features
- Fetch trending topics for domains like AI and Cloud.
- Configure API keys for OpenAI, Gemini, Claude, Instagram, LinkedIn, and Substack.
- Generate brief or detailed posts via chosen LLM.
- Publish to multiple platforms and view history in a simple dashboard.
- Streamlit web UI for end-to-end workflow.
- LangGraph agent wiring modules together.

## Setup
1. Create and populate a `.env` file based on `.env.example` with your API keys.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run tests:
   ```bash
   pytest
   ```
4. Launch the UI:
   ```bash
   streamlit run ui/app.py
   ```

## Extending
- Replace stub functions in `trend_analysis.py`, `content_generation.py`, and `publisher.py` with real API calls.
- Add analytics or database-backed dashboard.
- Extend to additional platforms or LLM providers.

## Tests
Each module includes basic tests found under `tests/`.

## UI Mockup
The Streamlit UI contains sections to configure API keys, select topics, generate content, choose platforms, and review publishing history.
