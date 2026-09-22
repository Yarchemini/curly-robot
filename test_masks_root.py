import pytest
from masks import get_mask_card_number, get_mask_account

import sys
import os
# Сами жестко добавляем папку, где лежат masks.py и generators.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from masks import get_mask_card_number, get_mask_account

def test_get_mask_card_number_valid():
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"

def test_get_mask_card_number_not_digit():
    assert get_mask_card_number("123456789012345a") == "Неверный формат карты"

def test_get_mask_card_number_wrong_length():
    assert get_mask_card_number("1234567890") == "Неверный формат карты"

def test_get_mask_account_valid():
    assert get_mask_account("73654108430135874305") == "**4305"

def test_get_mask_account_short():
    assert get_mask_account("123") == "Неверный формат счета"

def test_get_mask_account_not_digit():
    assert get_mask_account("123a") == "Неверный формат счета"
