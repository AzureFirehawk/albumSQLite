"""
Main program file
Controls main program loop and routes user input to appropriate functions
"""

# Import modules
from connect import connection, initialize
from artists import show_or_add_artist
from albums import (
  add_album,
  edit_album,
  delete_album,
  view_by_artist
)
from stats import show_stats_menu
from utils import get_menu_choice

def show_main_menu():
  """Display main menu options"""
  print("\n== CD Collection Manager ==")
  print("1. Add album")
  print("2. Edit album")
  print("3. Delete album")
  print("4. View albums by artist")
  print("5. Collection statistics")
  print("6. Exit")

def main():
  """Main program loop"""
  conn = connection()
  initialize(conn)

  while True:
    show_main_menu()
    choice = get_menu_choice(6)

    if choice == 1:
      add_album(conn)
    elif choice == 2:
      edit_album(conn)
    elif choice == 3:
      delete_album(conn)
    elif choice == 4:
      artist_id, name = show_or_add_artist(conn)
      view_by_artist(conn, artist_id)
    elif choice == 5:
      show_stats_menu(conn)
    elif choice == 6:
      print("Goodbye!")
      break

  conn.close()

# Run main program
if __name__ == "__main__":
  main()