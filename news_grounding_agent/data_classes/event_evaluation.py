from dataclasses import dataclass, asdict

from news_grounding_agent.data_classes.event import Event
from news_grounding_agent.data_classes.news import News


@dataclass
class EventEvaluation:
    event: Event
    positive_articles: list[News]
    negative_articles: list[News]
    neutral_articles: list[News]

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "EventEvaluation":
        return cls(
            event=Event.from_dict(data["event"]),
            positive_articles=[
                News.from_dict(n) for n in data.get("positive_articles", [])
            ],
            negative_articles=[
                News.from_dict(n) for n in data.get("negative_articles", [])
            ],
            neutral_articles=[
                News.from_dict(n) for n in data.get("neutral_articles", [])
            ],
        )
