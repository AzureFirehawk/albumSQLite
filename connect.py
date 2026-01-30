import sqlite3

def connection():
  return sqlite3.connect('albums.db')

conn = sqlite3.connect('albums.db')

def initialize(conn):
  c = conn.cursor()

  c.execute("""CREATE TABLE IF NOT EXISTS artists (
    artist_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
  )""")

  c.execute("""CREATE TABLE IF NOT EXISTS albums (
    album_id INTEGER PRIMARY KEY AUTOINCREMENT,
    artist_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    genre TEXT,
    FOREIGN KEY (artist_id) REFERENCES artists (artist_id)
            ON DELETE CASCADE
  )""")

  conn.commit()
