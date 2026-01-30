"""
Utility functions
"""

def get_menu_choice(max_choice, prompt="Select an option: "):
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