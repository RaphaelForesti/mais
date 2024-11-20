from http import HTTPStatus


def test_user(client):
    response = client.post(
        '/users',
        json={
            'username': 'raphael.santos',
            'email': 'raphael.santos@test.com',
            'password': 'pass',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
