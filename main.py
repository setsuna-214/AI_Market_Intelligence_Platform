from src.collectors.rss_collector import RSSCollector
from src.database.json_storage import JSONStorage
from src.database.json_reader import JSONReader
from src.analytics.news_analyser import NewsAnalyser
from src.reporting.report_generator import ReportGenerator


def main():


    collector = RSSCollector(

        "https://news.google.com/rss/search?q=中国+电商",

        "Google News",

        "aggregator"

    )


    news = collector.collect()



    print(
        "Collected articles:",
        len(news)
    )


    print("\nEntity Extraction Result:\n")


    for article in news[:10]:

        print("----------------")

        print(
            article.title
        )

        print(
            "Companies:",
            article.companies
        )



    storage = JSONStorage(

        "data/raw/news.json"

    )


    storage.save(news)



    reader = JSONReader(

        "data/raw/news.json"

    )


    articles = reader.load()



    analyser = NewsAnalyser()


    result = analyser.analyse(
        articles
    )


    report_generator = ReportGenerator(
    "reports/daily_report.md"
    )


    report_generator.generate(
        result
    )


    print(
        "Report generated!"
    )



if __name__ == "__main__":

    main()