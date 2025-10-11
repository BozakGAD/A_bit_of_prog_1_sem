from itertools import count

def print_pack_report(product):
    dividers = []
    for i in "35":
        if product%int(i) == 0:
            dividers.append(i)
    if len(dividers) == 2:
        print(f"{product} - Расфасуем по 3 или по 5")
    elif len(dividers) == 1:
        print(f"{product} - Расфасуем по {dividers[0]}")
    else:
        print(f"{product} - Не заказываем!")
prod = 0
while prod<1:
    prod = int(input())
print_pack_report(prod)
