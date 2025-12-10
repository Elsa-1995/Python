import pytest
import requests

BASE_URL = "https://ru.yougile.com"
API_KEY = "КЛЮЧ"

HEADERS = {
    "Authorization": "Bearer " + API_KEY,
    "Content-Type": "application/json"
}

@pytest.fixture
def created_project():
    url = BASE_URL + "/api-v2/projects"
    data = {"title": "Тестовый проект"}

    response = requests.post(url, headers=HEADERS, json=data)
    assert response.status_code == 201

    project_data = response.json()

    yield project_data  # Отдаем данные тесту

    # Очистка после теста
    project_id = project_data.get("id")
    if project_id:
        delete_url = BASE_URL + "/api-v2/projects/" + project_id
        delete_data = {"archived": True}
        requests.put(delete_url, headers=HEADERS, json=delete_data)


# ========== ПОЗИТИВНЫЕ ТЕСТЫ ==========

def test_create_project_success():
    url = BASE_URL + "/api-v2/projects"
    data = {"title": "Позитивный тест"}

    response = requests.post(url, headers=HEADERS, json=data)

    assert response.status_code == 201

    # Очистка
    if response.status_code == 201:
        project_id = response.json().get("id")
        if project_id:
            delete_url = BASE_URL + "/api-v2/projects/" + project_id
            delete_data = {"archived": True}
            requests.put(delete_url, headers=HEADERS, json=delete_data)


def test_get_project_success(created_project):
    project_id = created_project.get("id")
    url = BASE_URL + "/api-v2/projects/" + project_id

    response = requests.get(url, headers=HEADERS)

    assert response.status_code == 200


def test_update_project_success(created_project):
    project_id = created_project.get("id")
    url = BASE_URL + "/api-v2/projects/" + project_id
    data = {"title": "Обновленный проект"}

    response = requests.put(url, headers=HEADERS, json=data)

    assert response.status_code == 200


# ========== НЕГАТИВНЫЕ ТЕСТЫ ==========

def test_create_project_empty_title():
    url = BASE_URL + "/api-v2/projects"
    data = {"title": ""}

    response = requests.post(url, headers=HEADERS, json=data)

    assert response.status_code == 400


def test_get_project_invalid_id():
    url = BASE_URL + "/api-v2/projects/invalid-id-123"

    response = requests.get(url, headers=HEADERS)

    assert response.status_code in [400, 404]


def test_update_project_empty_title(created_project):
    project_id = created_project.get("id")
    url = BASE_URL + "/api-v2/projects/" + project_id
    data = {"title": ""}

    response = requests.put(url, headers=HEADERS, json=data)

    assert response.status_code == 400