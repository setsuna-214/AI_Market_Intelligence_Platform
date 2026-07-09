import feedparser
from datetime import datetime

from src.collectors.base_collector import BaseCollector
from src.models.news import NewsArticle


class RSSCollector(BaseCollector):

    def __init__(
        self,
        rss_url,
        source_name,
        source_type
    ):
        self.rss_url = rss_url
        self.source_name = source_name
        self.source_type = source_type


    def collect(self):

        feed = feedparser.parse(self.rss_url)

        articles = []

        for entry in feed.entries:

            article = NewsArticle(
                title=entry.title,
                content=entry.get("summary", ""),
                source_name=self.source_name,
                source_type=self.source_type,
                published_at=datetime.now(),
                companies=[],
                categories="ecommerce",
                url=entry.link
            )

            articles.append(article)

        return articles