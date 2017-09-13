# Generate two random numbers (a,b) between -1 and 1
# If length from origo to the point is greated than 1, then the point is not
#   in the circle. Otherwise it is in the circle
# Sum up amount of in and out of circle.
# Do maths on this shit (see report) to estimate pi
# See report for more info


import random
import math
from grapher_1  import arrayPrinter
from grapher_1  import arrayColoredPrinter
from txter_1    import writeList
from txter_1    import write2DListToExcel

runs = 100000
cir = 0
sqr = 0
allPointList = []
sqrPointList = []
cirPointList = []

for i in range (runs):
    point = [(random.uniform(-1, 1)), (random.uniform(-1, 1))]

    allPointList.append(point)

    r = math.sqrt(point[0]**2 + point[1]**2)
    if (r > 1):
        sqr += 1
        sqrPointList.append(point)
    else:
        cir += 1
        cirPointList.append(point)


arrayColoredPrinter (allPointList, 0, 0, 0, False, True, True)
arrayColoredPrinter (cirPointList, 0, 0, 255, False, False, False)
arrayColoredPrinter (sqrPointList, 255, 0, 0, True, False, False)
writeList (allPointList)
write2DListToExcel (allPointList)



pi = 4 * (cir) / (cir + sqr)
error = abs(math.pi - pi)

print ("pi:\t"      + str(pi))
print ("error:\t"   + str(error))

print ("runs:\t"    + str(runs))
print ("cir:\t"     + str(cir))
print ("sqr:\t"     + str(sqr))

#print (allPointList)
