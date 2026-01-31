"""
Albums Module:
CRUD functions for albums
"""

from artists import show_or_add_artist, select_artist
from utils import get_menu_choice

# ------------Main Menu Functions------------
# ---Add Album---
def add_album(conn):
  """
  Add new album to database
  """
  print("\n== Add Album ==")
  artist_id, name = show_or_add_artist(conn)
  title = prompt_album_title()
  genre = prompt_album_genre()
  insert_album(conn, artist_id, title, genre)
  print(f"'{title}' by {name} has been added to the database.")

# ---Edit Album---
def edit_album(conn):
  """
  Edit existing album in database
  """
  print("\n== Edit Album ==")

  artist_id = select_artist(conn)
  if not artist_id:
    return
  
  albums = get_albums_for_artist(conn, artist_id)
  if not albums:
    print("There are no albums for this artist.")
    return

  album_id, current_title, current_genre = select_album(albums)
  print("\nCurrent album details:")
  print(f"Title: {current_title}")
  print(f"Genre: {current_genre if current_genre else 'Unknown Genre'}")

  title = prompt_edit_value("Title", current_title)
  genre = prompt_edit_value("Genre", current_genre)

  update_album(conn, album_id, title, genre)
  print(f"Album '{title}' has been updated in the database.")

# ---Delete Album---
def delete_album(conn):
  """
  Delete album from database
  """
  print("\n== Delete Album ==")

  artist_id = select_artist(conn)
  if not artist_id:
    return

  albums = get_albums_for_artist(conn, artist_id)
  if not albums:
    print("There are no albums for this artist.")
    return

  album_id, title, _ = select_album(albums)

  confirm = input(f"Are you sure you want to delete '{title}'? (y/n): ").strip().lower()
  if confirm != "y":
    print("Album deletion cancelled.")
    return
  
  remove_album(conn, album_id)
  print(f"Album '{title}' has been deleted from the database.") 

# ---View Albums by Artist---
def view_by_artist(conn, artist_id):
  """
  Returns a list of albums for a given artist
  """
  albums = get_albums_for_artist(conn, artist_id)
  if not albums:
    print("No albums found.")
    return
  display_albums(albums)

# ------------User Input Functions------------
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

def prompt_edit_value(field_name, current_value):
  value = input(f"{field_name} (blank to keep '{current_value}'): ").strip()
  return value.title() if value else current_value

def select_album(albums):
  """
  Helper function to consolidate menu selection code
  Returns: (album_id, title, genre)
  """ 
  print("\nAlbums:")
  display_albums(albums)
  choice = get_menu_choice(len(albums))
  return albums[choice - 1]

# ------------Database Helper Functions------------
def insert_album(conn, artist_id, title, genre=None):
  c = conn.cursor()
  c.execute("""
    INSERT INTO albums (artist_id, title, genre)
    VALUES (?, ?, ?)
  """, (artist_id, title, genre)
  )
  conn.commit()

def get_albums_for_artist(conn, artist_id):
  c = conn.cursor()
  c.execute("""
    SELECT album_id, title, genre
    FROM albums
    WHERE artist_id = ?
    ORDER BY title
  """, (artist_id,)
  )
  return c.fetchall()

def display_albums(albums):
  for index, (_, title, genre) in enumerate(albums, start=1):
    display_genre = genre.title() if genre else "Unknown Genre"
    print(f"{index}. {title} ({display_genre})")

def update_album(conn, album_id, title, genre=None):
  c = conn.cursor()
  c.execute("""
    UPDATE albums
    SET title = ?, genre = ?
    WHERE album_id = ?
  """, (title, genre, album_id)
  )
  conn.commit()

def remove_album(conn, album_id):
  c = conn.cursor()
  c.execute("""
    DELETE FROM albums
    WHERE album_id = ?
  """, (album_id,)
  )
  conn.commit()