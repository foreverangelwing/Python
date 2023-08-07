import random

start = int(input('輸入開始值：'))
end = int(input('輸入結束值：'))
r = random.randint(start, end)
count = 0
while True:
    count = count +1
    mun = int(input('猜猜數字：'))    
    if mun == r:
        print('猜中了！')
        print('你猜得第', count, '次')  
        print(r,)
        break
    elif mun > r:
        print('比答案大')
    elif mun < r:
        print('比答案小')
    else:
        print('只能輸入數字')
    print('你猜得第', count, '次')  
