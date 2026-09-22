"""Тесты для модуля src.processing."""

import pytest

from src.processing import filter_by_state, sort_by_date


class TestFilterByState:
    def test_default_state_executed(self, operations_list: list[dict]) -> None:
        result = filter_by_state(operations_list)
        assert [op["id"] for op in result] == [1, 3]
        assert all(op["state"] == "EXECUTED" for op in result)

    @pytest.mark.parametrize(
        "state, expected_ids",
        [
            ("EXECUTED", [1, 3]),
            ("CANCELED", [2]),
            ("PENDING", [4]),
            ("UNKNOWN_STATE", []),
        ],
    )
    def test_filter_by_various_states(
        self, operations_list: list[dict], state: str, expected_ids: list[int]
    ) -> None:
        result = filter_by_state(operations_list, state)
        assert [op["id"] for op in result] == expected_ids

    def test_no_matching_state_returns_empty_list(self, operations_list: list[dict]) -> None:
        result = filter_by_state(operations_list, "REFUNDED")
        assert result == []

    def test_empty_operations_list(self, empty_operations_list: list[dict]) -> None:
        result = filter_by_state(empty_operations_list)
        assert result == []

    def test_original_list_not_mutated(self, operations_list: list[dict]) -> None:
        original_length = len(operations_list)
        filter_by_state(operations_list)
        assert len(operations_list) == original_length


class TestSortByDate:
    def test_sort_descending_by_default(self, operations_list: list[dict]) -> None:
        result = sort_by_date(operations_list)
        dates = [op["date"] for op in result]
        assert dates == sorted(dates, reverse=True)

    def test_sort_ascending(self, operations_list: list[dict]) -> None:
        result = sort_by_date(operations_list, reverse=False)
        dates = [op["date"] for op in result]
        assert dates == sorted(dates)

    def test_sort_with_identical_dates_preserves_order(
        self, operations_same_date: list[dict]
    ) -> None:
        result = sort_by_date(operations_same_date)
        assert [op["id"] for op in result] == [1, 2, 3]

    def test_original_list_not_mutated(self, operations_list: list[dict]) -> None:
        original_order = [op["id"] for op in operations_list]
        sort_by_date(operations_list)
        assert [op["id"] for op in operations_list] == original_order

    def test_empty_operations_list(self, empty_operations_list: list[dict]) -> None:
        result = sort_by_date(empty_operations_list)
        assert result == []

    def test_missing_date_key_raises_key_error(self) -> None:
        operations = [{"id": 1, "state": "EXECUTED"}]
        with pytest.raises(KeyError):
            sort_by_date(operations)