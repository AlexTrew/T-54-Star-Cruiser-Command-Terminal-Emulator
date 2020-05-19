# universegen_backend.py

import object_data_templates
import sqlite_init

import sqlite3
from sqlite3 import Error

from numpy import random
from math import cos, sin

#some constants

universeSizeX = 100000
universeSizeY = 100000

systemSizeX = 1000
systemSizeY = 1000

maxPlanets = 15
noOfStars = 250

conn = None


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


def createSystemData(conn):

    c = conn.cursor()

    i = 0
    while i < noOfStars:

        name = object_data_templates.starNames[random.randint(0, len(object_data_templates.starNames))]

        s = System((random.randint(0, universeSizeX),random.randint(0, universeSizeY)), name, random.randint(0,len(object_data_templates.starData)))
    
        #generate planets
        numberOfPlanets = random.randint(0,1000)%maxPlanets

        c.execute(sqlite_init.writeSystems, (i, s.location.index(0), s.location.index(1), s.name, s.type, s.temp, s.mass, s.starRadius, s.luminosity, s.description))
    
        j = 0
        while j < numberOfPlanets:
            radius = random.randint(0, systemSizeX/2)
            angle = random.randint(0, 360)        
            p = Planet(radius, angle, name+ " "+str(i+1))
            s.planets.append(p)
            print(p.name + " " + str(p.location))
            j = j + 1

        i=i+1
        
def createDbConnection(db_file):
    """ create a database connection to a SQLite database """
    try:
        print(sqlite3.version)
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

def closeDbConnection(conn):
    try:
        conn.close()
    except Error as e:
        print(e)

   
def initDb(conn):
    c = conn.cursor()
    c.executescript(sqlite_init.init)


def main():
    universeFile = open("universe.T54", "w")
    conn = createDbConnection("universe.T54")

    initDb(conn)
    
    
    createSystemData(conn)
    i = i+1
    closeDbConnection(conn)    
    universeFile.close()
    

if __name__ == "__main__":
    main()
