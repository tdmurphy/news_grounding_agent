from dataclasses import dataclass
from datetime import datetime

@dataclass
class News:
    title: str
    url: str
    date: datetime
    summary: str