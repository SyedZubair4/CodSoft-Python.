print('''Do you want will happen if MATHS doesn\'t exist?
Here are some basic mathematics operations which you can perform
1)Addition
2)Subtraction
3)Multiplication
4)Division
5)Remainder
6)Quit''')

num1=int(input('Enter first number:'))
num2=int(input('Enter second number:'))
choice=int(input('Enter the operation to be performed:'))

found=0
while True:

    if found==1:
        print('You have entered wrong choice, please select the operation to be performed:')
        found=0

    if choice == 1:
        print(num1 + num2)
        break
    elif choice == 2:
        print(num1 - num2)
        break
    elif choice == 3:
        print(num1 * num2)
        break
    elif choice == 4:
        while True:
            if num2==0:
                num2=int(input('Divisor cannot be zero, please enter valid input:'))
            else:
                break
        print(float(num1 / num2))
        break
    elif choice == 5:
        print(num1 % num2)
        break
    elif choice == 6:
        break

    else:
        found=1


