# TheTool.py

## Overview

TheTool.py is a Python script designed to help manage finances by calculating the remaining balance after deducting user-defined expenses from an initial payment. It also allocates 20% of the remaining balance to security savings.

## Features

- **Interactive Input**: Allows users to input the initial payment amount and dynamically add expenses.
- **Flexible Expense Calculation**: Deducts user-defined expenses from the initial payment.
- **Security Savings**: Allocates 20% of the remaining balance to security savings.
- **Detailed Summary**: Displays a summary including initial payment, deducted expenses, security savings, and remaining balance.

## How to Use

1. **Clone the Repository** (if applicable):
   ```bash
   git clone https://github.com/Kevi-cyber-beep/kevigjonaj.git
   cd kevigjonaj
  
   run the script:
   python TheTool.py

2.
Input Instructions:

    Enter the initial payment amount when prompted.
    Follow the prompts to enter each expense name and amount. Type 'done' when finished entering expenses.

 Example:

Enter the initial payment amount: 50000
Enter the name of the expense (or type 'done' to finish): Rent
Enter the amount for this expense: 11000
Enter the name of the expense (or type 'done' to finish): Internet
Enter the amount for this expense: 1500
Enter the name of the expense (or type 'done' to finish): Food
Enter the amount for this expense: 18200
Enter the name of the expense (or type 'done' to finish): done

  output:

After Rent, remaining balance: 39000.00
After Internet, remaining balance: 37500.00
After Food, remaining balance: 19300.00

Summary:
Initial payment: 50000.00
Expenses:
Rent: 11000.00
Internet: 1500.00
Food: 18200.00
Security savings: 6130.00
Remaining balance: 19300.00

(Notes)
Notes:

    Ensure all input values are numeric to avoid errors.
    The script dynamically calculates the remaining balance based on user-provided expenses.
