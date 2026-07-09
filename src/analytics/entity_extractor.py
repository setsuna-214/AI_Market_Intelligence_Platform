class EntityExtractor:


    def __init__(self):

        self.company_keywords = {


            # Alibaba Group

            "Alibaba": "Alibaba",
            "Alibaba Group": "Alibaba",
            "AliExpress": "Alibaba",
            "Taobao": "Taobao",
            "Tmall": "Tmall",
            "天猫": "Tmall",
            "淘宝": "Taobao",
            "阿里": "Alibaba",
            "阿里巴巴": "Alibaba",



            # JD

            "JD": "JD",
            "JD.com": "JD",
            "Jingdong": "JD",
            "京东": "JD",
            "京东物流": "JD Logistics",



            # PDD

            "PDD": "PDD",
            "Pinduoduo": "PDD",
            "Temu": "PDD",
            "拼多多": "PDD",



            # ByteDance

            "TikTok Shop": "TikTok Shop",
            "TikTok": "TikTok",
            "Douyin": "Douyin Ecommerce",
            "抖音": "Douyin Ecommerce",



            # Kuaishou

            "Kuaishou": "Kuaishou",
            "快手": "Kuaishou",



            # Global ecommerce

            "Amazon": "Amazon",
            "亚马逊": "Amazon",

            "Walmart": "Walmart",

            "Shopify": "Shopify",

            "eBay": "eBay"



        }



    def extract(self, text):


        companies = []


        text_lower = text.lower()



        for keyword, company in self.company_keywords.items():


            if keyword.lower() in text_lower:


                if company not in companies:

                    companies.append(company)



        return companies