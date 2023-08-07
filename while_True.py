while True:
    mode = input('輸入遊戲模式：')
    mode_upper = mode.upper()
    if mode_upper == 'Q':
        break
    elif mode_upper == '1':
        print('啟動模式一')
    elif mode_upper == '2':
        print('啟動模式二')
    else:
        print('只能輸入 1/2/q')