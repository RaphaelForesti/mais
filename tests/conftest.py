import pytest
from fastapi.testclient import TestClient

from mais.app import app


@pytest.fixture
def client():
    with TestClient(app=app) as client:
        yield client