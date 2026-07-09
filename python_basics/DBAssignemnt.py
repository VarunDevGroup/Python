import sqlite3

DBName='MusicalTrackDatabase.sqlite'

lstTables=['Artist','Genre','Album','Track']

Query1='''CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);'''


Query2='''CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);'''

Query3='''CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);'''


Query4='''CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);'''

#try:
connection=sqlite3.connect(DBName)
cur= connection.cursor()

for tName in lstTables:
    cur.execute(f'''DROP TABLE IF EXISTS {tName}''')

cur.execute(Query1)
cur.execute(Query2)
cur.execute(Query3)
cur.execute(Query4)

fileHandle=open('C:\\Users\\Varun\\Downloads\\tracks\\tracks\\tracks.csv')
for line in fileHandle:
    lineArray=line.strip().split(',')
    if len(lineArray) < 6 : continue

    name = lineArray[0]
    artist = lineArray[1]
    album = lineArray[2]
    count = lineArray[3]
    rating = lineArray[4]
    length = lineArray[5]
    genre  = lineArray[6]

    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]
    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, len, rating, count,genre_id) 
        VALUES ( ?, ?, ?, ?, ?,? )''', 
        ( name, album_id, length, rating, count ,genre_id) )

    connection.commit()
    
connection.close()
#except Exception as e:
#    print("Error:", e)

    