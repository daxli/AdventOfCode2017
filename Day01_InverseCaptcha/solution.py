#------------------------------------------------------------------------------#
#  Part 1 
def partOne(data):
    sum = 0
    for pos in xrange(0, len(data)):
        if(data[pos] == data[pos-1]):
            sum = sum + int(data[pos])
    
    return sum
#------------------------------------------------------------------------------#
#  Part 2
def partTwo(data):
    length = len(data)
    step = length / 2

    sum = 0
    for pos in xrange(0, length):
        if(data[pos] == data[pos-step]):
                sum = sum + int(data[pos])

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
        '1122': 3,
        '1111': 4,
        '1234': 0,
        '91212129': 9
    }
    tester(partOne, partOneSecarios)

    # Test Part2 solution
    partTwoSecarios = { 
        '1212': 6,
        '1221': 0,
        '123425': 4,
        '123123': 12,
        '12131415': 4
    }
    tester(partTwo, partTwoSecarios)

    
    #  Read input file
    with open('input.txt', 'r') as file:
        inputData = file.read()
    
    print 'Day01: Inverse Captcha'
    print '\tPart 1 solution: {0}'.format(partOne(inputData))
    print '\tPart 2 solution: {0}'.format(partTwo(inputData))
