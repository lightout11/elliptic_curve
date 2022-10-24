import sympy

from arithematic_ec_fp import Point, add

def count_points_ec(a, b, p):
    singular = 4 * a ** 3 + 27 * b ** 2
    if singular == 0:
        return -1
    count = 1
    for x in range(p):
        for y in range(p):
            left = pow(y, 2, p)
            right = pow(pow(x, 3, p) + pow(a * x + b, 1, p), 1, p)
            if left == right:
                count += 1
    return count

def print_points(a, b, p):
    for x in range(p):
        for y in range(p):
            left = pow(y, 2, p)
            right = (pow(x, 3, p) + ((a % p) * x) % p + b % p) % p
            if left == right:
                print("(%d, %d)" % (x, y))

def generate_random_elliptic():
    count = 0
    while sympy.isprime(count) is False:
        a = sympy.randprime(10, 10000)
        b = sympy.randprime(10, 10000)
        p = sympy.randprime(10, 10000)
        print(a)
        print(b)
        print(p)
        print("y^2 = x^3 + " + str(a) + "x + " + str(b) + " (mod " + str(p) + ")")
        count = count_points_ec(a, b, p)
        print(count)
        print(sympy.isprime(count))
        if (sympy.isprime(count) is True):
            print_points(a, b, p)

def generate_elliptic(a, b, p):
    print("y^2 = x^3 + " + str(a) + "x + " + str(b) + " (mod " + str(p) + ")")
    count = count_points_ec(a, b, p)
    print(count)
    print(sympy.isprime(count))
    print_points(a, b, p)
    return count

def print_multiplication_table(point, a, b, p, count):
    pointtmp = point
    print("P = (%d, %d)" % (pointtmp.x, pointtmp.y))
    for i in range(2, count):
        pointtmp = add(pointtmp, point, a, b, p)
        print("%dP = (%d, %d)" % (i, pointtmp.x, pointtmp.y))

# generate_random_elliptic()
a = 4133
b = 1367
p = 397
count = generate_elliptic(a, b, p)
print("Enter point")
x = int(input("- Enter x: "))
y = int(input("- Enter y: "))

print(print_multiplication_table(Point(x, y), a, b, p, count))