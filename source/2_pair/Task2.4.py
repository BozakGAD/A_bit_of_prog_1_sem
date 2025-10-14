from random import choice
from string import ascii_uppercase, ascii_lowercase

def gener_password(list_of_needs):
    """
    Генерирует случайный пароль на основе заданных параметров.

    Args:
        list_of_needs (list): Список из 5 элементов, определяющих состав и длину пароля:
            [0] (int): 1 — использовать символы нижнего регистра (a-z), 0 — нет.
            [1] (int): 1 — использовать символы верхнего регистра (A-Z), 0 — нет.
            [2] (int): 1 — использовать специальные символы (~!@#$%^&*()), 0 — нет.
            [3] (int): 1 — использовать цифры (0-9), 0 — нет.
            [4] (int): длина генерируемого пароля.

    Returns:
        None: функция выводит сгенерированный пароль в консоль.

    Raises:
        ValueError: Если задана длина пароля меньше 1.

    Example:
        >>> gener_password([1, 1, 0, 1, 8])
        Ваш пароль: Ab4kdG0c
    """
    password = ""
    symbols = [i for i in ascii_lowercase if list_of_needs[0] == 1]
    symbols += [i for i in ascii_uppercase if list_of_needs[1] == 1]
    symbols += [i for i in "~!@#$%^&*()" if list_of_needs[2] == 1]
    symbols += [str(i) for i in range(0, 10) if list_of_needs[3] == 1]
    for i in range(list_of_needs[4]):
        password += choice(symbols)
    print(f"Ваш пароль: {password}")


print("""При вводе параметров генерации пароля:
1 - 'Да', любое другое значение - 'Нет'""")

print("""__________________________________
Наличие символов верхнего регистра:""")
list_of_needs = [int(input())]

print("""__________________________________
Наличие символов нижнего регистра:""")
list_of_needs.append(int(input()))

print("""__________________________________
Наличие специальных символов:""")
list_of_needs.append(int(input()))

print("""__________________________________
Наличие цифр:""")
list_of_needs.append(int(input()))

print("""__________________________________
Длина пароля:""")
list_of_needs.append(int(input()))
if list_of_needs[4] > 0:
    gener_password(list_of_needs)
else:
    raise ValueError("Длина пароля не может быть меньше 1.")

