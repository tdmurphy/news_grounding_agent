from google.adk.agents import LlmAgent

from news_grounding_agent.data_classes.event import Event
from news_grounding_agent.data_classes.event_evaluation import EventEvaluation
from news_grounding_agent.multi_tool_agent.event_analysis_agent.prompt import (
    EVENT_ANALYSIS_AGENT_INSTRUCTION,
)


def classify_event_sentiment(event_dict: dict) -> dict:
    """
    A tool that takes a dictionary representing an Event,
    classifies its articles by sentiment, and returns a
    dictionary representing an EventEvaluation.
    """
    # 1. Deserialize dict back into an Event object
    event = Event.from_dict(event_dict)

    # --- Your sentiment analysis logic would go here ---
    # (For demonstration, we'll just create dummy lists)
    positive_articles = [
        article
        for article in event.article_list
        if "positive" in article.summary.lower()
    ]
    negative_articles = [
        article
        for article in event.article_list
        if "negative" in article.summary.lower()
    ]
    neutral_articles = [
        article
        for article in event.article_list
        if "neutral" in article.summary.lower()
    ]
    # ---

    # 2. Create the final EventEvaluation object
    evaluation = EventEvaluation(
        event=event,
        positive_articles=positive_articles,
        negative_articles=negative_articles,
        neutral_articles=neutral_articles,
    )

    # 3. Serialize the output object to a dict before returning
    return evaluation.to_dict()


# You would then provide this `classify_event_sentiment` function
# to your ADK agent in its list of tools.

event_analysis_agent = LlmAgent(
    model="gemini-1.5-flash-latest",
    name="event_analysis_agent",
    description="This agent analyzes a single event and classifies its associated news articles by sentiment.",
    instruction=EVENT_ANALYSIS_AGENT_INSTRUCTION,
    tools=[classify_event_sentiment],
)
