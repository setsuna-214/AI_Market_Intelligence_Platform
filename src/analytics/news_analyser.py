from collections import Counter



class NewsAnalyser:


    def analyse(self, articles):


        result = {}


        result["total_articles"] = len(
            articles
        )



        result["sources"] = dict(
            Counter(
                article.source_name
                for article in articles
            )
        )



        companies = []

        for article in articles:

            companies.extend(
                article.companies
            )


        result["companies"] = dict(
            Counter(companies)
        )



        topics = []

        for article in articles:

            topics.extend(
                article.topics
            )


        result["topics"] = dict(
            Counter(topics)
        )



        result["categories"] = dict(
            Counter(
                article.categories
                for article in articles
            )
        )


        return result