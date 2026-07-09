import feedparser
from datetime import datetime

from src.collectors.base_collector import BaseCollector
from src.models.news import NewsArticle

from src.analytics.entity_extractor import EntityExtractor
from src.analytics.topic_extractor import TopicExtractor



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

        self.topic_extractor = TopicExtractor()



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


            full_text = (
                title
                + " "
                + content
                + " "
                + self.source_name
            )



            companies = self.entity_extractor.extract(
                full_text
            )


            topics = self.topic_extractor.extract(
                full_text
            )



            article = NewsArticle(

                title=title,

                content=content,

                source_name=self.source_name,

                source_type=self.source_type,

                published_at=datetime.now(),

                companies=companies,

                categories="ecommerce",

                topics=topics,

                url=entry.get(
                    "link",
                    ""
                )

            )


            articles.append(article)



        return articles