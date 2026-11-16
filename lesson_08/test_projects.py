import os
import pytest
from dotenv import load_dotenv
from .yougile_api import YougileProjectsApi

load_dotenv()
BASE_URL = "https://ru.yougile.com/api-v2"
TOKEN = os.getenv("YOUGILE_TOKEN")


@pytest.fixture
def api():
    return YougileProjectsApi(BASE_URL, TOKEN)


@pytest.fixture
def created_project(api):
    response = api.create_project({"title": "Test Base Project"})
    project_id = response.json().get("id")
    yield project_id


def test_create_project_positive(api):
    response = api.create_project({"title": "New Auto Project"})
    assert response.status_code == 201
    assert "id" in response.json()


def test_create_project_negative(api):
    response = api.create_project({"title": ""})
    assert response.status_code in [400, 422]


def test_get_project_positive(api, created_project):
    response = api.get_project(created_project)
    assert response.status_code == 200
    assert response.json().get("id") == created_project


def test_get_project_negative(api):
    fake_id = "00000000-0000-0000-0000-000000000000"
    response = api.get_project(fake_id)
    assert response.status_code == 404


def test_update_project_positive(api, created_project):
    response = api.update_project(
        created_project, {"title": "Updated Project Name"}
    )
    assert response.status_code == 200
    assert response.json().get("title") == "Updated Project Name"


def test_update_project_negative(api):
    fake_id = "00000000-0000-0000-0000-000000000000"
    response = api.update_project(
        fake_id, {"title": "Should Fail"}
    )
    assert response.status_code in [400, 404]
