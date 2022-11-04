def test_get_all_breakfasts_with_empty_db_return_empty_list(client):
    response = client.get("/breakfast")
    response_body = response.get_json()

    assert response_body == []
    assert response.status_code == 200

def test_get_one_breakfast_with_empty_db_returns_404(client):
    response = client.get("/breakfast/1") # http method .get
    response_body = response.get_json()

    assert response.status_code == 404
    assert "message" in response_body


def test_get_one_breakfast_with_populated_db_returns_breakfast_json(client, two_breakfasts):
    response = client.get("/breakfast/1") # http method .get
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "french toast",
        "prep_time": 15,
        "rating": 3.0
    }

def test_post_one_breakfast_creates_bike_in_db(client, two_breakfasts):
    response = client.post("/breakfast", json={
        "name": "coffee",
        "prep_time": 10,
        "rating": 5.0
    })
    response_body = response.get_json()

    assert response.status_code == 201
    assert "msg" in response_body
    assert response_body["msg"] == 'Successfully created Breakfast with id =3'
   