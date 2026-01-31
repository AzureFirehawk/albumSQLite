"""
Main program file
Controls main program loop and routes user input to appropriate functions
"""

# Import modules
from connect import connection, initialize
from artists import select_artist
from albums import (
  add_album,
  edit_album,
  delete_album,
  view_by_artist
)
from stats import show_stats_menu
from utils import (get_menu_choice, prompt_continue)

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
      while True:
        add_album(conn)
        if not prompt_continue("Add another album? (y/n): "):
          break
    elif choice == 2:
      while True:
        edit_album(conn)
        if not prompt_continue("Edit another album? (y/n): "):
          break
    elif choice == 3:
      while True:
        delete_album(conn)
        if not prompt_continue("Delete another album? (y/n): "):
          break
    elif choice == 4:
      while True:
        artist_id = select_artist(conn)
        if not artist_id:
          break
        view_by_artist(conn, artist_id)
        if not prompt_continue("View albums for another artist? (y/n): "):
          break
    elif choice == 5:
      show_stats_menu(conn)
    elif choice == 6:
      print("Goodbye!")
      break

  conn.close()

# Run main program
if __name__ == "__main__":
  main()