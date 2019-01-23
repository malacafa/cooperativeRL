import pygame
from random import randrange
from DrawMap import DrawMap
from Obj import Police, Theif

class Simulation:
    def __init__(self):
        self.size = 30
        self.window = pygame.display.set_mode((30*self.size, 30*self.size))
        self.fps = pygame.time.Clock()
        self.drawmap = DrawMap()
        self.police1 = Police(1)
        self.police2 = Police(2)
        self.theif = Theif()
        self.END = False
        self.map = self.drawmap.getMap()
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 10)

    def step(self, theifAction, police1Action, police2Action):
        done = False

        self.police1.move(police1Action)
        self.police2.move(police2Action)

        position1 = self.police1.getPosition()
        position2 = self.police2.getPosition()

        self.theif.move(theifAction, position1, position2)

        self.r = self.theif.checkCaught(position1, position2)
        position = self.theif.getPosition()
        self.window.fill(pygame.Color(255, 255, 255))
        print(position, position1, position2)
        pygame.draw.circle(self.window, pygame.Color(0, 0, 255), position, 30)
        pygame.draw.circle(self.window, pygame.Color(255, 0, 100), position1, 30)
        pygame.draw.circle(self.window, pygame.Color(255, 100, 0), position2, 30)
        for i in range(30):
            for j in range(30):
                if self.map[i][j] == 1:
                    pygame.draw.rect(self.window, pygame.Color(0, 0, 0), pygame.Rect(i*30, j*30, 30, 30))

        if True in self.r:
            done = True
        
        pygame.display.flip()
        self.fps.tick(10)
    
if __name__ == "__main__":
    simulation = Simulation()
    for i in range(100):
        a1 = randrange(4)
        a2 = randrange(4)
        a3 = randrange(4)
        simulation.step(1, 1, 1)