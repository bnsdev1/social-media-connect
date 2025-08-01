import streamlit as st
from trend_agent.trend_analysis import get_trending_topics
from trend_agent.content_generation import generate_content
from trend_agent.publisher import publish_to_platforms
from trend_agent.dashboard import log_post, get_history
from trend_agent.config import APIConfig

st.set_page_config(page_title="Trend Publisher", layout="wide")

st.sidebar.header("API Configuration")
openai_key = st.sidebar.text_input("OpenAI API Key", type="password")
gemini_key = st.sidebar.text_input("Gemini API Key", type="password")
claude_key = st.sidebar.text_input("Claude API Key", type="password")
instagram_token = st.sidebar.text_input("Instagram Token", type="password")
linkedin_token = st.sidebar.text_input("LinkedIn Token", type="password")
substack_token = st.sidebar.text_input("Substack Token", type="password")

config = APIConfig(
    openai_api_key=openai_key or None,
    gemini_api_key=gemini_key or None,
    claude_api_key=claude_key or None,
    instagram_token=instagram_token or None,
    linkedin_token=linkedin_token or None,
    substack_token=substack_token or None,
)

st.title("Trending Topic Publisher")

# Step 1: Select domain
Domain = st.selectbox("Select domain", ["AI", "Cloud"])

# Step 2: Show trending topics
if Domain:
    topics = get_trending_topics(Domain)
    topic = st.selectbox("Trending topics", topics)
else:
    topic = None

# Step 3: Choose LLM provider and length
provider = st.selectbox("LLM Provider", ["openai", "gemini", "claude"])
length = st.radio("Post length", ["brief", "detailed"])

# Step 4: Generate content
if st.button("Generate Content") and topic:
    content = generate_content(topic, length, provider, config)
    st.session_state["content"] = content

content_box = st.text_area("Content", value=st.session_state.get("content", ""), height=200)

# Step 5: Select platforms
platforms = st.multiselect("Publish to", ["instagram", "linkedin", "substack"])

# Step 6: Publish
if st.button("Publish") and content_box and platforms:
    results = publish_to_platforms(content_box, platforms, config)
    for res in results:
        log_post(res)
    st.success("Published! Check dashboard for results.")

# Step 7: Dashboard
st.subheader("Publishing History")
for item in get_history():
    st.write(item)
