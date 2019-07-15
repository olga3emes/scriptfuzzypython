from __future__ import print_function
import sys
import random
import functools
import bisect
import math


import matplotlib.pyplot as plt


class ZipfGenerator:

    def __init__(self, n, alpha):
        # Calculate Zeta values from 1 to n:
        tmp = [1. / (math.pow(float(i), alpha)) for i in range(1, n+1)]
        zeta = functools.reduce(lambda sums, x: sums + [sums[-1] + x], tmp, [0])

        # Store the translation map:
        self.distMap = [x / zeta[-1] for x in zeta]

    def next(self):
        # Take a uniform 0-1 pseudo-random value:
        u = random.random()

        # Translate the Zipf variable:
        return bisect.bisect(self.distMap, u) - 1

zipf=ZipfGenerator(10000,1)



def randomTrap():

    #Point is the geometric center of trapezoid

    point = random.uniform(-sys.maxint,sys.maxint)

    # Width of trapezoid (using zipf distribution)

    width = zipf.next() * random.uniform(0,sys.maxint/1000)

    # Adapt tilt if we want an angle more opened or not

    tilt = random.uniform(0.25,0.75)


    # Creating trapezoid a,b,c,d

    a = point-width/2

    d = point+width/2

    if (d < a):
        aux=d
        d=a
        a=aux

    b = point - tilt*(width/2)

    c = point + tilt*(width/2)

    if (c < b):
        aux=c
        c=b
        b=aux


    return [a,b,c,d]


def randomTrapWidth():

    point = random.uniform(-sys.maxint,sys.maxint)

    width = zipf.next() * random.uniform(0,sys.maxint/1000)

    tilt = random.uniform(0.25,0.75)

    a = point-width/2

    d = point+width/2

    if (d < a):
        aux=d
        d=a
        a=aux

    b = point - tilt*(width/2)

    c = point + tilt*(width/2)

    if (c < b):
        aux=c
        c=b
        b=c

    return width



# def randDoc(id):
#
#     x = randomTrap()
#     y = randomTrap()
#
#     post = {"_id": id, "x": x, "y": y}
#
#     post["x"]
#     post["y"]
#
#     print(x, y)
#     return post
#
# for i in xrange(1):
#     doc = randDoc(i)
#     print(json.dumps(doc))
#     if i % 1000 == 0:
#         print(".", end="", file=sys.stderr)
#
#


x = []

for i in xrange(1000):
    x.append(random.uniform(-sys.maxint,sys.maxint))
plt.hist(x, bins='auto', alpha=1, edgecolor='black', linewidth=1)
plt.grid(True)
plt.title("Histogram of centers with 'auto' bins")
plt.show()

x = []

for i in xrange(1000):
    x.append(randomTrapWidth())
plt.hist(x, bins='auto', alpha=1, edgecolor='black', linewidth=1)
plt.grid(True)
plt.title("Histogram of width with 'auto' bins")
plt.show()



for i in xrange(1000):
    x = randomTrap()
    y =[0,1,1,0]
    plt.plot(x,y)

plt.title("Trapezoids")

plt.show()






client = MongoClient("mongodb://main_admin:abc123@localhost:27017")

mydb = client["mydatabase"]
client.admin.command('enableSharding', 'mydatabase')
#NO PARA STANDALONE
mycol = mydb["mytest"]


random.seed(SEED)

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


zipf = ZipfGenerator(SIZE, 1) #10000???


def randomTrap():
    # Point is the geometric center of trapezoid

    point = random.uniform(-DOMAINMIN, DOMAINMAX)

    # Width of trapezoid (using zipf distribution)

    width = zipf.next() * random.uniform(IMPRECISIONMIN, IMPRECISIONMAX)

    # Adapt tilt if we want an angle more opened or not

    tilt = random.uniform(FUZZYMIN, FUZZYMAX)

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


for i in xrange(SIZE):
    mydict = randDoc(i)
    n = mycol.insert_one(mydict)

timesql= datetime.date.now()

myquery = {"$where:'feq(this.x,[]) >=0.5'"}
mydoc = mycol.find(myquery).explain("executionStats")

sql = "UPDATE Query SET time = %s WHERE id = %s"
val = (timesql, idQue)
cursor.execute(sql, val)
mydb.commit()

sql = "UPDATE Query SET timelast = %s WHERE id = %s"
val = (datetime.date.now(), idQue)
cursor.execute(sql, val)
mydb.commit()

sql = "UPDATE Test SET updatedAt = %s WHERE id = %s"
val = (datetime.date.now(), idTest)
cursor.execute(sql, val)
mydb.commit()


#Get the file name for the new file to write
filename = TESTNAME

# If the file name exists, write a JSON string into the file.
if filename:
    # Writing JSON data
    with open(filename, 'w') as f:
        json_util.dumps(mydoc,f)


