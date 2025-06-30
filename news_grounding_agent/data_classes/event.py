from dataclasses import dataclass, field, asdict
from datetime import datetime

from news_grounding_agent.data_classes.article import Article


@dataclass
class Event:
    title: str
    date: datetime
    summary: str
    article_list: list[Article] = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Event":
        return cls(
            title=data["title"],
            date=data["date"],
            summary=data["summary"],
            article_list=[Article.from_dict(n) for n in data.get("article_list", [])],
        )
