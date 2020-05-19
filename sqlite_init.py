import sqlite3

init = "\
\
    PRAGMA foreign_keys = ON;\
    \
    CREATE TABLE IF NOT EXISTS Systems(\
        id INTEGER PRIMARY KEY,\
        location_x INTEGER,\
        location_y INTEGER,\
        name TEXT NOT NULL,\
        type TEXT NOT NULL,\
        temp INTEGER,\
        mass DOUBLE,\
        starRadius INTEGER,\
        luminosity INTEGER,\
        description INTEGER\
        );\
\
    CREATE TABLE IF NOT EXISTS Planets(\
        id integer PRIMARY KEY,\
        location_x integer,\
        location_y integer,\
        name TEXT,\
        systemId INTEGER,\
        FOREIGN KEY(systemId) REFERENCES Systems(id));"

    
writeSystems = "\
\
    INSERT INTO Systems(id, location_x, location_y, name, type ,temp, mass, starRadius, luminosity, description)\
    VALUES(?,?,?,?,?,?,?,?,?,?)\
"

writePlanets = "\
\
    INSERT INTO Planets(id, location_x, location_y, name, systemId)\
    VALUES(?,?,?,?,?)\
"
