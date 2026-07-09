from dataclasses import dataclass
from typing import List
from datetime import datetime

@dataclass
class NewsArticle:
    title: str
    content: str
    source_name: str
    source_type: str
    published_at: datetime
    companies: List[str]
    categories: str
    url: str = ""