"""
Utility functions
"""

def get_menu_choice(max_choice, prompt="\nSelect an option: "):
  """
  Prompt user for menu choice
  """
  while True:
    choice = input(prompt).strip()
    try:
      if not choice.isdigit():
        print ("Please enter a number.")
        continue

      choice = int(choice)
      if choice < 1 or choice > max_choice:
        raise ValueError

      return choice
    except ValueError:
      print(f"Please enter a number between 1 and {max_choice}.")

def prompt_continue(message="\nDo you want to continue? (y/n): ", default=True):
  """
  Prompt user to continue or exit a loop
  Returns: True if user wants to continue, False if not
  """
  yes_options = ('y', 'yes')
  no_options = ('n', 'no')

  while True:
    choice = input(message).strip().lower()
    if not choice:
      return default
    elif choice in yes_options:
      return True
    elif choice in no_options:
      return False
    else:
      print("Please enter 'y' or 'n'.")

def prompt_edit_value(field_name, current_value):
  value = input(f"{field_name} (blank to keep '{current_value}'): ").strip()
  return value.title() if value else current_value