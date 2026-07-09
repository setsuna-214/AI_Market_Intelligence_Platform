# print("test")

from src.collectors.rss_collector import RSSCollector


def main():

    collector = RSSCollector(
        "https://news.google.com/rss/search?q=中国+电商",
        "Google News",
        "aggregator"
    )

    news = collector.collect()


    print("Total articles:", len(news))

    for article in news[:5]:
        print("----------------")
        print(article.title)
        print(article.source_name)
        print(article.url)


if __name__ == "__main__":
    main()