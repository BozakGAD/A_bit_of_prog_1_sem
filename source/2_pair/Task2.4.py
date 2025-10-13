from random import choice
from string import ascii_uppercase, ascii_lowercase

def gener_password(list_of_needs):
    password = ""
    symbols = [i for i in ascii_lowercase if list_of_needs[0] == 1]
    symbols += [i for i in ascii_uppercase if list_of_needs[1] == 1]
    symbols += [i for i in "~!@#$%^&*()" if list_of_needs[2] == 1]
    symbols += [str(i) for i in range(0,10) if list_of_needs[3] == 1]
    for i in range(list_of_needs[4]):
        password += choice(symbols)
    print(password)


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
gener_password(list_of_needs)