import pygame
import random,sys

screen = pygame.display.set_mode((660,260))

"""
Dna Structure = 
{
    "eyes" = {"Color" : (r,g,b), "Size" : radius},
    "face" = {"Color" : (r,g,b) , "Size" : radius},
    "mouth" = {"Color" : (r,g,b), "Size" : radius},
    "nose" = {"Color" : (r,g,b), "Size" : radius}
}
"""

def RandColor():
    return (random.randint(0,235), random.randint(0,205), random.randint(0,235))

class Face(object):

    def __init__(self,Offset):
        self.dna = {}
        x,y = Offset
        #Positions
        self.NoseLocs = (x + 130,y + random.randint(115,145))
        self.FaceLocs = (x + 130,y + 130)
        self.MouthLocs = (x + 130,y + 150)
        self.EyeLocs1 = (x + random.randint(85,115),y + random.randint(100,110))
        self.EyeLocs2 = (x + random.randint(145,155),y + random.randint(100,110))

    def GenerateFaceData(self):
        self.dna = {
                "eyes" : {"Color" : RandColor(), "Size" : random.randint(5,25)},
                "face" : {"Color" : RandColor(), "Size" : random.randint(65,90)},
                "mouth" : {"Color" : RandColor(), "Size" : random.randint(15,25)},
                "nose" : {"Color" : RandColor(), "Size" : random.randint(5,15)}
        }


    def PlotFace(self):
        pygame.draw.circle(screen,self.dna["face"]["Color"],self.FaceLocs,self.dna["face"]["Size"])
        pygame.draw.circle(screen,self.dna["mouth"]["Color"],self.MouthLocs,self.dna["mouth"]["Size"])
        pygame.draw.circle(screen,self.dna["nose"]["Color"],self.NoseLocs,self.dna["nose"]["Size"])
        pygame.draw.circle(screen,self.dna["eyes"]["Color"],self.EyeLocs1,self.dna["eyes"]["Size"])
        pygame.draw.circle(screen,self.dna["eyes"]["Color"],self.EyeLocs2,self.dna["eyes"]["Size"])


Face1 = Face((0,0))
Face1.GenerateFaceData()

Face2 = Face((220,0))
Face2.GenerateFaceData()

Face3 = Face((440,0))
Face3.GenerateFaceData()

while True:
    screen.fill((245,200,245))
    Face1.PlotFace()

    Face2.PlotFace()

    Face3.PlotFace()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()
