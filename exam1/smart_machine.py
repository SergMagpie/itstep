while True:
    num = input('Enter a number or exit for exit ')
    if num == 'exit':
        break
    try:
        x = float(num)
        if x < 100:
            print(x - 10)
        else:
            print(x - 20)
    except:
        print("Wrong Input")
        