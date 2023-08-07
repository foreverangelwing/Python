import os

def read_file(filename):
    products = []
    if os.path.isfile(filename):
        print('找到檔案')
        with open(filename, 'r', encoding='UTF-16') as f:
            for line in f:
                if '商品,價格' in line:
                    continue
                name, price = line.strip().split(',')
                products.append([name, price])
        print(products)
    else:
        print('沒有檔案')
    return products

def user_input(products):
    while True:
        name = input('數入商品名稱：')
        if name == 'q':
            break
        price = input('數入商品價格：')
        price = int(price)
        products.append([name, price])
    print(products)
    return products

def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])

def write_file(filename, products):
    with open(filename, 'w', encoding='UTF-16') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')

products = read_file('products.csv')
products = user_input(products)
print_products(products)
write_file('products.csv', products)
 