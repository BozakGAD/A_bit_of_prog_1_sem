import datetime
from decimal import Decimal
from types import NoneType

def add(items, title, amount, expiration_date=None):
    """
    Добавляет продукт в словарь холодильника.

    Если продукт с указанным названием уже существует, то новая запись (с количеством 
    и сроком годности) добавляется к списку существующих записей. Если продукт отсутствует, 
    создаётся новый ключ в словаре. Дата срока годности может быть как указана, так и отсутствовать.

    Args:
        items (dict): Словарь, где ключ — это название продукта,
        а значение — список словарей с ключами "amount" (Decimal) и "expiration_date".
        
        title (str): Название добавляемого продукта.
        
        amount (str или Decimal): Количество добавляемого продукта. Преобразуется в Decimal.
        
        expiration_date (str, None): Дата истечения срока годности в формате "YYYY-MM-DD".
        Если не указана, значение будет None.

    Returns:
        dict: Обновлённый словарь продуктов.

    Example:
        >>> items = {}
        >>> add(items, "Молоко", "1.5", "2025-10-25")
        {'Молоко': [{'amount': Decimal('1.5'), 'expiration_date': datetime.date(2025, 10, 25)}]}

        >>> add(items, "Хлеб", "2")
        {'Молоко': [{'amount': Decimal('1.5'), 'expiration_date': datetime.date(2025, 10, 25)}],
         'Хлеб': [{'amount': Decimal('2'), 'expiration_date': None}]}
    """
    if type(expiration_date) == NoneType and title in items:
        items[title] += [{"amount": Decimal(amount), "expiration_date": None}]
    
    elif type(expiration_date) == NoneType and title not in items:
        items[title] = [{"amount": Decimal(amount), "expiration_date": None}]
    
    elif title in items:
        listed_exp_date = expiration_date.split("-")
        items[title] += [{"amount": Decimal(amount), "expiration_date": datetime.date(int(listed_exp_date[0]), int(listed_exp_date[1]), int(listed_exp_date[2]))}]
    
    else:
        listed_exp_date = expiration_date.split("-")
        items[title] = [{"amount": Decimal(amount), "expiration_date": datetime.date(int(listed_exp_date[0]), int(listed_exp_date[1]), int(listed_exp_date[2]))}]
    return items


def add_by_note(items, note):
    """
    Добавляет продукт в словарь холодильника на основе введённой строки.

    Функция разбирает строку `note`, определяя из неё название продукта, количество
    и при необходимости срок годности. Ожидается, что заметка содержит название 
    продукта и одно или два числовых значения:
    - если указано одно число — это количество;
    - если указано два числа — предпоследнее число — количество, последнее — дата 
      срока годности в формате "YYYY-MM-DD".

    Внутри используется функция `add()` для непосредственного добавления данных 
    в словарь `items`.

    Args:
        items (dict): Словарь с продуктами, где ключ — название (str),
        а значение — список словарей с ключами:
        - "amount" (Decimal): количество,
        - "expiration_date" (datetime.date или None).
        
        note (str): Текстовая строка с описанием продукта, например:
        "Молоко 1.5 2025-10-25" или "Хлеб 2".

    Returns:
        dict: Обновлённый словарь продуктов после добавления.

    Example:
        >>> items = {}
        >>> add_by_note(items, "Молоко 1.5 2025-10-25")
        {'Молоко': [{'amount': Decimal('1.5'), 'expiration_date': datetime.date(2025, 10, 25)}]}

        >>> add_by_note(items, "Хлеб 2")
        {'Молоко': [{'amount': Decimal('1.5'), 'expiration_date': datetime.date(2025, 10, 25)}],
         'Хлеб': [{'amount': Decimal('2'), 'expiration_date': None}]}
    """
    splitted_note = note.split()
    for i in splitted_note:
        try:
            float(i)
            break
        except ValueError:
            pass
    try:
        float(splitted_note[-1])
        amount = splitted_note[-1]
        del splitted_note[-1]
        connect_title = " ".join(splitted_note)
        return add(items, connect_title, amount)
    except ValueError:
        pass
    amount = splitted_note[-2]
    date = splitted_note[-1]
    del splitted_note[-1]
    del splitted_note[-1]
    connect_title = " ".join(splitted_note)
    return add(items, connect_title, amount, date)


def find(items, needle):
    """
    Ищет продукты в словаре холодильника по названию.

    Функция выполняет поиск всех продуктов, название которых содержит подстроку `needle`,
    без учёта регистра букв. Возвращает список найденных совпадений (ключей словаря `items`).

    Args:
        items (dict): Словарь с продуктами, где ключ — это название продукта (str),
        а значение — список словарей с данными о количестве и сроке годности.
        
        needle (str): Подстрока или фрагмент названия продукта для поиска.

    Returns:
        list[str]: Список названий продуктов, в которых встречается `needle`.

    Example:
        >>> items = {
        ...     "Молоко": [{"amount": Decimal("1.0"), "expiration_date": None}],
        ...     "Шоколад": [{"amount": Decimal("2.0"), "expiration_date": None}],
        ...     "Молочный коктейль": [{"amount": Decimal("0.5"), "expiration_date": None}]
        ... }
        >>> find(items, "мол")
        ['Молоко', 'Молочный коктейль']
    """
    list_of_findings = []
    for i in items:
        if needle.lower() in i.lower():
            list_of_findings.append(i)
    return list_of_findings


def amount(items, needle):
    """
    Подсчитывает общее количество продуктов, наименование которых совпадает с искомой строкой.

    Функция ищет все продукты в словаре `items`, чьи названия содержат подстроку `needle`
    (поиск нечувствителен к регистру), и суммирует значения "amount" для всех найденных записей.

    Args:
        items (dict): Словарь с продуктами, где ключ — это название продукта (str),
        а значение — список словарей с данными о количестве и сроке годности.
        
        needle (str): Подстрока, по которой выполняется поиск продуктов в названиях.

    Returns:
        Decimal: Суммарное количество всех найденных продуктов.

    Example:
        >>> items = {
        ...     "Молоко": [
        ...         {"amount": Decimal("0.5"), "expiration_date": datetime.date(2025, 10, 25)}
        ...     ],
        ...     "Шоколад": [
        ...         {"amount": Decimal("2.0"), "expiration_date": None}
        ...     ]
        ... }
        >>> amount(items, "мол")
        Decimal('0.5')

        >>> amount(items, "шок")
        Decimal('2.0')
    """
    sum_of_amounts = 0
    for i in items:
        if needle.lower() in i.lower():
            for a in items[i]:
                sum_of_amounts += a["amount"]

    return Decimal(sum_of_amounts)


goods = {'Вода': [{'amount': Decimal('5'), 'expiration_date': datetime.date(2025, 10, 16)}]}
print(add(goods, "Вода", 10, "2025-10-18"))
print(add(goods, "Вода", 20))
print(add_by_note(goods, 'Макароны 1.5'))
print(find(goods, "од"))
print(amount(goods, "од"))
