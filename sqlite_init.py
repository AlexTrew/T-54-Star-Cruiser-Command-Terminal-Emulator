import sqlite3

initScript = "\
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
        starRadius INTEGER,\
        luminosity INTEGER,\
        description INTEGER\
        );\
\
    CREATE TABLE IF NOT EXISTS Planets(\
        id integer PRIMARY KEY,\
        name TEXT,\
        location_x integer,\
        location_y integer,\
        systemId INTEGER,\
        FOREIGN KEY(systemId) REFERENCES Systems(id));"

    

