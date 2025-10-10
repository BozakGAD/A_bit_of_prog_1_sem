num = int(input())
l = list(range(2,num+1))
for check_num in l:
    for i in range(2, num//check_num+1):
        if check_num*i in l:
            l.remove(check_num*i)
print(l)
