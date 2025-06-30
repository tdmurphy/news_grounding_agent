from google.adk import Agent
from news_grounding_agent.multi_tool_agent.news_collection_agent.collection_agent_prompt import COLLECTION_AGENT_PROMPT

class NewsCollectionAgent(Agent):
    """
    Agent for collecting news articles from various sources given a company name.
    """

    def __init__(self, name: str = "NewsCollectionAgent", **kwargs):
        super().__init__(name=name, **kwargs)
        self.description = "An agent that collects news articles from various sources."
        self.model = "gemini-1.5-flash"
        self.instruction = COLLECTION_AGENT_PROMPT