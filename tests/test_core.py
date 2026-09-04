from payloadlab import catalog, normalize

def test_catalog():
    assert normalize({"name": "demo"})["name"] == "demo"
    assert len(catalog([{"category": "web"}, {"category": "host"}], "web")) == 1
