import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

print(mydb)


#
# seedInicialization = SEED
# ZipfGenerator(n, alpha):
# # Calculate Zeta values from 1 to n:
# for i in range(1, n + 1)
#   tmp = [1 / i ^ alpha]
# zeta = reduce(
#   x: sums + [sums[-1] + x], tmp, [0]
# )
# # Store the translation map:
# distMap = [x / zeta[-1] for x in zeta]
#
# next:
# random = randomPsudoUniformValue
#
# # Translate the Zipf variable:
# return bisect(distMap, random) - 1
#
# zipf = ZipfGenerator(SIZE, 1)
#
# RandomTrapezoidGenerator:
# # Point is the geometric
# center
# of
# trapezoid
#
# point = random(
#   -systemMaxSize, systemMaxSize)
#
# # width = TrapezoidBaseSize
# width = zipf.next * randomValue
#
# # titl = TrapezoidMoreOrLessOpened
# tilt = random(ANGLE
# DEGREES)
#
# # Creating trapezoid a,b,c,d
# a = point - width / 2
# d = point + width / 2
#
# if (d < a):
#   aux = d, d = a, a = aux
#
# b = point - tilt * (width / 2)
# c = point + tilt * (width / 2)
#
# if (c < b):
#   aux = c, c = b, b = aux
#
# return [a, b, c, d]
#
# randomDocumentGenerator(id):
# x = RandomTrapezoidGenerator()
# post = {"id" = id, "x" = x}
# return post
#
# for i in xrange(NUMBEROFDOCUMENTS):
#   MongoDB.insertIntoCollection(
#     randomDocumentGenerator(i))
#
