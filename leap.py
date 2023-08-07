
def is_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    elif year % 3200 != 0:
        return True
    else:
        return False
leap = is_leap(int(input('輸入年份：')))
if leap == True:
    print('潤年')
else:
    print('平年')
    
print(leap)
