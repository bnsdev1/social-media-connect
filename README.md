# Social Media Connect

This project demonstrates a modular agent for discovering trending topics, generating content using various LLM providers, and publishing to social media platforms.

## Features
- Fetch trending topics for domains like AI and Cloud.
- Configure API keys for OpenAI, Gemini, Claude, Instagram, LinkedIn, and Substack.
- Generate brief or detailed posts via chosen LLM.
- Publish to multiple platforms and view history in a simple dashboard.
- Streamlit web UI for end-to-end workflow.
- LangGraph agent wiring modules together.

## Process Flow
1. **Discover Trends** – the agent queries for trending topics within domains such as AI or Cloud.
2. **Select Topic** – users choose a topic in the Streamlit UI.
3. **Generate Content** – the selected topic is sent to an LLM provider to craft a brief or detailed post.
4. **Choose Platforms** – users select social media destinations (e.g., Instagram, LinkedIn).
5. **Publish** – the publisher module posts the generated content to the chosen platforms and logs the activity.
6. **Review History** – publishing history is displayed in the dashboard for transparency.

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

## Running with Docker
1. Build the container image:
   ```bash
   docker build -t social-media-connect .
   ```
2. Run the container, providing your environment variables:
   ```bash
   docker run --env-file .env -p 8501:8501 social-media-connect
   ```
   The UI will be available at http://localhost:8501.

An architecture diagram illustrating the main components is available in [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Extending
- Replace stub functions in `trend_analysis.py`, `content_generation.py`, and `publisher.py` with real API calls.
- Add analytics or database-backed dashboard.
- Extend to additional platforms or LLM providers.

## Tests
Each module includes basic tests found under `tests/`.

## UI Mockup
The Streamlit UI contains sections to configure API keys, select topics, generate content, choose platforms, and review publishing history.
