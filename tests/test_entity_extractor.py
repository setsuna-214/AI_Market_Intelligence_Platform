from src.analytics.entity_extractor import EntityExtractor



def test_jd_detection():

    extractor = EntityExtractor()


    result = extractor.extract(
        "JD.com expands overseas logistics network"
    )


    assert "JD" in result



def test_no_false_jd():

    extractor = EntityExtractor()


    result = extractor.extract(
        "China ecommerce market is growing"
    )


    assert "JD" not in result