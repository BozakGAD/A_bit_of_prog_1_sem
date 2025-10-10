from random import choice,shuffle
from string import ascii_uppercase
st = []
nu = []
sy = []
for i in ascii_uppercase:
    st += i
for i in range(0,10):
    nu += str(i)
for i in "!@#$%^&*()":
    sy += str(i)
ran_code = [choice(st)]+[choice(st)]+[choice(st)]+[choice(nu)]+[choice(nu)]+[choice(nu)]+[choice(sy)]+[choice(sy)]
shuffle(ran_code)
s = "".join(ran_code)
print(s)
