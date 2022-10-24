class Point:
    x = -1
    y = -1

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

def add(pointp, pointq, a, b, p):
    lamb = 0
    if pointp != pointq:
        tmpx = pointq.x - pointp.x
        tmpy = pointq.y - pointp.y
        if tmpx < 0:
            tmpx = -tmpx
            tmpy = -tmpy
        lamb = pow(pow(tmpy, 1, p) * pow(tmpx, -1, p), 1, p)
        # print("lamb = %d" % (lamb))
    if pointp == pointq:
        numerator = 3 * pointp.x ** 2 + a
        denominator = 2 * pointp.y
        # if (denominator < 0):
        #     numerator = -numerator
        #     denominator = -denominator
        lamb = pow(pow(numerator, 1, p) * pow(denominator, -1, p), 1, p)
        # print("lamb = %d" % (lamb))
    x = pow(lamb ** 2 - pointp.x - pointq.x, 1, p)
    y = pow(lamb * (pointp.x - x) - pointp.y, 1, p)
    # print("(x, y) = (%d, %d)" % (x, y))
    return Point(x, y)

def multiply(k, point, a, b, p):
    pointtmp = point
    for i in range(k - 1):
        pointtmp = add(pointtmp, point, a, b, p)
    return Point(pointtmp.x, pointtmp.y)
