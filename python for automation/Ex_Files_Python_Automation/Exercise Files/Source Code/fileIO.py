fileName = '../inputFile.txt'
f = open(fileName,'r')
# output1= '../PassFile.txt'
passFile = open('PassFile1.txt','w')


count=1
for line in f:
    line_split=line.split()
    if line_split[2] == 'P':
        passFile.write(line)

f.close()
passFile.close()

'''
output1 = "PassFile.txt"
output2 = "FailFile.txt"
passFile = open(output1,'w')
failFile = open(output2, 'w')
for line in f:
    line_split = line.split()
    if line_split[2] == "P":
        passFile.write(line)
    else:
        failFile.write(line)
passFile.close()
failFile.close()
'''