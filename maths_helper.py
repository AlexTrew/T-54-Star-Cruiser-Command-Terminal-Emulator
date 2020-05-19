from math import cos, sin

def calculateOrbitalCoordinates(radius, angle):
    return [round(radius*cos(angle)), round(radius*sin(angle))]
