from typing import Any


def filter_by_state(operations: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """
    Отфильтровывает список операций по значению ключа state.

    Args:
        operations: Список словарей с данными о банковских операциях.
            Каждый словарь должен содержать ключ "state".
        state: Значение ключа "state", по которому нужно отфильтровать
            операции. По умолчанию "EXECUTED".

    Returns:
        Новый список словарей, содержащий только те операции, у которых
        значение ключа "state" равно переданному аргументу state.
    """
    return [operation for operation in operations if operation.get("state") == state]


def sort_by_date(operations: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """
    Сортирует список операций по значению ключа date.

    Args:
        operations: Список словарей с данными о банковских операциях.
            Каждый словарь должен содержать ключ "date" со строкой
            в формате ISO 8601 (например, "2019-07-03T18:35:29.512364").
        reverse: Порядок сортировки. True — от новых операций к старым
            (по убыванию даты), False — от старых к новым (по возрастанию
            даты). По умолчанию True.

    Returns:
        Новый список словарей, отсортированный по дате. Исходный список
        не изменяется.
    """
    return sorted(operations, key=lambda operation: operation["date"], reverse=reverse)