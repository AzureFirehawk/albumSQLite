"""
Albums Module:
CRUD functions for albums
"""

from artists import show_or_add_artist
from utils import get_menu_choice

def add_album(conn):
  """
  Add new album to database
  """
  print("\n== Add Album ==")
  artist_id, name = show_or_add_artist(conn)
  title = prompt_album_title()
  genre = prompt_album_genre()
  insert_album(conn, artist_id, title, genre)
  print(f"{title} by {name} has been added to the database.")

def edit_album(conn):
  """
  Edit album in database
  """
  pass

def delete_album(conn):
  """
  Delete album from database
  """
  pass

def view_by_artist(conn, artist_id):
  """
  View albums by artist
  """
  pass

def display_albums(albums):
  """
  Display list of albums
  """
  pass

# user input prompts
def prompt_album_title():
  """
  Prompt user for album title
  """
  while True:
    title = input("Enter the album title: ").strip()
    if title:
      return title.title()

    print("Album title cannot be blank.")

def prompt_album_genre():
  """
  Prompt user for album genre
  """
  genre = input("Enter the album genre: ").strip()
  return genre.title() if genre else None

# SQL helpers
def insert_album(conn, artist_id, title, genre=None):
  c = conn.cursor()
  c.execute("""
    INSERT INTO albums (artist_id, title, genre)
    VALUES (?, ?, ?)
  """, (artist_id, title, genre)
  )
  conn.commit()