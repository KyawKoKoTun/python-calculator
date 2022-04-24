def calculate(num1, num2, option):
    if option == 1:
        result = num1+num2
        print(result)
    elif option == 2:
        result = num1-num2
        print(result)
    elif option == 3:
        result = num1*num2
        print(result)
    elif option == 4:
        result = num1/num2
        print(result)
    else:
        print('Enter a vaild option')
    

while True:
    print('option 1: addition')
    print('option 2: subtraction')
    print('option 3: multiplication')
    print('option 4: division')
    while True:
        try:
            option = int(input('Input option: '))
            num1 = int(input('Enter first number: '))
            num2 = int(input('Enter second number: '))
            break
        except:
            print('Enter a number not a string\n')
    calculate(num1, num2, option)
    print('\n')

