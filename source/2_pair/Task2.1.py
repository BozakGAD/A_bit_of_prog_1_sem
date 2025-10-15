from string import ascii_lowercase, ascii_uppercase

ENG_ALPHA_LOW = [i for i in ascii_lowercase]
ENG_ALPHA_UPPER = [i for i in ascii_uppercase]
RUS_ALPHA_LOW = [chr(i) for i in range(ord('а'), ord('я') + 1)]
RUS_ALPHA_UPPER = [chr(i) for i in range(ord('А'), ord('Я') + 1)]

def which_alpha(char):
    """
    Определяет, к какому алфавиту (русскому или английскому) и регистру
    принадлежит заданный символ.

    Args:
        char (str): Один символ, который нужно проверить.

    Returns:
        list: Возвращает список символов соответствующего алфавита и регистра,
        - если `char` найден.
    None: Если символ не принадлежит ни одному из алфавитов, возвращает None.

    Example:
        >>> which_alpha("U")
        ENG_ALPHA_UPPER
    """
    if char in ENG_ALPHA_LOW:
        return ENG_ALPHA_LOW
    if char in ENG_ALPHA_UPPER:
        return ENG_ALPHA_UPPER
    if char in RUS_ALPHA_LOW:
        return RUS_ALPHA_LOW
    if char in RUS_ALPHA_UPPER:
        return RUS_ALPHA_UPPER
    else:
        return None


def cypher(text_to_cypher, shift_num):
    """
    Шифрует текст с помощью символьного сдвига (шифр Цезаря)
    для символов русского и английского алфавитов.

    Для каждого символа строки определяется соответствующий алфавит
    (русский или английский, верхний или нижний регистр) и выполняется
    циклический сдвиг на заданное количество позиций.

    Args:
        text_to_cypher (str): Исходный текст, который нужно зашифровать.
        shift_num (int): Величина сдвига по алфавиту. Может быть положительной или отрицательной.

    Returns:
    str: Зашифрованный текст, где каждая буква сдвинута на shift_num позиций.
    - Символы, не принадлежащие алфавиту, остаются без изменений.

    Example:
        >>> cypher("Самая лучшая шифровка в мире", 5)
        "Цесед ршьэед энщхузпе з снхк"
    """
    cyphered_text = ""
    for char in text_to_cypher:
        alpha = which_alpha(char)
        if alpha is None:
            cyphered_text += char
        else:
            cyphered_text += alpha[(alpha.index(char) + shift_num) % len(alpha)]
    return cyphered_text


def decypher(text_to_decypher, shift_num):
    """
        Дешифрует текст, зашифрованный методом символьного сдвига (шифр Цезаря)
        для русского и английского алфавитов.

        Для каждого символа строки определяется соответствующий алфавит
        (русский или английский, верхний или нижний регистр) и выполняется
        обратный циклический сдвиг на заданное количество позиций.

        Args:
        text_to_decypher (str): Текст, который нужно расшифровать.
        shift_num (int): Величина сдвига по алфавиту, использованная при шифровании.
        - Может быть положительной или отрицательной.

        Returns:
        str: Расшифрованный текст, в котором каждая буква сдвинута обратно
        - на указанное число позиций. Символы, не принадлежащие алфавиту,
        - остаются без изменений.

        Example:
            >>> decypher("Цесед ршьэед энщхузпе з снхк", 5)
            "Самая лучшая шифровка в мире"
        """
    decyphered_text = ""
    for char in text_to_decypher:
        alpha = which_alpha(char)
        if alpha is None:
            decyphered_text += char
        else:
            decyphered_text += alpha[(alpha.index(char) - shift_num) % len(alpha)]
    return decyphered_text


print("Шифр Цезаря.")
print("Выберите значение сдвига шифра: ")
shift = int(input())

print("Введите строку для шифровки/дешифровки: ")
text = str(input())

print("Шифровка (1) / Дешифровка (0)")
if input() == "0":
    print(f"Расшифровка: {decypher(text, shift)}")
else:
    print(f"Шифр: {cypher(text, shift)}")
