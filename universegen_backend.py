# universegen_backend.py

import object_data_templates

from numpy import random
from math import cos, sin

#some constants

universeSizeX = 100000
universeSizeY = 100000

systemSizeX = 1000
systemSizeY = 1000

maxPlanets = 15
noOfStars = 250



#classes


class System:

    

    def __init__(self, location, name, typeIndex):
        self.location = location
        self.name = name
        self.type = object_data_templates.starData[typeIndex]['Type']
        self.temp = round(float(object_data_templates.starData[typeIndex]['Temp'])*random.uniform(0.5,1.5))
        self.mass = round(float(object_data_templates.starData[typeIndex]['Mass'])*random.uniform(0.5,1.5), 3)
        self.starRadius = round(float(object_data_templates.starData[typeIndex]['Radius'])*random.uniform(0.5,1.5), 3)
        self.luminosity = round(float(object_data_templates.starData[typeIndex]['Luminosity'])*random.uniform(0.5,1.5), 3)
        self.description = object_data_templates.starData[typeIndex]['Desc']
    planets = list()
    
class Planet:

    def calulatePlanetPosition(self, radius, angle):
        x = round(radius*cos(angle))
        y = round(radius*sin(angle))
        return x,y   
    
    def __init__(self, radius, angle, name):
        self.radius = radius
        self.angle = angle
        self.name = name
        self.location = self.calulatePlanetPosition(radius, angle)


def createSystem():


    name = object_data_templates.starNames[random.randint(0, len(object_data_templates.starNames))]

    s = System((random.randint(0, universeSizeX),random.randint(0, universeSizeY)), name, random.randint(0,len(object_data_templates.starData)))
    
    #generate planets
    numberOfPlanets = random.randint(0,1000)%maxPlanets
    
    print("Generating Star, " + name + ", at" + str(s.location) + " with " + str(numberOfPlanets) + " heavenly bodies")
    print("Type: " + s.type + ", Temperature: " + str(s.temp) + ", Mass: " + str(s.mass) + ", Radius: " + str(s.starRadius) + ", Luminosity: " + str(s.luminosity) + ", Description: " + s.description)
    print("Planets:")
    i = 0
    while i < numberOfPlanets:
        radius = random.randint(0, systemSizeX/2)
        angle = random.randint(0, 360)        
        p = Planet(radius, angle, name+ " "+str(i+1))
        s.planets.append(p)
        print(p.name + " " + str(p.location))
        i = i + 1
        
        
    
def main():
    i = 0
    while i < noOfStars:
        createSystem()
        i = i+1 

if __name__ == "__main__":
    main()