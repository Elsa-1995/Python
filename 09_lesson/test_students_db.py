from StudentTable import StudentTable

# Подключение
db = StudentTable("postgresql://postgres:1234@localhost:5050/my_new_db")


def test_add_student():
    """Тест 1: Добавление студента"""
    name = "Иван Иванов"
    email = "ivan@example.com"

    # Добавляем студента
    db.create(name, email)
    new_id = db.get_max_id()

    # Получаем студента
    student = db.get_student_by_id(new_id)

    # Удаляем (очистка)
    db.delete_student(new_id)

    # Проверяем
    assert len(student) == 1
    assert student[0]["name"] == name
    assert student[0]["email"] == email
    print(f"✓ Студент добавлен: {name}")


def test_update_student():
    """Тест 2: Изменение студента"""
    # Создаем
    db.create("Петр Петров", "petr@example.com")
    student_id = db.get_max_id()

    # Удаляем старого
    db.delete_student(student_id)

    # Создаем с новыми данными (имитация изменения)
    db.create("Петр Сидоров", "petr_sidorov@example.com")
    new_id = db.get_max_id()

    # Получаем
    student = db.get_student_by_id(new_id)

    # Удаляем (очистка)
    db.delete_student(new_id)

    # Проверяем изменения
    assert student[0]["name"] == "Петр Сидоров"
    assert student[0]["email"] == "petr_sidorov@example.com"
    print(f"✓ Студент изменен: Петр Сидоров")


def test_delete_student():
    """Тест 3: Удаление студента"""
    # Создаем
    db.create("Анна Смирнова", "anna@example.com")
    student_id = db.get_max_id()

    # Удаляем
    db.delete_student(student_id)

    # Проверяем что удален
    student = db.get_student_by_id(student_id)
    assert len(student) == 0
    print(f"✓ Студент удален: ID {student_id}")
