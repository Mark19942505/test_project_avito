import requests

BASE_URL = "https://qa-internship.avito.com/api/1/item"



def test_create_ad():
    response = requests.post(BASE_URL, json={
        "name": "Кирпич",
        "price": 10000,
        "sellerId": 3452,
        "statistics": {
            "contacts": 32,
            "like": 35,
            "viewCount": 14
        }
    })
    assert response.status_code == 200
    assert response.json()
    ad = response.json()


def test_get_ad():
    response = requests.get(f"{BASE_URL}/{id}")
    assert response.status_code == 200
    ad = response.json()


def test_get_ads_by_seller():
    response = requests.get(f"https://qa-internship.avito.com/api/1/:sellerID/item")
    assert response.status_code == 200
    ads = response.json()
    assert isinstance(ads, list)
    assert len(ads) > 0
    for ad in ads:
        assert "id" in ad
        assert "name" in ad
        assert "price" in ad
        assert "sellerId" in ad

def test_create_ad_missing_fields():
    response = requests.post(BASE_URL, json={
        "price": 10000,
        "sellerId": 3452
    })
    assert response.status_code == 500

def test_get_non_existent_ad():
    non_existent_id = "non_existent_id"
    response = requests.get(f"{BASE_URL}/{non_existent_id}")
    assert response.status_code == 404

if __name__ == "__test_ads.py__":
    ad_id = test_create_ad()
    test_get_ad(ad_id)
    test_get_ads_by_seller(3452)
    test_create_ad_missing_fields()
    test_get_non_existent_ad()