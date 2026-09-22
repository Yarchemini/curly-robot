"""Тесты для модуля src.widget."""

import pytest

from src.widget import get_date, mask_account_card


class TestMaskAccountCard:
    """Тесты функции mask_account_card."""

    @pytest.mark.parametrize(
        "info, expected",
        [
            ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
            ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
            ("MasterCard 1234567812345678", "MasterCard 1234 56** **** 5678"),
        ],
    )
    def test_card_type_masking(self, info: str, expected: str) -> None:
        """Функция распознаёт карту (по отсутствию слова 'Счет') и маскирует её как карту."""
        assert mask_account_card(info) == expected

    @pytest.mark.parametrize(
        "info, expected",
        [
            ("Счет 73654108430135874305", "Счет **4305"),
            ("Счет 1234", "Счет **1234"),
        ],
    )
    def test_account_type_masking(self, info: str, expected: str) -> None:
        """Функция распознаёт счет (по слову 'Счет') и маскирует его как счет."""
        assert mask_account_card(info) == expected

    def test_empty_string_returns_empty(self) -> None:
        """При пустой входной строке функция возвращает пустую строку."""
        assert mask_account_card("") == ""

    def test_malformed_input_single_token(self) -> None:
        """Если во входной строке нет названия, функция все равно не падает с ошибкой."""
        result = mask_account_card("7000792289606361")
        assert result.endswith("7000 79** **** 6361")


class TestGetDate:
    """Тесты функции get_date."""

    @pytest.mark.parametrize(
        "date_str, expected",
        [
            ("2024-03-11T02:26:18.671407", "11.03.2024"),
            ("2019-07-03T18:35:29.512364", "03.07.2019"),
            ("2020-01-01", "01.01.2020"),  # дата без времени — граничный случай
        ],
    )
    def test_valid_date_conversion(self, date_str: str, expected: str) -> None:
        """Функция корректно конвертирует дату из ISO-формата в ДД.ММ.ГГГГ."""
        assert get_date(date_str) == expected

    def test_missing_date(self) -> None:
        """Пустая строка (отсутствие даты) обрабатывается без ошибок."""
        assert get_date("") == ""

    @pytest.mark.parametrize(
        "invalid_date_str",
        [
            "не дата",
            "2024-13-45",  # некорректные месяц и день
            "11.03.2024",  # не ISO-формат
        ],
    )
    def test_invalid_date_raises_error(self, invalid_date_str: str) -> None:
        """Некорректная строка с датой приводит к исключению ValueError."""
        with pytest.raises(ValueError):
            get_date(invalid_date_str)
