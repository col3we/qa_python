import pytest
from sqlalchemy import create_engine, text

DB_CONNECTION_STRING = (
    "postgresql+psycopg2://myuser:mypassword@localhost:5432/mydatabase"
)


@pytest.fixture(scope="module")
def db_engine():
    engine = create_engine(DB_CONNECTION_STRING)
    yield engine
    engine.dispose()


def test_add_student(db_engine):
    with db_engine.begin() as connection:
        insert_query = text(
            "INSERT INTO students (first_name, last_name, email) "
            "VALUES (:first_name, :last_name, :email) RETURNING id"
        )
        result = connection.execute(
            insert_query,
            {
                "first_name": "Тест",
                "last_name": "Тестов",
                "email": "test@example.com",
            },
        )
        student_id = result.scalar()

        select_query = text(
            "SELECT first_name FROM students WHERE id = :id"
        )
        name = connection.execute(
            select_query, {"id": student_id}
        ).scalar()
        assert name == "Тест"

        delete_query = text("DELETE FROM students WHERE id = :id")
        connection.execute(delete_query, {"id": student_id})


def test_update_student(db_engine):
    with db_engine.begin() as connection:
        insert_query = text(
            "INSERT INTO students (first_name, last_name, email) "
            "VALUES (:first_name, :last_name, :email) RETURNING id"
        )
        student_id = connection.execute(
            insert_query,
            {
                "first_name": "СтароеИмя",
                "last_name": "Фамилия",
                "email": "update@example.com",
            },
        ).scalar()

        update_query = text(
            "UPDATE students SET first_name = :new_name WHERE id = :id"
        )
        connection.execute(
            update_query, {"new_name": "НовоеИмя", "id": student_id}
        )

        select_query = text(
            "SELECT first_name FROM students WHERE id = :id"
        )
        name = connection.execute(
            select_query, {"id": student_id}
        ).scalar()
        assert name == "НовоеИмя"

        connection.execute(
            text("DELETE FROM students WHERE id = :id"),
            {"id": student_id}
        )


def test_delete_student(db_engine):
    with db_engine.begin() as connection:
        insert_query = text(
            "INSERT INTO students (first_name, last_name, email) "
            "VALUES (:first_name, :last_name, :email) RETURNING id"
        )
        student_id = connection.execute(
            insert_query,
            {
                "first_name": "Удаляемый",
                "last_name": "Студент",
                "email": "delete@example.com",
            },
        ).scalar()

        delete_query = text("DELETE FROM students WHERE id = :id")
        connection.execute(delete_query, {"id": student_id})

        select_query = text(
            "SELECT COUNT(*) FROM students WHERE id = :id"
        )
        count = connection.execute(
            select_query, {"id": student_id}
        ).scalar()
        assert count == 0
