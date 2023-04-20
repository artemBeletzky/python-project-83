import pytest
from flask import Flask
from flask.testing import FlaskClient

from page_analyzer import app


@pytest.fixture()
def setup_app_instance() -> Flask:
    app_instance = app
    app_instance.config.update(
        {
            "TESTING": True,
        }
    )
    # for future setups
    yield app_instance
    # for future tear downs


@pytest.fixture()
def client(setup_app_instance) -> FlaskClient:
    return setup_app_instance.test_client()


def test_request_to_root(client):
    response = client.get("/")
    assert (
        response.status_code == 200
    ), 'GET request to "/" has status code different from 200'
