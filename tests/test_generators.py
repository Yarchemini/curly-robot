"""Тесты для модуля src.generators."""

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


class TestFilterByCurrency:
    """Тесты функции filter_by_currency."""

    @pytest.mark.parametrize(
        "currency_code, expected_ids",
        [
            ("USD", [1, 2, 4]),
            ("RUB", [3, 5]),
        ],
    )
    def test_filters_by_given_currency(
        self, transactions_with_currency: list[dict], currency_code: str, expected_ids: list[int]
    ) -> None:
        """Функция возвращает только транзакции с указанной валютой."""
        result = list(filter_by_currency(transactions_with_currency, currency_code))
        assert [transaction["id"] for transaction in result] == expected_ids

    def test_returns_iterator(self, transactions_with_currency: list[dict]) -> None:
        """Функция возвращает именно итератор, а не список."""
        result = filter_by_currency(transactions_with_currency, "USD")
        assert hasattr(result, "__next__")

    def test_no_matching_currency_returns_empty(self, transactions_with_currency: list[dict]) -> None:
        """Если транзакций в указанной валюте нет, итератор не выдает элементов."""
        assert list(filter_by_currency(transactions_with_currency, "EUR")) == []

    def test_empty_transactions_list(self, empty_operations_list: list[dict]) -> None:
        """На пустом списке транзакций итератор не падает и не выдает элементов."""
        assert list(filter_by_currency(empty_operations_list, "USD")) == []


class TestTransactionDescriptions:
    """Тесты функции-генератора transaction_descriptions."""

    def test_returns_correct_descriptions(self, transactions_with_currency: list[dict]) -> None:
        """Генератор поочередно возвращает описания всех транзакций."""
        descriptions = list(transaction_descriptions(transactions_with_currency))
        assert descriptions == [
            "Перевод организации",
            "Перевод со счета на счет",
            "Перевод со счета на счет",
            "Перевод с карты на карту",
            "Перевод организации",
        ]

    @pytest.mark.parametrize("count", [0, 1, 3, 5])
    def test_various_input_sizes(self, transactions_with_currency: list[dict], count: int) -> None:
        """Генератор корректно работает с разным числом входных транзакций."""
        descriptions = list(transaction_descriptions(transactions_with_currency[:count]))
        assert len(descriptions) == count

    def test_empty_list(self, empty_operations_list: list[dict]) -> None:
        """На пустом списке транзакций генератор не выдает элементов."""
        assert list(transaction_descriptions(empty_operations_list)) == []

    def test_supports_next(self, transactions_with_currency: list[dict]) -> None:
        """Значения можно получать по одному через next()."""
        descriptions = transaction_descriptions(transactions_with_currency)
        assert next(descriptions) == "Перевод организации"
        assert next(descriptions) == "Перевод со счета на счет"


class TestCardNumberGenerator:
    """Тесты генератора card_number_generator."""

    def test_generates_expected_range(self) -> None:
        """Генератор выдает номера карт в заданном диапазоне по порядку."""
        assert list(card_number_generator(1, 5)) == [
            "0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003",
            "0000 0000 0000 0004",
            "0000 0000 0000 0005",
        ]

    @pytest.mark.parametrize(
        "number, expected",
        [
            (1, "0000 0000 0000 0001"),
            (42, "0000 0000 0000 0042"),
            (9999999999999999, "9999 9999 9999 9999"),  # верхняя граница диапазона
        ],
    )
    def test_formatting(self, number: int, expected: str) -> None:
        """Номер карты форматируется группами по 4 цифры, разделенными пробелом."""
        assert next(card_number_generator(number, number)) == expected

    def test_edge_of_range_start(self) -> None:
        """Генератор корректно обрабатывает нижнюю границу диапазона."""
        assert list(card_number_generator(1, 1)) == ["0000 0000 0000 0001"]

    def test_edge_of_range_end(self) -> None:
        """Генератор корректно обрабатывает верхнюю границу диапазона."""
        assert list(card_number_generator(9999999999999999, 9999999999999999)) == ["9999 9999 9999 9999"]

    def test_generation_stops_correctly(self) -> None:
        """После выдачи всех номеров генератор поднимает StopIteration."""
        generator = card_number_generator(1, 3)
        values = [next(generator) for _ in range(3)]
        assert len(values) == 3
        with pytest.raises(StopIteration):
            next(generator)
