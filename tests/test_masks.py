"""Тесты для модуля src.masks."""

import pytest

from src.masks import get_mask_account, get_mask_card_number


class TestGetMaskCardNumber:
    """Тесты функции get_mask_card_number."""

    def test_valid_card_number(self, valid_card_number: str) -> None:
        """Корректный 16-значный номер карты маскируется в ожидаемом формате."""
        assert get_mask_card_number(valid_card_number) == "7000 79** **** 6361"

    @pytest.mark.parametrize(
        "card_number, expected",
        [
            ("7000792289606361", "7000 79** **** 6361"),
            ("1234567812345678", "1234 56** **** 5678"),
            ("0000000000000000", "0000 00** **** 0000"),
        ],
    )
    def test_various_valid_card_numbers(self, card_number: str, expected: str) -> None:
        """Функция корректно маскирует разные валидные номера карт."""
        assert get_mask_card_number(card_number) == expected

    @pytest.mark.parametrize(
        "card_number",
        [
            "123456789012345",  # 15 цифр — короче ожидаемой длины
            "12345678901234567",  # 17 цифр — длиннее ожидаемой длины
            "",  # пустая строка
            "700079228960636a",  # содержит буквы
            "7000 7922 8960 6361",  # содержит пробелы
            "7000-7922-8960-6361",  # содержит дефисы
        ],
    )
    def test_invalid_card_number_formats(self, card_number: str) -> None:
        """При некорректном формате номера карты возвращается сообщение об ошибке."""
        assert get_mask_card_number(card_number) == "Неверный формат карты"

    def test_missing_card_number(self) -> None:
        """Пустая строка (отсутствие номера карты) обрабатывается корректно."""
        assert get_mask_card_number("") == "Неверный формат карты"


class TestGetMaskAccount:
    """Тесты функции get_mask_account."""

    def test_valid_account_number(self, valid_account_number: str) -> None:
        """Корректный номер счета маскируется — видны только последние 4 цифры."""
        assert get_mask_account(valid_account_number) == "**4305"

    @pytest.mark.parametrize(
        "account_number, expected",
        [
            ("73654108430135874305", "**4305"),
            ("1234", "**1234"),  # длина ровно 4 — граничный случай
            ("123456", "**3456"),
        ],
    )
    def test_various_valid_account_numbers(self, account_number: str, expected: str) -> None:
        """Функция корректно маскирует счета разной длины (от 4 цифр и больше)."""
        assert get_mask_account(account_number) == expected

    @pytest.mark.parametrize(
        "account_number",
        [
            "123",  # короче ожидаемой минимальной длины (4)
            "1",
            "",  # пустая строка
            "12a4",  # содержит буквы
            "1234 5678",  # содержит пробел
        ],
    )
    def test_invalid_account_formats(self, account_number: str) -> None:
        """При некорректном формате счета (короче 4 цифр или не число) возвращается ошибка."""
        assert get_mask_account(account_number) == "Неверный формат счета"

    def test_missing_account_number(self) -> None:
        """Пустая строка (отсутствие номера счета) обрабатывается корректно."""
        assert get_mask_account("") == "Неверный формат счета"
