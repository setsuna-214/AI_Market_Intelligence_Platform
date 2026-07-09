from src.collectors.rss_collector import RSSCollector
from src.database.json_storage import JSONStorage


def main():

    collector = RSSCollector(
        "https://news.google.com/rss/search?q=中国+电商",
        "Google News",
        "aggregator"
    )

    news = collector.collect()


    storage = JSONStorage(
        "data/raw/news.json"
    )

    storage.save(news)


    print(
        "Saved articles:",
        len(news)
    )


if __name__ == "__main__":
    main()