"""Общие фикстуры для тестов проекта."""

import pytest


@pytest.fixture
def valid_card_number() -> str:
    """Корректный 16-значный номер карты."""
    return "7000792289606361"


@pytest.fixture
def valid_account_number() -> str:
    """Корректный номер банковского счета."""
    return "73654108430135874305"


@pytest.fixture
def operations_list() -> list[dict]:
    """Список операций с разными значениями state и date."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 3, "state": "EXECUTED", "date": "2020-01-15T09:12:00.000000"},
        {"id": 4, "state": "PENDING", "date": "2017-05-01T00:00:00.000000"},
    ]


@pytest.fixture
def operations_same_date() -> list[dict]:
    """Список операций с одинаковой датой — для проверки стабильности сортировки."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 3, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def empty_operations_list() -> list[dict]:
    """Пустой список операций."""
    return []
 feature/generators


@pytest.fixture
def transactions_with_currency() -> list[dict]:
    """Список транзакций с разными кодами валют — для тестов generators."""
    return [
        {"id": 1, "operationAmount": {"currency": {"code": "USD"}}, "description": "Перевод организации"},
        {"id": 2, "operationAmount": {"currency": {"code": "USD"}}, "description": "Перевод со счета на счет"},
        {"id": 3, "operationAmount": {"currency": {"code": "RUB"}}, "description": "Перевод со счета на счет"},
        {"id": 4, "operationAmount": {"currency": {"code": "USD"}}, "description": "Перевод с карты на карту"},
        {"id": 5, "operationAmount": {"currency": {"code": "RUB"}}, "description": "Перевод организации"},
    ]
=======
 main
