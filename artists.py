"""
Artists Module:
List, add, select artists
"""

import sqlite3
from utils import get_menu_choice

class ArtistAlreadyExists(Exception):
  """
  Exception raised when an artist already exists
  """
  pass

def show_or_add_artist(conn):
  """
  Gives user the option to select an exisiting artist or add a new one
  Returns: (artist_id, name)
  """
  
  artists = get_all_artists(conn)

  # if no artists, add one
  if not artists:
    print("There are no artists in the database. Lets add one!")
    return _add_artist_flow(conn)

  # display artists and "Add a new artist" option
  print("\nSelect an artist:")
  display_artists(artists)
  print(f"{len(artists) + 1}. Add a new artist")
  choice = get_menu_choice(len(artists) + 1)

    # if user picks an existing artist
  if choice <= len(artists):
    artist_id, name = artists[choice - 1]
    return artist_id, name
    
  # if user picks "Add a new artist"
  return _add_artist_flow(conn)

def select_artist(conn):
  """
  Prompt user to select an artist
  Returns: artist_id or None
  """
  artists = get_all_artists(conn)
  if not artists:
    print("There are no artists in the database.")
    return None
  
  display_artists(artists)
  choice = get_menu_choice(len(artists))
  artist_id, _ = artists[choice - 1]
  return artist_id


# Helper functions
def get_all_artists(conn):
  """
  Return list of (artist_id, name)
  """
  c = conn.cursor()
  c.execute("""
    SELECT artist_id, name 
    FROM artists 
    ORDER BY name
  """)
  return c.fetchall()

def _add_artist_flow(conn):
  """
  Setup flow for adding a new artist
  """
  name = prompt_new_artist_name()
  try:
    artist_id = add_artist(conn, name)
    return artist_id, name
  except ArtistAlreadyExists:
    print(f"{name} already exists in the database.")

def add_artist(conn, name):
  """
  Add new artist to database
  Returns: artist_id
  """
  try:
    c = conn.cursor()
    c.execute("""
      INSERT INTO artists (name)
      VALUES (?)
    """, (name,))
    conn.commit()
    return c.lastrowid
  except sqlite3.IntegrityError:
    raise ArtistAlreadyExists

def display_artists(artists):
  """
  Display list of artists
  """
  for index, (_, name) in enumerate(artists, start=1):
    print(f"{index}. {name}")

def prompt_new_artist_name():
  """
  Prompt user for new artist name
  """
  while True:
    name = input("Enter the artist name: ").strip().title()
    if name:
      return name
    print("Artist name cannot be blank.")
