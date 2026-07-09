import json
from pathlib import Path
from datetime import datetime

from src.models.news import NewsArticle


class JSONReader:


    def __init__(self, path):

        self.path = Path(path)



    def load(self):

        with open(
            self.path,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)


        articles = []


        for item in data:

            article = NewsArticle(

                title=item["title"],

                content=item["content"],

                source_name=item["source_name"],

                source_type=item["source_type"],

                published_at=datetime.fromisoformat(
                    item["published_at"]
                ),

                companies=item["companies"],

                categories=item["categories"],

                url=item["url"]
            )


            articles.append(article)


        return articles