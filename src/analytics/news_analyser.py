from collections import Counter


class NewsAnalyser:

    def analyse(self, articles):

        result = {}

        # 新闻数量
        result["total_articles"] = len(articles)


        # 来源统计
        sources = [
            article.source_name
            for article in articles
        ]

        result["sources"] = dict(
            Counter(sources)
        )


        # 公司统计
        companies = []

        for article in articles:
            companies.extend(
                article.companies
            )

        result["companies"] = dict(
            Counter(companies)
        )


        # 分类统计
        categories = [
            article.categories
            for article in articles
        ]

        result["categories"] = dict(
            Counter(categories)
        )


        return result