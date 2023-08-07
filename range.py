import random

for i in range(3):
    print(i)
for i in range(100):
    r = random.randint(1, 1000)
    print('這是第', i + 1, '次產生的隨機數', r)

for i in range(1, 10, 2):
    print(i)
for i in range(10, 1, -2):
    print(i)
