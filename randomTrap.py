import sys
import random
import math
import functools
import bisect


random.seed(1)

class ZipfGenerator:

    def __init__(self, n, alpha):
        # Calculate Zeta values from 1 to n:
        tmp = [1. / (math.pow(float(i), alpha)) for i in range(1, n + 1)]
        zeta = functools.reduce(lambda sums, x: sums + [sums[-1] + x], tmp, [0])

        # Store the translation map:
        self.distMap = [x / zeta[-1] for x in zeta]

    def next(self):
        # Take a uniform 0-1 pseudo-random value:
        u = random.random()

        # Translate the Zipf variable:
        return bisect.bisect(self.distMap, u) - 1


zipf = ZipfGenerator(10000, 1)


def randomTrap():
    # Point is the geometric center of trapezoid

    point = random.uniform(-sys.maxint, sys.maxint)

    # Width of trapezoid (using zipf distribution)

    width = zipf.next() * random.uniform(0, sys.maxint / 1000)

    # Adapt tilt if we want an angle more opened or not

    tilt = random.uniform(0.25, 0.75)

    # Creating trapezoid a,b,c,d

    a = point - width / 2

    d = point + width / 2

    if (d < a):
        aux = d
        d = a
        a = aux

    b = point - tilt * (width / 2)

    c = point + tilt * (width / 2)

    if (c < b):
        aux = c
        c = b
        b = aux

    return [a, b, c, d]


def randDoc(id):
    x = randomTrap()
    post = {"_id": id, "x": x}
    post["x"]

    return post


for i in xrange(1000):
    print(randDoc(i))

