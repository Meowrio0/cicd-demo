from app.main import add, app, multiply


def test_add():
    assert add(2, 3) == 5


def test_health():
    client = app.test_client()
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json() == {"status": "ok"}


def test_add_route():
    client = app.test_client()
    r = client.get("/add?a=2&b=3")
    assert r.get_json()["result"] == 5


def test_multiply():
    assert multiply(4, 5) == 20


def test_multiply_route():
    client = app.test_client()
    r = client.get("/multiply?a=4&b=5")
    assert r.get_json()["result"] == 20
