from sqlalchemy import create_engine, text


class StudentTable:
    __scripts = {
        "select": text("SELECT * FROM students WHERE deleted_at IS NULL"),
        "select only active": text("SELECT * FROM students WHERE is_active = true AND deleted_at IS NULL"),
        "delete by id": text("DELETE FROM students WHERE id = :id_to_delete"),
        "insert_new": text("INSERT INTO students(name, email) VALUES (:name, :email)"),
        "get_max_id": text("SELECT MAX(id) FROM students WHERE deleted_at IS NULL"),
        "select by id": text("SELECT * FROM students WHERE id = :select_id AND deleted_at IS NULL")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_students(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select"])
        rows = result.mappings().all()
        conn.close()
        return rows

    def get_active_students(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select only active"])
        rows = result.mappings().all()
        conn.close()
        return rows

    def delete_student(self, student_id):
        with self.__db.connect() as connection:
            transaction = connection.begin()
            sql_statement = self.__scripts["delete by id"]
            connection.execute(sql_statement, {"id_to_delete": student_id})
            transaction.commit()

    def create(self, name, email):
        conn = self.__db.connect()
        conn.execute(self.__scripts["insert_new"], {"name": name, "email": email})
        conn.commit()
        conn.close()

    def get_max_id(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["get_max_id"])
        max_id = result.scalar()
        conn.close()
        return max_id

    def get_student_by_id(self, student_id):
        conn = self.__db.connect()
        result = conn.execute(
            self.__scripts["select by id"],
            {"select_id": student_id}
        )
        student = result.mappings().all()
        conn.close()
        return student