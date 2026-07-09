import re



class TopicExtractor:


    def __init__(self):


        self.topic_keywords = {


            "Cross-border Ecommerce": [

                "cross-border",

                "cross border",

                "overseas",

                "global expansion",

                "international",

                "出海",

                "海外"

            ],



            "Logistics": [

                "logistics",

                "warehouse",

                "delivery",

                "supply chain",

                "shipping",

                "物流",

                "仓"

            ],



            "Regulation": [

                "regulation",

                "investigation",

                "fine",

                "ban",

                "policy",

                "监管",

                "调查"

            ],



            "AI Commerce": [

                "artificial intelligence",

                "machine learning",

                "AI technology",

                "AI-powered",

                "人工智能",

                "智能"

            ],



            "Consumer Behaviour": [

                "consumer",

                "shopping",

                "discount",

                "retail",

                "消费",

                "购物"

            ]

        }



    def extract(
        self,
        text
    ):


        topics = []


        for topic, keywords in self.topic_keywords.items():


            for keyword in keywords:


                if self._match_keyword(
                    keyword,
                    text
                ):

                    topics.append(topic)

                    break



        return topics



    def _match_keyword(
        self,
        keyword,
        text
    ):


        if re.search(
            r"[\u4e00-\u9fff]",
            keyword
        ):

            return keyword in text



        pattern = (
            r"\b"
            +
            re.escape(keyword)
            +
            r"\b"
        )


        return re.search(
            pattern,
            text,
            re.IGNORECASE
        ) is not None