
import app as flask_app


def test_homepage_returns_200():
    client = flask_app.app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Portal Login" in response.data
