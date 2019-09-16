from pymongo import MongoClient
import sys
import random
import math
import functools
import bisect
import pymysql
import datetime
import commands
import time

SEED = sys.argv[1];
print "Seed: " + SEED
QUERYSEED = sys.argv[2];
print "Query-Seed: " + QUERYSEED


TESTNAME="Test - Outdatabase vs Indatabase - 500 docs" + SEED;
print "Test - Outdatabase vs Indatabase - 500 docs"
EXPERIMENT = 3; # 1-6
NODES=5; #4+router+config

#---------------- Database --------------------------
SIZE = 500;#500,1000,2000,5000

FUZZYMIN = 0.25;
FUZZYMAX = 0.75 ;
DOMAINMIN = sys.maxint;
DOMAINMAX = sys.maxint;
IMPRECISIONMIN = 0.0;
IMPRECISIONMAX = DOMAINMAX/1000;

#---------------- Queries -----------------------------
NUMQUERIES = 30;

FUZZYMINQ = 0.25;
FUZZYMAXQ = 0.75 ;
DOMAINMINQ = sys.maxint;
DOMAINMAXQ = sys.maxint;
IMPRECISIONMINQ = 0.0;
IMPRECISIONMAXQ = DOMAINMAX/1000;

TYPE= "feq";
OPERATION=">=";
rango = random.randrange(0,10,1)
REQUIREMENTLEVEL = rango/10.0;
print "req: "
print  REQUIREMENTLEVEL


# Abre conexion con la base de datos

#db = pymysql.connect("35.233.40.167","root","a1rpagz2","experimental")

db = pymysql.connect("34.76.127.234","root","a1rpagz2","experimental")

#db = pymysql.connect("127.0.0.1","root","a1rpagz2","experimental")


# prepare a cursor object using cursor() method
cursor = db.cursor()


#memoria GB
#cpuNum double
sql = "INSERT INTO Environment (nodesNum, machineType, cpuNum, ramMemory, diskType, zone)" \
      " VALUES (%s, %s, %s, %s, %s, %s)"
val = (NODES,"n1-standard-2",0.25,0.5,"SSD","europe-west1-b")
cursor.execute(sql, val)
db.commit()
idEnv=cursor.lastrowid
print idEnv


sql = "INSERT INTO Dbase (seed, size, fuzzyficationMin, fuzzyficationMax, imprecisionMin, imprecisionMax, domainMin, domainMax)" \
      " VALUES (%s,%s,%s,%s, %s, %s, %s, %s)"
val = (SEED,SIZE,FUZZYMIN,FUZZYMAX,IMPRECISIONMIN,IMPRECISIONMAX,DOMAINMIN,DOMAINMAX)
cursor.execute(sql, val)
db.commit()
idDab=cursor.lastrowid
print idDab


sql = "INSERT INTO QuerySet (type, totalTime, seed, numQueries, fuzzyficationMin, fuzzyficationMax, imprecisionMin, imprecisionMax, domainMin, domainMax)" \
      " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = (TYPE,0,QUERYSEED,NUMQUERIES,FUZZYMINQ,FUZZYMAXQ,IMPRECISIONMINQ,IMPRECISIONMAXQ,DOMAINMINQ,DOMAINMAXQ)
cursor.execute(sql, val)
db.commit()
idQuerySet=cursor.lastrowid
print idQuerySet



sql = "INSERT INTO Test (name, createdAt, updatedAt, idExperiment, idEnvironment, idDbase, idQuerySet)" \
      " VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = (TESTNAME,datetime.datetime.now(),datetime.datetime.now(),EXPERIMENT,idEnv,idDab,idQuerySet)
cursor.execute(sql, val)
db.commit()
idTest=cursor.lastrowid
print idTest



client = MongoClient("mongodb://main_admin:abc123@localhost:27017")



mydb = client["mydatabase"]
mycol = mydb["mytest"]
mycol.delete_many({})
client.admin.command('enableSharding', 'mydatabase')
#NO PARA STANDALONE



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


def randomTrap(domainMin, domainMax, imprecisionMin, imprecisionMax, fuzzyMin, fuzzyMax, numTrap):

    zipf = ZipfGenerator(numTrap, 1)
    # Point is the geometric center of trapezoid

    point = random.uniform(domainMin,domainMax)

    # Width of trapezoid (using zipf distribution)

    width = zipf.next() * random.uniform(imprecisionMin, imprecisionMax)

    # Adapt tilt if we want an angle more opened or not

    tilt = random.uniform(fuzzyMin, fuzzyMax)

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
    x = randomTrap(-DOMAINMIN,DOMAINMAX,IMPRECISIONMIN,IMPRECISIONMAX,FUZZYMIN,FUZZYMAX,SIZE)

    post = {"_id": id, "x": x}
    post["x"]
    return post


for i in xrange(SIZE):
    mydict = randDoc(i)
    n = mycol.insert_one(mydict)


totalTime=0

for i in range(1, NUMQUERIES+1):
    sql = "INSERT INTO Query (ordered, idQuerySet, resultsNum, timeMillis, operation, requirementLevel)" \
          " VALUES (%s, %s, %s, %s, %s, %s)"
    val = (i, idQuerySet, 0, 0, OPERATION, REQUIREMENTLEVEL)
    cursor.execute(sql, val)
    db.commit()
    idQue = cursor.lastrowid
    print "id Query:"
    print idQue

    random.seed(QUERYSEED)
    y=randomTrap(-DOMAINMINQ,DOMAINMAXQ,IMPRECISIONMINQ,IMPRECISIONMAXQ,FUZZYMINQ,FUZZYMAXQ,NUMQUERIES)
    fullStr = ','.join([str(elem) for elem in y])
    #"$where:'feq(this.x,[-10000,0,1,10000]) >=0.5'"
    #lista = mycol.find({"$where": 'feq(this.x,['+ fullStr +'])' + OPERATION + str(REQUIREMENTLEVEL)})
    mydb.command({"planCacheClear": "mycol"})#cache cleaned
    #mydoc= mycol.find({"$where": 'feq(this.x,[' + fullStr + '])' + OPERATION + str(REQUIREMENTLEVEL)}).explain()

    millis = int(round(time.time() * 1000))

    mydoc2 = mycol.find({})
    lista = list()
    for d in mydoc2:
        alfaA = d[0]
        betaA = d[1]
        gammaA = d[2]
        deltaA = d[3]

        alfaB = y[0]
        betaB = y[1]
        gammaB = y[2]
        deltaB = y[3]

        res=0
        if (gammaA >= betaB and betaA <= gammaB) :
            res=1

        if (deltaA <= alfaB or alfaA >= deltaB) :
            res= 0

        if (deltaA > alfaB and gammaA < betaB) :
            res= (deltaA - alfaB) / ((betaB - alfaB) - (gammaA - deltaA))
        else:
            res= ((deltaB - alfaA) / ((betaA - alfaA) - (gammaB - deltaB)))

        if (res >= REQUIREMENTLEVEL):
            lista.append(d)

    millis2= int(round(time.time() * 1000))

    querytime=millis2-millis

    totalTime= totalTime + querytime

    sql = "UPDATE QuerySet SET totalTime = %s WHERE id = %s"
    val = (totalTime, idQuerySet)
    cursor.execute(sql, val)
    db.commit()

    sql = "UPDATE Query SET resultsNum = %s WHERE id = %s"
    val = (lista.len(), idQue)
    cursor.execute(sql, val)
    db.commit()

    sql = "UPDATE Query SET timeMillis = %s WHERE id = %s"
    val = (querytime, idQue)
    cursor.execute(sql, val)
    db.commit()

sql = "UPDATE Test SET updatedAt = %s WHERE id = %s"
val = (datetime.datetime.now(), idTest)
cursor.execute(sql, val)
db.commit()





# desconecta del servidor SQL
db.close()
#desconecta mongo
client.close()