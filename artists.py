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
  Output: artist_id
  """
  while True:
    artists = get_all_artists(conn)

    # if no artists, add one
    if not artists:
      print("There are no artists in the database. Lets add one!")
      try:
        name = prompt_new_artist_name()
        artist_id = add_artist(conn, name)
        return artist_id
      except ArtistAlreadyExists:
        print("That artist already exists.")
        continue
    
    # display artists and "Add a new artist" option
    print("\nSelect an artist:")
    display_artists(artists)
    print(f"{len(artists) + 1}. Add a new artist")
    choice = get_menu_choice(len(artists) + 1)

    # if user picks an existing artist
    if choice <= len(artists):
      artist_id = artists[choice - 1][0]
      return artist_id
    
    # if user picks "Add a new artist"
    else:
      name = prompt_new_artist_name()
      try:
        artist_id = add_artist(conn, name)
        return artist_id
      except ArtistAlreadyExists:
        print("That artist already exists.")

def get_all_artists(conn):
  """
  Return list of artist_id and name
  """
  c = conn.cursor()
  c.execute("""
    SELECT artist_id, name 
    FROM artists 
    ORDER BY name
  """)
  return c.fetchall()

def add_artist(conn, name):
  """
  Add new artist to database
  Output: artist_id
  """
  try:
    c = conn.cursor()
    c.execute("""
      INSERT INTO artists (name)
      VALUES (?)
    """, (name,))
    conn.commit()
    artist_id = c.lastrowid
    return artist_id
  except sqlite3.IntegrityError:
    raise ArtistAlreadyExists

def display_artists(artists):
  """
  Display list of artists
  """
  # for artist_id, name in artists:
  #   print(f"{artist_id + 1}. {name}")
  for index, (_, name) in enumerate(artists, start=1):
    print(f"{index}. {name}")

def prompt_new_artist_name():
  """
  Prompt user for new artist name
  """
  while True:
    name = input("Enter the artist name: ").strip()
    name = name.title()
    if name:
      return name

    print("Artist name cannot be blank.")
