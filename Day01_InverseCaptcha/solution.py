with open('input.txt', 'r') as file:
    inputData = file.read()

sum = 0
for pos in xrange(0, len(inputData)):
    if(inputData[pos] == inputData[pos-1]):
            sum = sum + int(inputData[pos])

print sum
