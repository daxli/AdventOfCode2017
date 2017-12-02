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
#  Part 2
def partTwo(data):
    sum = 0
    for line in data.split('\n'):
        orderedLine = map(lambda x: int(x), line.split('\t'))
        for dividend in orderedLine:
            for divider in orderedLine:
                if (dividend != divider) and not (dividend % divider):
                    sum = sum + (dividend / divider)
                    break
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
        '7\t5\t3':    4,
        '2\t4\t6\t8': 6
    }
    tester(partOne, partOneSecarios)

    # Test Part1 solution
    partTwoSecarios = { 
        '5\t9\t2\t8': 4,
        '9\t4\t7\t3': 3,
        '3\t8\t6\t5': 2
    }
    tester(partTwo, partTwoSecarios)

    #  Read input file
    with open('input.txt', 'r') as file:
        inputData = file.read()
    
    print 'Day02: Corruption Checksum'
    print '\tPart 1 solution: {0}'.format(partOne(inputData))
    print '\tPart 2 solution: {0}'.format(partTwo(inputData))
