#------------------------------------------------------------------------------#
#  Part 1 
def partOne(data):
    sum = 0
    for line in data.split('\n'):
        orderedLine = sorted(map(lambda x: int(x), line.split('\t')))
        difference = abs(orderedLine[0] - orderedLine[-1])
        sum = sum + difference
    return sum

#------------------------------------------------------------------------------#
def tester(function, scenarios):
    errorMessage = ''
    for case, expected in scenarios.iteritems():
        try:
            actual = function(case)
            assert actual == expected
        except AssertionError:
            pattern = 'Actual: {0}\tExpected:{1}\tCase: {2}'
            errorDetails = pattern.format(actual, expected, case)
            errorMessage = '\n'.join([errorMessage, errorDetails])
    
    if errorMessage:
        print 'TEST FAIL: {0}'.format(function.__name__)
        print errorMessage
        print 'Exit program....'
        exit(1)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
if __name__ == "__main__":
    # Test Part1 solution
    partOneSecarios = { 
        '5\t1\t9\t5': 8,
        '7\t5\t3': 4,
        '2\t4\t6\t8': 6
    }
    tester(partOne, partOneSecarios)

    #  Read input file
    with open('input.txt', 'r') as file:
        inputData = file.read()
    
    print 'Day02: Corruption Checksum'
    print '\tPart 1 solution: {0}'.format(partOne(inputData))
