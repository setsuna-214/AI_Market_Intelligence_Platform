import re


class EntityExtractor:


    def __init__(self):

        self.company_keywords = {


            "JD.com": "JD",

            "Jingdong": "JD",

            "京东": "JD",

            "京东物流": "JD Logistics",



            "Alibaba Group": "Alibaba",

            "Alibaba": "Alibaba",

            "AliExpress": "Alibaba",

            "阿里巴巴": "Alibaba",

            "阿里": "Alibaba",

            "Taobao": "Taobao",

            "淘宝": "Taobao",

            "Tmall": "Tmall",

            "天猫": "Tmall",



            "Pinduoduo": "PDD",

            "PDD": "PDD",

            "Temu": "PDD",

            "拼多多": "PDD",



            "TikTok Shop": "TikTok Shop",

            "TikTok": "TikTok",

            "Douyin": "Douyin Ecommerce",

            "抖音": "Douyin Ecommerce",



            "Amazon": "Amazon",

            "亚马逊": "Amazon",

            "Walmart": "Walmart",

            "Shopify": "Shopify",

            "eBay": "eBay"

        }



    def extract(self, text):


        companies = []


        for keyword, company in self.company_keywords.items():


            if self._match_keyword(
                keyword,
                text
            ):


                if company not in companies:

                    companies.append(company)



        return companies



    def _match_keyword(
        self,
        keyword,
        text
    ):


        # Chinese keywords
        # direct matching

        if re.search(
            r"[\u4e00-\u9fff]",
            keyword
        ):

            return keyword in text



        # English keywords
        # word boundary matching

        pattern = (
            r"\b"
            + re.escape(keyword)
            + r"\b"
        )


        return re.search(
            pattern,
            text,
            re.IGNORECASE
        ) is not None