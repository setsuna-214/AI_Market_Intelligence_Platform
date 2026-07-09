import feedparser
from datetime import datetime

from src.collectors.base_collector import BaseCollector
from src.models.news import NewsArticle
from src.analytics.entity_extractor import EntityExtractor


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

        self.entity_extractor = EntityExtractor()



    def collect(self):

        feed = feedparser.parse(
            self.rss_url
        )


        articles = []


        for entry in feed.entries:


            title = entry.get(
                "title",
                ""
            )


            content = entry.get(
                "summary",
                ""
            )


            companies = self.entity_extractor.extract(
                title 
                + " "
                + content
                + " "
                + self.source_name
            )


            article = NewsArticle(

                title=title,

                content=content,

                source_name=self.source_name,

                source_type=self.source_type,

                published_at=datetime.now(),

                companies=companies,

                categories="ecommerce",

                url=entry.get(
                    "link",
                    ""
                )
            )


            articles.append(article)


        return articles