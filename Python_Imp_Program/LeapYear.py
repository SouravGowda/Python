year = int(input('enter the year''\n'))

if (year%400) & (year%4) == 0:
    print('Leap year')
#elif (year%4) == 0:
    #print('Leap year')
elif (year%100) == 0:
    print('Not a Leap year')
else:
    print('not a leap year')

print(year%400)
print(year%4)
