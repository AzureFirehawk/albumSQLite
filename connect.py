import sqlite3

conn = sqlite3.connect('albums.db')

c = conn.cursor()

c.execute("""CREATE TABLE artists (
  artist_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL
)""")

c.execute("""CREATE TABLE albums (
  album_id INTEGER PRIMARY KEY AUTOINCREMENT,
  artist_id INTEGER NOT NULL,
  title TEXT NOT NULL,
  genre TEXT,
  FOREIGN KEY (artist_id) REFERENCES artists (artist_id)
          ON DELETE CASCADE
)""")

conn.commit()
conn.close()