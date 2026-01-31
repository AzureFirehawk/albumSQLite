"""
Stats Module:
Read-only aggregation functions from database
"""

from utils import get_menu_choice, prompt_continue
from albums import get_albums_for_artist, display_albums
from artists import get_all_artists, display_artists

def show_stats_menu(conn):
  """
  Show stats menu and prompt user for choice
  """
  while True:
    print("\n== Collection Statistics ==")
    total_albums(conn)
    total_artists(conn)
    print("\n1. Albums per artist")
    print("2. Albums per genre")
    print("3. Return to main menu")
    choice = get_menu_choice(3)

    if choice == 1:
      albums_per_artist(conn)
      if not prompt_continue("\nPress enter to return to stats menu..."):
        break
    elif choice == 2:
      albums_per_genre(conn)
      if not prompt_continue("\nPress enter to return to stats menu..."):
        break
    elif choice == 3:
      break

def albums_per_artist(conn):
  """
  Show albums by artist
  """
  artists = get_all_artists(conn)
  if not artists:
    print("There are no artists in the database.")
    return
  
  print ("\n== Albums per Artist ==")
  artist_counts = []
  for artist_id, name in artists:
    albums = get_albums_for_artist(conn, artist_id)
    artist_counts.append((name, len(albums)))

  artist_counts.sort(key=lambda x: x[1], reverse=True)

  for name, count in artist_counts:
    print(f"{name}: {count} album{'s' if count != 1 else ''}")



def albums_per_genre(conn):
  """
  Show albums by genre
  """
  c = conn.cursor()
  c.execute("""
    SELECT
      COALESCE(genre, 'Unknown Genre') AS genre,
      COUNT(*) AS count
    FROM albums
    GROUP BY genre
    ORDER BY count DESC, genre
  """)
  results = c.fetchall()

  if not results:
    print("There are no albums in the database.")
    return

  print("\n== Albums per Genre ==")
  for genre, count in results:
    print(f"\n{genre:<20}: {count} album{'s' if count != 1 else ''}")

def total_albums(conn):
  c = conn.cursor()
  c.execute("""SELECT COUNT(*) FROM albums""")
  total = c.fetchone()[0]
  print(f"\nTotal albums in collection: {total}")

def total_artists(conn):
  c = conn.cursor()
  c.execute("""SELECT COUNT(*) FROM artists""")
  total = c.fetchone()[0]
  print(f"\nTotal artists in collection: {total}")