from pydantic import BaseModel, Field
from datetime import datetime


class NewsArticle(BaseModel):
    """A model representing a single news article."""

    title: str = Field(..., description="The title of the news article.")
    url: str = Field(..., description="The URL where the article can be found.")
    date: datetime = Field(..., description="The publication date of the article.")
    summary: str = Field(..., description="A brief summary of the article's content.")


class ArticleList(BaseModel):
    """A list of news articles."""

    articles: list[NewsArticle]
