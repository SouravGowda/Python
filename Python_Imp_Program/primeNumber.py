#2 3 5 7 11 13 17 19 23 29

num = int(input('enter the number: '))

for i in range(2,num):
    if num % i == 0:
        print(num,'is not a prime number')
        break
    else:
        print(num,'is a prime number')
        break
