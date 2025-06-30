from dataclasses import dataclass

from news_grounding_agent.data_classes.event import Event
from news_grounding_agent.data_classes.news import News

@dataclass
class EventEvaluation:
    event: Event
    positive_articles: list[News]
    negative_articles: list[News]
    neutral_articles: list[News]