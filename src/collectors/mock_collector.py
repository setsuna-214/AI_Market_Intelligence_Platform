from datetime import datetime

from src.collectors.base_collector import BaseCollector
from src.models.news import NewsArticle

class MockCollector(BaseCollector):
    def collect(self):
        # Return a list of mock NewsArticle objects for testing purposes
        return [
            NewsArticle(
                title="Mock Article 1",
                content="This is the content of mock article 1.",
                source_name="Mock Source 1",
                source_type="RSS",
                published_at=datetime.now(),
                companies=["Company A", "Company B"],
                categories="Category 1",
                url="https://example.com/mock-article-1"
            ),
            NewsArticle(
                title="Mock Article 2",
                content="This is the content of mock article 2.",
                source_name="Mock Source 2",
                source_type="RSS",
                published_at=datetime.now(),
                companies=["Company C"],
                categories="Category 2",
                url="https://example.com/mock-article-2"
            )
        ]