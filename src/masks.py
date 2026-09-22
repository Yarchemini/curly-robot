def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты в формате XXXX XX** **** XXXX."""
    if not card_number.isdigit() or len(card_number) != 16:
        return "Неверный формат карты"
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета, оставляя последние 4 цифры."""
    if not account_number.isdigit() or len(account_number) < 4:
        return "Неверный формат счета"
    return f"**{account_number[-4:]}"