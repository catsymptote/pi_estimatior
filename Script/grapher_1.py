from PIL import Image
import os.path

xSize = 1024    # Horizontal resolution
ySize = 1024    # Vertical resolution


def __highListFinder(TwoDimList):
    lowX    = TwoDimList[0][0]
    lowY    = TwoDimList[0][1]
    highX   = TwoDimList[0][0]
    highY   = TwoDimList[0][1]

    for i in range (len(TwoDimList)):
        if (TwoDimList[i][0] > lowX):
            lowX = TwoDimList[i][0]
        if (TwoDimList[i][1] > lowY):
            lowY = TwoDimList[i][1]
        if (TwoDimList[i][0] < highX):
            highX = TwoDimList[i][0]
        if (TwoDimList[i][1] < highY):
            highY = TwoDimList[i][1]
    return (lowX, lowY, highX, highY)


def __coordinateSystemConverter (pointList, lowHighVal, coordSize):
    shiftedPointList = pointList
    for i in range (len(pointList)):
        shiftedPointList[i][0] = int((pointList[i][0] - lowHighVal[0])/(lowHighVal[2] - lowHighVal[0]) * coordSize[0])
        shiftedPointList[i][1] = int((pointList[i][1] - lowHighVal[1])/(lowHighVal[3] - lowHighVal[1]) * coordSize[1])
        #print ("sPL[" + str(i) + "][0]\t" + str(shiftedPointList[i][0]))
        #print ("sPL[" + str(i) + "][1]\t" + str(shiftedPointList[i][1]))
        #print ("-------------------")
    return shiftedPointList


"""
def __printCoordSystem (shiftedPointList, coordSize, origo):
    for y in range (coordSize[1]):
        img.putpixel((origo[0], coordSize[1] - y, (255, 255, 255) ))
"""


def arrayPrinter (pointList):
    coordSize = [xSize, ySize]
    print ("coordSize\t" + str(coordSize))

    lowHighVal = __highListFinder(pointList)
    print ("lowHighVal\t" + str(lowHighVal))

    shiftedPointList = __coordinateSystemConverter (pointList, lowHighVal, coordSize)

    # Create the image, close it, then open it, because reasons or whatever :P
    print ("File already exist?\t" + str(os.path.isfile("img/img.png")))
    if (not os.path.isfile("img/img.png")):
        img = Image.new("RGB", (coordSize[0] + 1, coordSize[1] + 1), (0, 0, 0))
        img.save("img/img.png", "PNG")
    img = Image.open("img/img.png")

    for i in range(len(shiftedPointList)):
        #print ("----------")
        #print (i)
        #print (int(shiftedPointList[i][0]))
        #print (int(shiftedPointList[i][1]))
        #print ("----------")
        img.putpixel( (int(shiftedPointList[i][0]), coordSize[1] - int(shiftedPointList[i][1])), (0, 0, 0) )

    img.save("img/img.png", "PNG")
    img.show()


def arrayColoredPrinter (pointList, cR, cG, cB, showImg, remakeImg, printOrigo):
    coordSize = [xSize, ySize]
    print ("coordSize\t" + str(coordSize))

    lowHighVal = __highListFinder(pointList)
    print ("lowHighVal\t" + str(lowHighVal))

    shiftedPointList = __coordinateSystemConverter (pointList, lowHighVal, coordSize)
    origo = [[0, 0], [0, 0]]
    shiftedOrigo = __coordinateSystemConverter (origo, lowHighVal, coordSize)

    # Create the image, close it, then open it, because reasons or whatever :P
    print ("File already exist?\t" + str(os.path.isfile("img/img.png")))
    if (not os.path.isfile("img/img.png") or remakeImg):
        img = Image.new("RGB", (coordSize[0] + 1, coordSize[1] + 1), (0, 0, 0))
        img.save("img/img.png", "PNG")
    img = Image.open("img/img.png")

    for i in range(len(shiftedPointList)):
        #print ("----------")
        #print (i)
        #print (int(shiftedPointList[i][0]))
        #print (int(shiftedPointList[i][1]))
        #print ("----------")
        img.putpixel( (int(shiftedPointList[i][0]), coordSize[1] - int(shiftedPointList[i][1])), ( cR, cG, cB ) )

    if (printOrigo):
        print (shiftedOrigo)
        for y in range (coordSize[1]):
            #print (coordSize[1])
            #print (shiftedOrigo)
            #print (shiftedOrigo[0][0])
            #print (coordSize[1] - int(y))
            #print (y)
            img.putpixel((int(coordSize[0] - shiftedOrigo[0][0]), int(coordSize[0] - y)), (255, 255, 255) )
        for x in range (coordSize[0]):
            img.putpixel((int(x), int(shiftedOrigo[0][0])), (255, 255, 255) )
        #__printCoordSystem(shiftedPointList, coordSize, origo)
        #img.putpixel( (int(shiftedOrigo[0][0]), coordSize[1] - int(shiftedOrigo[0][1])), ( 255, 255, 255 ) )

    img.save("img/img.png", "PNG")
    if (showImg):
        img.show()


#listA = [[1, 1], [2, 4], [13, 13], [24, 24], [32, 32], [48, 53], [-18, -17], [-20, 16]]
#arrayPrinter(listA)
