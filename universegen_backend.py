# universegen_backend.py

import object_data_templates
import sqlite_init
import maths_helper
import sqlite3
from sqlite3 import Error

from numpy import random

#some constants

universeSizeX = 100000
universeSizeY = 100000

systemSizeX = 1000
systemSizeY = 1000

maxPlanets = 15
noOfStars = 250

conn = None



def createSystemData(conn):

    c = conn.cursor()

    planetId = 0

    systemId = 0
    while systemId < noOfStars:

        typeIndex = random.randint(0, len(object_data_templates.starData))
    
        locationX = random.randint(0, universeSizeX)
        locationY = random.randint(0, universeSizeY)
        name = object_data_templates.starNames[random.randint(0, len(object_data_templates.starNames))]
        type = object_data_templates.starData[typeIndex]['Type']
        temp = round(float(object_data_templates.starData[typeIndex]['Temp'])*random.uniform(0.5,1.5))
        mass = round(float(object_data_templates.starData[typeIndex]['Mass'])*random.uniform(0.5,1.5), 3)
        starRadius = round(float(object_data_templates.starData[typeIndex]['Radius'])*random.uniform(0.5,1.5), 3)
        luminosity = round(float(object_data_templates.starData[typeIndex]['Luminosity'])*random.uniform(0.5,1.5), 3)
        description = object_data_templates.starData[typeIndex]['Desc']

        
        numberOfPlanets = random.randint(0,1000)%maxPlanets

        c.execute(sqlite_init.writeSystems, (systemId, locationX, locationY, name, type, temp, mass, starRadius, luminosity, description))    
        j = 1
        while j <= numberOfPlanets:
            
            radius = random.randint(0, systemSizeX/2)
            angle = random.randint(0, 360)
            location = maths_helper.calculateOrbitalCoordinates(radius, angle)
            locationX = location[0]
            locationY = location[1]
            planetName = name + " " + str(j)
            c.execute(sqlite_init.writePlanets, (planetId, locationX, locationY, planetName, systemId))
            planetId = planetId+1
            j = j + 1

        systemId=systemId+1

        conn.commit()
        
        
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
    closeDbConnection(conn)    
    universeFile.close()
    

if __name__ == "__main__":
    main()
