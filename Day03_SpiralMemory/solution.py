import math

class Point(object):
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def manhattandDistance(self, other):
        dx = self.X - other.X
        dy = self.Y - other.Y
        return abs(dx) + abs(dy)

def calculateOrigo(size):
    if size == 1:
        return Point(1, 1)

    y = int(math.ceil(size / 2.0))
    if size % 2:
        return Point(y, y)
    else:
        return Point(y + 1, y)

#------------------------------------------------------------------------------#
def partOne(number):
    size = int(math.ceil(math.sqrt(number)))
    origo = calculateOrigo(size)

    referenceX = (number % size) if (number % size) else size
    reference = Point(referenceX, size)

    return origo.manhattandDistance(reference)

#------------------------------------------------------------------------------#
def partTwo(number):
    pass
    # https://oeis.org/A141481

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
        1: 0,
        12: 3,
        23: 2
    }
    tester(partOne, partOneSecarios)

    print 'Day03: Spiral Memory'
    print '\tPart 1 solution: {0}'.format(partOne(361527))
    #print '\tPart 2 solution: {0}'.format(partTwo(inputData))
    
