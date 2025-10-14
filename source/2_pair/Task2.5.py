from roman import toRoman, fromRoman

def rom_arab_converter(list_arab_rom):
    """
        Преобразует числа из арабской и римской системы в противоположную для них систему.

        Функция принимает список строк, каждая из которых может быть
        либо арабским числом, либо римским числом.
        Если элемент состоит только из цифр, он преобразуется в римскую запись.
        В противном случае — в арабское число.

        Args:
            list_arab_rom (list): Список строк, содержащих арабские или римские числа.

        Returns:
            list: Список с преобразованными числами.
            - Римские числа преобразуются в этом списке в арабские и наоборот.
        Example:
            >>> 3658 34 XVII DCCXXIV
            ['MMMDCLVIII', 'XXXIV', 17, 724]
        """
    translated_list = []
    for i in list_arab_rom:
        if i.isdigit():
            translated_list.append(toRoman(int(i)))
        else:
            translated_list.append(fromRoman(i))
    return translated_list


print("""Введите числа, которые хотите перевести
из римской системы в арабскую и наоборот:""")
required_values = ((input()).split(" "))
print(rom_arab_converter(required_values))
