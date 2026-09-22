from typing import Any, Iterator


def filter_by_currency(transactions: list[dict[str, Any]], currency_code: str) -> Iterator[dict[str, Any]]:
    """
    Отфильтровывает транзакции по коду валюты операции.

    Args:
        transactions: Список словарей с данными о транзакциях. Каждый
            словарь должен содержать ключ "operationAmount" с вложенным
            словарем "currency", в котором есть ключ "code".
        currency_code: Код валюты, по которому нужно отфильтровать
            транзакции (например, "USD", "RUB").

    Returns:
        Итератор, поочередно выдающий транзакции, у которых код валюты
        операции совпадает с currency_code.

    Example:
        >>> txs = [
        ...     {"id": 1, "operationAmount": {"currency": {"code": "USD"}}},
        ...     {"id": 2, "operationAmount": {"currency": {"code": "RUB"}}},
        ... ]
        >>> list(filter_by_currency(txs, "USD"))
        [{'id': 1, 'operationAmount': {'currency': {'code': 'USD'}}}]
    """
    return (
        transaction
        for transaction in transactions
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code
    )


def transaction_descriptions(transactions: list[dict[str, Any]]) -> Iterator[str]:
    """
    Возвращает описания транзакций по очереди.

    Args:
        transactions: Список словарей с данными о транзакциях. Каждый
            словарь должен содержать ключ "description".

    Yields:
        Значение ключа "description" очередной транзакции из списка.

    Example:
        >>> txs = [{"description": "Перевод организации"}, {"description": "Перевод со счета на счет"}]
        >>> descriptions = transaction_descriptions(txs)
        >>> next(descriptions)
        'Перевод организации'
        >>> next(descriptions)
        'Перевод со счета на счет'
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генерирует номера банковских карт в заданном диапазоне.

    Args:
        start: Начальное значение диапазона (включительно). Допустимый
            минимум — 1 (номер карты 0000 0000 0000 0001).
        stop: Конечное значение диапазона (включительно). Допустимый
            максимум — 9999999999999999 (номер карты 9999 9999 9999 9999).

    Yields:
        Номер карты в формате "XXXX XXXX XXXX XXXX", где X — цифра.

    Example:
        >>> list(card_number_generator(1, 2))
        ['0000 0000 0000 0001', '0000 0000 0000 0002']
    """
    for number in range(start, stop + 1):
        digits = f"{number:016d}"
        yield " ".join(digits[i : i + 4] for i in range(0, len(digits), 4))
