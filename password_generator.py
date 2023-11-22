import random as rdm

def generator(n):
    words=[]
    global available
    for i in range(n):
        words.append(rdm.sample(available, n)[0])
    return words


available = [chr(i) for i in range(33,123)]
start=0
found=0
while True:
    if start==0:
        start=1
        length = int(input('Enter the length of password you want to generate:'))
        password = generator(length)

        print('We have generated a this password specially for you-->  ' + str(password) + '  <--')
        option = input('Do you want to generate one more(y/n):')
        if option == 'y':
            found = 1
        elif option == 'n':
            break
        else:
            continue


    if found==1:
        length = int(input('Sure, Enter the length of password you want to generate:'))
        password = generator(length)

        print('We have generated a this password specially for you-->  ' + str(password) + '  <--')
        option = input('Do you want to generate one more(y/n):')
        if option == 'y':
            found = 1
        elif option=='n':
            break

    else:
        break






