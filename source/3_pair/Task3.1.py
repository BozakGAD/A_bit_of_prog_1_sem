import datetime
from decimal import Decimal
from types import NoneType

def add(items, title, amount, expiration_date=None):
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
    list_of_findings = []
    for i in items:
        if needle.lower() in i.lower():
            list_of_findings.append(i)
    return list_of_findings


def amount(items, needle):
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
