from random import choice
from random import shuffle
from string import ascii_uppercase

st = [i for i in ascii_uppercase]
nu = [str(i) for i in range(1,10)]
sy = [i for i in "!@#$%^&*()"]
ran_code = ([choice(st)]+[choice(st)]+[choice(st)]
            +[choice(nu)]+[choice(nu)]+[choice(nu)]
            +[choice(sy)]+[choice(sy)])
shuffle(ran_code)
s = "".join(ran_code)
print(s)
