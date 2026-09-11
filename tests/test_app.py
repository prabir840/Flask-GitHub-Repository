from app import app


def test_home_page_renders_application_content():
    response = app.test_client().get("/")

    assert response.status_code == 200
    assert b"Ship with" in response.data
    assert b"confidence." in response.data


def test_health_endpoint_returns_successful_plain_text_response():
    response = app.test_client().get("/health")

    assert response.status_code == 200
    assert response.text == "healthy"
    assert response.mimetype == "text/plain"