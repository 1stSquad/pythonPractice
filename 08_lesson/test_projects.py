import pytest
from pages.project_page import ProjectPage
from test_data import (BASE_URL, TOKEN, PROJECT_TITLE_VALID,
                       PROJECT_TITLE_INVALID, PROJECT_TITLE_UPDATED)


headers = {
    'Authorization': f'bearer {TOKEN}',
    'Content-Type': 'application/json'
}


@pytest.fixture()
def project_page():
    return ProjectPage(BASE_URL, headers)


@pytest.fixture()
def create_project(project_page):
    response = project_page.create_project(PROJECT_TITLE_VALID)
    assert response.status_code == 201
    project_id = response.json()['id']
    yield project_id


def test_create_project_positive(project_page):
    response = project_page.create_project(PROJECT_TITLE_VALID)
    assert response.status_code == 201
    assert 'id' in response.json()


def test_create_project_negative(project_page):
    response = project_page.create_project(PROJECT_TITLE_INVALID)
    assert response.status_code == 400


def test_get_project_positive(project_page):
    response = project_page.get_projects()
    assert response.status_code == 200
    assert "content" in response.json()
    assert isinstance(response.json()["content"], list)


def test_get_project_id_positive(project_page, create_project):
    project_id = create_project
    response = project_page.get_project_by_id(project_id)
    assert response.status_code == 200
    assert response.json()["id"] == project_id
    assert "id" in response.json()


def test_update_project_positive(project_page, create_project):
    project_id = create_project
    response = project_page.update_project(project_id, PROJECT_TITLE_UPDATED)
    assert response.status_code == 200
    assert "id" in response.json()


def test_update_project_negative(project_page, create_project):
    project_id = create_project
    response = project_page.update_project(project_id, '')
    assert response.status_code == 400