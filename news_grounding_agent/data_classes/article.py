from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class Article:
    title: str
    url: str
    date: datetime
    summary: str

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Article":
        return cls(
            title=data["title"],
            url=data["url"],
            date=data["date"],
            summary=data["summary"],
        )
