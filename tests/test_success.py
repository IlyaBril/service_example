import pytest
from service_example.app.main import create_app


@pytest.fixture()
def client():
    app = create_app()
    return app.test_client()


def test_success_handler(client):
    response = client.get('/success')
    assert response.status_code == 200
    assert response.json['success']