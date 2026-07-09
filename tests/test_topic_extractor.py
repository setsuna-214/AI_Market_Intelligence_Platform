from src.analytics.topic_extractor import TopicExtractor



def test_cross_border_topic():

    extractor = TopicExtractor()


    result = extractor.extract(
        "Chinese sellers expand overseas ecommerce"
    )


    assert "Cross-border Ecommerce" in result



def test_ai_topic():

    extractor = TopicExtractor()


    result = extractor.extract(
        "AI-powered ecommerce recommendation system"
    )


    assert "AI Commerce" in result