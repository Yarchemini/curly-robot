def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номера банковской карты."""
    if not card_number.isdigit() or len(card_number) != 16:
        return "Неверный формат карты"

    # Формат маски: XXXX XX** **** XXXX
    part1 = card_number[:4]
    part2 = card_number[4:6]
    part4 = card_number[12:]

    return f"{part1} {part2}** **** {part4}"


def get_mask_account(account_number: str) -> str:
    """Функция, для маскировки номера банковского счета."""
    if not account_number.isdigit() or len(account_number) < 4:
        return "Неверный формат счета"

    # Маскируем так чтобы были видны только последние 4 цифры, перед ними две звездочки
    return f"**{account_number[-4:]}"

def mask_account_card(info: str) -> str:
    """Принимает строку с названием и номером карты/счета и маскирует её."""
    if not info:
        return ""

    # Разделяем входную строку на слова
    parts = info.split()
    number = parts[-1]  # Последнее слово — это сам номер
    name = " ".join(parts[:-1])  # Всё остальное — название (например, Visa Platinum)

    if "Счет" in name:
        # Используем твою вторую функцию для счетов
        return f"{name} {get_mask_account(number)}"
    else:
        # Используем твою первую функцию для карт
        return f"{name} {get_mask_card_number(number)}"


def get_date(date_str: str) -> str:
    """Конвертирует строку даты из формата ISO в формат ДД.ММ.ГГГГ."""
    if not date_str or len(date_str) < 10:
        return ""
    clean_date = date_str[:10]  # Берем только "2024-03-11"
    year, month, day = clean_date.split("-")
    return f"{day}.{month}.{year}"


if __name__ == "__main__":
    # Проверяем карту Visa
    print(mask_account_card("Visa Platinum 7000792289606361"))

    # Проверяем карту Maestro
    print(mask_account_card("Maestro 7000792289606361"))

    # Проверяем Счет
    print(mask_account_card("Счет 73654108430135874305"))

    # Проверяем дату
    print(get_date("2024-03-11T02:26:18.671407"))
