import os
import time
import random

# Function to add colors
def colored_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

# Function to clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to print ASCII art with dynamic color change
def print_ascii_art():
    colors = ['1;31', '1;32', '1;33', '1;34', '1;36']  # Red, Green, Yellow, Blue, Cyan
    art_lines = [
        '██████╗ ██╗   ██╗███████╗██╗██╗     ██╗███████╗',
        '██╔═══██╗██║   ██║██╔════╝██║██║     ██║██╔════╝',
        '██║   ██║██║   ██║███████╗██║██║     ██║███████╗',
        '██║▄▄ ██║██║   ██║╚════██║██║██║     ██║╚════██║',
        '╚██████╔╝╚██████╔╝███████║██║███████╗██║███████║',
        ' ╚══▀▀═╝  ╚═════╝ ╚══════╝╚═╝╚══════╝╚═╝╚══════╝'
    ]

    for line in art_lines:
        color = random.choice(colors)
        print(colored_text(line, color))

# Function to animate the dancing raccoon
def dance_raccoon():
    frame_top = "       \033[1;36m.--.\033[0m"
    frame_side = "     \033[1;36m/ .-. \\\033[0m"
    frame_bottom = "       \033[1;36m'--'\033[0m"

    raccoon_actions = [
        """
      /\\___/\\
     ( o.o   ) nom nom
     (  =^=  )
     (      )
     (         )
     (          )))))))))))
    """,
        """
      /\\___/\\
     ( o.o   )
     (  =^.^= )
     (  \"w\"   )
    (( _/) (( _/)
    """,
        """
      /\\___/\\
     ( o.O   )
     (  =   = )
     (   \" \"   )
     (         )
     (          )
    """
    ]

    colors = ['\033[1;31m', '\033[1;33m', '\033[1;32m', '\033[1;34m', '\033[1;36m']  # Red, Yellow, Green, Blue, Cyan
    sounds = ['*munch* *munch*', 'Bop it! Twist it! Pull it!', 'ZZzzzZZzz...', 'Woo-hoo!', 'Yippee!']

    try:
        while True:
            clear_screen()
            print(frame_top)
            print(frame_side)

            # Randomly choose a raccoon pose and its corresponding color
            raccoon_pose = random.choice(raccoon_actions)
            raccoon_color = random.choice(colors)
            print(raccoon_color + raccoon_pose + '\033[0m')

            print(frame_side)
            print(frame_bottom)

            # Play a random sound effect corresponding to the raccoon's action
            print(colored_text(random.choice(sounds), '1;33'))  # Yellow color for sound effect

            time.sleep(0.5)  # Wait for half a second

    except KeyboardInterrupt:
        pass

# Function to get detailed expense amount
def get_detailed_expense_amount(expense_name):
    while True:
        try:
            unit_cost = float(input(styled_text(f"What’s the cost per {expense_name} item, my friend? ", 'prompt')))
            quantity_per_day = int(input(styled_text(f"How many {expense_name}s do you fancy each day? ", 'prompt')))
            days = int(input(styled_text(f"For how many days will you be enjoying those {expense_name}s? ", 'prompt')))
            return unit_cost * quantity_per_day * days
        except ValueError:
            print(styled_text("Ah, seems like you entered something unusual. Please give me numbers I can understand.", 'error'))

# Function to calculate remaining balance and generate summary
def calculate_remaining_balance(payment, expenses):
    remaining_balance = payment
    summary = []

    total_expense = sum(expense_amount for expense_amount in expenses.values())
    remaining_balance -= total_expense

    security_savings = remaining_balance * 0.20
    remaining_balance -= security_savings

    summary.append(styled_text("Here’s your summary, with a touch of class:", 'section_heading'))
    summary.append(f"Initial payment: {colored_text(f'{payment:.2f}', '1;32')}")
    summary.append(styled_text("Your Expenses:", 'section_heading'))
    for expense_name, expense_amount in expenses.items():
        summary.append(f"  {expense_name}: {colored_text(f'{expense_amount:.2f}', '1;31')}")
    summary.append(f"Total expenses: {colored_text(f'{total_expense:.2f}', '1;31')}")
    summary.append(f"Security savings: {colored_text(f'{security_savings:.2f}', '1;33')}")
    summary.append(f"Remaining balance: {colored_text(f'{remaining_balance:.2f}', '1;32')}")

    return summary

# Function to style text based on type
def styled_text(text, style):
    styles = {
        'title': f"\033[1;36m{text}\033[0m",  # Cyan color, bold
        'section_heading': f"\033[1;34m{text}\033[0m",  # Blue color, bold
        'prompt': f"\033[1;32m{text}\033[0m",  # Green color, bold
        'error': f"\033[1;31m{text}\033[0m"  # Red color, bold
    }
    return styles.get(style, text)

# Function to get the initial payment
def get_initial_payment():
    while True:
        try:
            return float(input(styled_text("Hello! What’s your initial payment to get started? ", 'prompt')))
        except ValueError:
            print(styled_text("Hmm, that doesn’t look like a number. Try again, please.", 'error'))

# Function to get the expense name
def get_expense_name():
    return input(styled_text("What’s the name of your expense? Or type 'done' if you’re finished: ", 'prompt')).strip()

# Function to get the expense amount
def get_expense_amount(expense_name):
    while True:
        try:
            return float(input(styled_text(f"How much are you spending on {expense_name} in total? ", 'prompt')))
        except ValueError:
            print(styled_text("I need a number here, please.", 'error'))

# Function to get expenses from the user
def get_expenses():
    expenses = {}
    while True:
        expense_name = get_expense_name()
        if expense_name.lower() == 'done':
            break
        detailed_entry = input(styled_text("Would you like to provide detailed info? (y/n, press Enter for 'no'): ", 'prompt')).strip().lower()
        if detailed_entry == 'y':
            expense_amount = get_detailed_expense_amount(expense_name)
        else:
            expense_amount = get_expense_amount(expense_name)
        expenses[expense_name] = expense_amount
    return expenses

# Function to display the summary
def display_summary(payment, expenses):
    summary = calculate_remaining_balance(payment, expenses)
    for line in summary:
        print(line)

# Main function to run the program
def main():
    clear_screen()
    print_ascii_art()
    print(styled_text("Welcome to the Cool Expense Tracker!", 'title'))
    print(styled_text("Enter your initial payment, then add your expenses.", 'title'))
    print(styled_text("Type 'done' when you have finished adding expenses.", 'title'))
    print(styled_text("You can choose to enter detailed expense information if you prefer.\n", 'title'))

    payment = get_initial_payment()
    expenses = get_expenses()
    clear_screen()
    display_summary(payment, expenses)

    print("\nPress Enter to see a dancing raccoon with the final result!")
    input()
    dance_raccoon()

if __name__ == "__main__":
    main()