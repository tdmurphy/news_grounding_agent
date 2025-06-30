from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class News:
    title: str
    url: str
    date: datetime
    summary: str

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "News":
        return cls(
            title=data["title"],
            url=data["url"],
            date=data["date"],
            summary=data["summary"],
        )
