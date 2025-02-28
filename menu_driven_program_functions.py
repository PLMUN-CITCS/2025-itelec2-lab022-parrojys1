"""Run different functions based on user's choice"""
def display_functions():
    """Display options for the user to choose from"""
    print("Menu:")
    print("1. Greet User")
    print("2. Check Even/Odd")
    print("3. Exit")

def handle_menu_choice(x):
    """Handle the user's choice"""
    if x == 1:
        greet_user()
    elif x == 2:
        even_odd_checker_action()
    elif x == 3:
        print("Exiting Program. Goodbye!")
    else:
        print("Invalid choice")

def greet_user():
    """Greet the user"""
    print("Hello! Welcome!\n")

def even_odd_checker_action():
    """Check if a number is even or odd"""
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(f"{number} is an Even number.\n")
    else:
        print(f"{number} is an Odd number.\n")

if __name__ == "__main__":
    while True:
        display_functions()
        choice = int(input("Enter your choice (1-3): "))
        handle_menu_choice(choice)
        if choice == 3:
            break
