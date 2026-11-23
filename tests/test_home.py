from app.main import app


def test_home_page():
    client = app.test_client()
    r = client.get("/")
    assert r.status_code == 200
    assert "CI/CD Demo" in r.get_data(as_text=True)
