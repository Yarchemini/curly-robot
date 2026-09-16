def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Возвращает список словарей с операциями, у которых ключ state равен переданному значению."""
    return [operation for operation in operations if operation.get("state") == state]


def sort_by_date(operations: list[dict], reverse: bool = True) -> list[dict]:
    """Возвращает список словарей с операциями, отсортированный по дате."""
    return sorted(operations, key=lambda operation: operation["date"], reverse=reverse)
