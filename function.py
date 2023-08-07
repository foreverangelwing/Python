def wash(dry=False, water=8):
    print('加水', water, '滿')
    print('洗衣')
    print('脫水')
    if dry:
        print('烘衣')
wash(dry=True, water=10)
wash(True)
wash(False)

def say_hi():
    print('hi')
say_hi()

def add(x, y):
    return x + y

result = (add(3, 4))

def average(numbers):
    avg = sum(numbers) / len(numbers)
    return avg
a = average([1, 2, 3])
print(a)

def hello(x, y=1):
    print(x, y)

hello(3, 4)