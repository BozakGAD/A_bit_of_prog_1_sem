s = "fffffff$$$$xxxx4sjfkbdhfxcjzui"
top=[]
used = []
for i in s:
    if i not in used:
        quant = s.count(i)
        top.append([quant,i])
        top.sort(reverse=True)
        used += i
print(top)
print(top[0],top[1],top[2])
