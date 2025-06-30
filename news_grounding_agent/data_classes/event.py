from dataclasses import dataclass, field
from datetime import datetime

from news_grounding_agent.data_classes.news import News

@dataclass
class Event:
    title: str
    date: datetime
    summary: str
    article_list: list[News] = field(default_factory=list)
