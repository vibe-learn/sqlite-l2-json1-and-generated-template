"""Homework scaffold — sqlite lesson `l2_json1_and_generated` (Vibe Learn).

Задача: хранилище событий с JSON-полем data + generated column user_id (индекс) и json_each по тегам.

Реализуй функции ниже — сигнатуры и тестовая поверхность фиксированы;
CI (.github/workflows/ci.yml) ставит зависимости и гоняет `pytest`.
Подробности и критерии приёмки — в README.md.

SQLite встроена в Python через stdlib `sqlite3` — никакого драйвера ставить
не нужно, сервера нет. БД это файл (DATABASE_PATH) или ":memory:" в тестах.
"""

import os
import sqlite3


def database_path() -> str:
    """Путь к файлу БД из env. Дефолт ":memory:" — БД живёт в процессе."""
    return os.environ.get("DATABASE_PATH", ":memory:")


def connect(path: str | None = None) -> sqlite3.Connection:
    """Открыть соединение sqlite3 (по умолчанию из database_path())."""
    return sqlite3.connect(path if path is not None else database_path())


# ----- TODO #1: ensure_schema -----
def ensure_schema(conn) -> None:
    """events(id, data TEXT) + generated column user_id AS (json_extract(data,'$.user_id')) с индексом"""
    raise NotImplementedError("ensure_schema: реализуй меня")


# ----- TODO #2: insert_event -----
def insert_event(conn, data: dict) -> int:
    """вставить событие (data сериализуется в JSON), вернуть id"""
    raise NotImplementedError("insert_event: реализуй меня")


# ----- TODO #3: find_by_user -----
def find_by_user(conn, user_id) -> list[dict]:
    """фильтр по индексированной generated-колонке user_id (проверь EXPLAIN QUERY PLAN — USING INDEX)"""
    raise NotImplementedError("find_by_user: реализуй меня")


# ----- TODO #4: find_by_tag -----
def find_by_tag(conn, tag: str) -> list[dict]:
    """json_each по '$.tags' — события, содержащие тег в массиве"""
    raise NotImplementedError("find_by_tag: реализуй меня")



def main() -> None:
    """Точка входа: подключиться и напомнить, что реализовать.

    Замени тело на демонстрацию реализованных функций.
    """
    print("Vibe Learn — sqlite lesson scaffold up")
    print(f"DATABASE_PATH: {database_path()} (stdlib sqlite3, no server)")
    print("Реализуй TODO-функции, затем `pytest`. README.md содержит задачу.")


if __name__ == "__main__":
    main()
