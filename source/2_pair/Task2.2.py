from random import shuffle
def check_winners(scores,student_score):
    sort_s = sorted(scores, reverse=True)
    if student_score in sort_s[0:3]:
        print("Вы в тройке победителей")
    else:
        print("Вы не попали в тройку победителей")

all_s = [int(i) for i in range(1,1001)]
shuffle(all_s) # Имитирую рандомизированность списка
stud_s = int(input())
check_winners(all_s,stud_s)
