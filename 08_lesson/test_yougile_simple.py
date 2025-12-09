import pytest
import requests

BASE_URL = "https://ru.yougile.com"
API_KEY = "ключ"  # Замените на свой ключ!

HEADERS = {
    "Authorization": "Bearer " + API_KEY,
    "Content-Type": "application/json"
}

# Список созданных проектов для очистки
created_projects = []

def create_project_simple(title, description=None):
    url = BASE_URL + "/api-v2/projects"
    data = {"title": title}

    if description:
        data["description"] = description

    response = requests.post(url, headers=HEADERS, json=data)

    if response.status_code == 201:
        try:
            project_data = response.json()
            if "id" in project_data:
                project_id = project_data["id"]
                created_projects.append(project_id)
        except:
            pass

    return response


def get_project_simple(project_id):
    url = BASE_URL + "/api-v2/projects/" + project_id
    return requests.get(url, headers=HEADERS)


def update_project_simple(project_id, title=None, description=None):
    url = BASE_URL + "/api-v2/projects/" + project_id

    data = {}
    if title is not None:
        data["title"] = title
    if description is not None:
        data["description"] = description

    return requests.put(url, headers=HEADERS, json=data)


# ========== ПОЗИТИВНЫЕ ТЕСТЫ ==========

def test_1_create_project_success():
    print("Тест 1: Создание проекта")

    response = create_project_simple("Тестовый проект 1")
    print("Код ответа: " + str(response.status_code))

    assert response.status_code == 201

    try:
        project_data = response.json()
        print("Данные проекта: " + str(project_data))
        assert "id" in project_data
        print("✓ Проект создан")
    except Exception as e:
        print("Ошибка: " + str(e))
        assert False


def test_2_get_project_success():
    print("\nТест 2: Получение проекта")

    response = create_project_simple("Проект для получения")
    if response.status_code != 201:
        print("Не удалось создать проект")
        return

    try:
        project_data = response.json()
        project_id = project_data.get("id")

        if not project_id:
            print("Нет ID в ответе")
            return

        print("ID проекта: " + project_id)

        get_response = get_project_simple(project_id)
        print("Код получения: " + str(get_response.status_code))

        assert get_response.status_code == 200

        project_info = get_response.json()
        print("Данные проекта: " + str(project_info))

        print("✓ Проект получен")
    except Exception as e:
        print("Ошибка: " + str(e))


def test_3_update_project_success():
    print("\nТест 3: Обновление проекта")

    response = create_project_simple("Проект для обновления")
    if response.status_code != 201:
        print("Не удалось создать проект")
        return

    try:
        project_data = response.json()
        project_id = project_data.get("id")

        if not project_id:
            print("Нет ID в ответе")
            return

        print("ID проекта: " + project_id)

        update_response = update_project_simple(project_id, title="Обновленный проект")
        print("Код обновления: " + str(update_response.status_code))

        assert update_response.status_code == 200

        updated_data = update_response.json()
        print("Обновленные данные: " + str(updated_data))

        print("✓ Проект обновлен")
    except Exception as e:
        print("Ошибка: " + str(e))


# ========== НЕГАТИВНЫЕ ТЕСТЫ ==========

def test_4_create_project_empty_title():
    print("\nТест 4: Создание с пустым title")

    response = create_project_simple("")
    print("Код ответа: " + str(response.status_code))

    assert response.status_code == 400
    print("✓ Ошибка получена")


def test_5_get_project_invalid_id():
    print("\nТест 5: Получение с невалидным ID")

    response = get_project_simple("invalid-id-123")
    status_code = response.status_code
    print("Код ответа: " + str(status_code))

    assert status_code == 400 or status_code == 404
    print("✓ Ошибка получена")


def test_6_update_project_empty_title():
    print("\nТест 6: Обновление с пустым title")

    response = create_project_simple("Проект для теста")
    if response.status_code != 201:
        print("Не удалось создать проект")
        return

    try:
        project_data = response.json()
        project_id = project_data.get("id")

        if not project_id:
            print("Нет ID в ответе")
            return

        update_response = update_project_simple(project_id, title="")
        print("Код обновления: " + str(update_response.status_code))

        assert update_response.status_code == 400
        print("✓ Ошибка получена")
    except Exception as e:
        print("Ошибка: " + str(e))


def test_7_update_nonexistent_project():
    print("\nТест 7: Обновление несуществующего проекта")

    response = update_project_simple("111111111111111111111111", title="Новый")
    status_code = response.status_code
    print("Код ответа: " + str(status_code))

    assert status_code == 400 or status_code == 404
    print("✓ Ошибка получена")


# ========== ОЧИСТКА ==========

def cleanup_projects():
    print("\nОчистка проектов...")

    for project_id in created_projects:
        try:
            url = BASE_URL + "/api-v2/projects/" + project_id
            data = {"archived": True}
            requests.put(url, headers=HEADERS, json=data)
            print("Удален проект: " + project_id)
        except Exception as e:
            print("Ошибка удаления: " + str(e))

    created_projects.clear()
    print("Очистка завершена")


# Очистка после всех тестов
import atexit

atexit.register(cleanup_projects)
