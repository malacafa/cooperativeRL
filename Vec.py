from math import cos, sin, sqrt, pi

class Vector:
    def __init__(self):
        self.heading = 0
        self.xVector = 10
        self.yVector = 0

    def reset(self):
        self.heading = 0
        self.xVector = 10
        self.yVector = 0 
        
    def changeVec(self, action):
        if action == 0: #backward
            self.heading = self.heading + pi
            if self.heading > 2*pi:
                self.heading = self.heading - 2*pi
            self.xVector = -1*self.xVector # xVector reverse
            self.yVector = -1*self.yVector # yVector reverse
        
        if action == 1: #forward
            self.heading = self.heading
            self.xVector = self.xVector
            self.yVector = self.yVector

        if action == 2: #left
            self.heading -= pi/6
            if self.heading < 0:
                self.heading = 2*pi-abs(self.heading)
            
            vec = sqrt(self.xVector**2 + self.yVector**2)
            self.xVector = vec*cos(self.heading)
            self.yVector = vec*sin(self.heading)
        
        if action == 3: #right
            self.heading += pi/6
            if self.heading > 2*pi:
                self.heading = self.heading - 2*pi

            vec = sqrt(self.xVector**2 + self.yVector**2)
            self.xVector = vec*sin(self.heading)
            self.yVector = vec*cos(self.heading)
    
    def getVector(self):
        return [self.xVector, self.yVector]
