from math import sqrt
from Vec import Vector
from DrawMap import DrawMap

class Theif:
    def __init__(self):
        self.lifeLength = 0
        self.isCaught = False
        self.vector = Vector()
        self.position = [3*30, 3*30]
        self.drawmap = DrawMap()
        self.drawmap.setMap()
        self.mapList = self.drawmap.getMap()
    
    def reset(self):
        self.lifeLength = 0
        self.isCaught = False
        self.position = [3*30, 3*30]
        self.vector.reset()
    
    def chkCollision(self):
        for i in range(30):
            for j in range(30):
                if self.mapList[i][j] == 1:
                    if self.distBetween(self.position, [i*30, j*30]) <= 10:
                        return 1
        
        return 0

    def move(self, action, position1, position2):
        self.vector.changeVec(action)
        xVector, yVector = self.vector.getVector()
        xPos, yPos = self.position
        if self.chkCollision() != 1:   
            xPos += xVector
            yPos += yVector
        self.position = [int(xPos), int(yPos)]
    
    def distBetween(self, posA, posB):
        tempX = (posA[0] - posB[0])**2
        tempY = (posA[1] - posB[0])**2
        return sqrt(tempX+tempY)
    
    def getPosition(self):
        return self.position
    
    def checkCaught(self, position1, position2):
        r = [False]*2
        if self.distBetween(self.position, position1) < 30: # change the number
            self.isCaught = True
            r[0] = True

        if self.distBetween(self.position, position2) < 30:
            self.isCaught = True
            r[1] = True
        
        return r
################################################################################
class Police:
    def __init__(self, id):
        self.lifeLength = 0
        self.didCatch = False
        self.vector = Vector()
        self.position = []
        self.drawmap = DrawMap()
        self.drawmap.setMap()
        self.mapList = self.drawmap.getMap()
        if id == 1:
            self.position = [27*30, 27*30]
        if id == 2:
            self.position = [3*30, 27*30]
    
    def reset(self, id):
        self.lifeLength = 0
        self.didCatch = False
        self.vector = Vector()
        if id == 1:
            self.position = [27*30, 27*30]
        if id == 2:
            self.position = [3*30, 27*30]
            
    def move(self, action):
        self.vector.changeVec(action)
        xVector, yVector = self.vector.getVector()
        xPos, yPos = self.position
        if self.chkCollision() != 1:   
            xPos += xVector
            yPos += yVector
        self.position = [int(xPos), int(yPos)]

    def distBetween(self, posA, posB):
        tempX = (posA[0] - posB[0])**2
        tempY = (posA[1] - posB[0])**2
        return sqrt(tempX+tempY)

    def chkCollision(self):
        for i in range(30):
            for j in range(30):
                if self.mapList[i][j] == 1:
                    if self.distBetween(self.position, [i*30, j*30]) <= 10:
                        return 1
        
        return 0
    
    def getPosition(self):
        return self.position