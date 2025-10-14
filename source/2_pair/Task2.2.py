from random import shuffle
def check_winners(scores, student_score):
    """
        Проверяет, входит ли результат студента в тройку лучших результатов.

        Функция сортирует список всех результатов по убыванию и определяет,
        находится ли результат студента среди трёх наибольших значений.
        В зависимости от результата выводится соответствующее сообщение.

        Args:
            scores (list): Список всех результатов участников.
            student_score (int): Результат студента для проверки.

        Returns:
            None: функция выводит данные о вхождении результата пользователя
            в тройку лидеров списка.

        Example:
            >>> check_winners(all_s, 999)
            Вы в тройке победителей!
        """
    sort_s = sorted(scores, reverse=True)
    if student_score in sort_s[0:3]:
        print("Вы в тройке победителей!")
    else:
        print("Вы не попали в тройку победителей.")

all_s = [int(i) for i in range(1, 1001)]
shuffle(all_s)  # Имитирую рандомизированность списка
stud_s = int(input())
check_winners(all_s, stud_s)
