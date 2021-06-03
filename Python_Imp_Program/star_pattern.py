num = 5 #number of stars
m=(2*num)-2

for i in range(0,num):
    for j in range(0,m):
        print(end=' ') #half pyramid left side without space
    m-=1
    for j in range(0,i+1):
        print('*',end="  ") #half pyramid right side without space
    print(' ')