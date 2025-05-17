import random
file = open('no_math_911.txt', 'a')
for i in range(100000):
    a = random.randint(11, 999)
    b = random.randint(11, 999)
    c = random.randint(1, 26)
    file.write(f'\n{a} + {b} = {a + b + c}?')
file.close()