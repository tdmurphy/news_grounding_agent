from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from .collection_agent_prompt import COLLECTION_AGENT_PROMPT
from .pydantic_models import ArticleList

news_collection_agent = LlmAgent(
    model="gemini-2.0-flash-latest",
    name="news_collection_agent",
    description="An agent that collects news articles from various sources and returns them as a structured list.",
    instruction=COLLECTION_AGENT_PROMPT,
    tools=[google_search],
    response_model=ArticleList,
)
