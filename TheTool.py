def calculate_remaining_balance(payment, expenses):
    remaining_balance = payment
    summary = []

    for expense_name, expense_amount in expenses.items():
        remaining_balance -= expense_amount
        summary.append(f"After {expense_name}, remaining balance: {remaining_balance:.2f}")

    security_savings = remaining_balance * 0.20
    remaining_balance -= security_savings

    summary.append("\nSummary:")
    summary.append(f"Initial payment: {payment:.2f}")
    summary.append("Expenses:")
    for expense_name, expense_amount in expenses.items():
        summary.append(f"{expense_name}: {expense_amount:.2f}")
    summary.append(f"Security savings: {security_savings:.2f}")
    summary.append(f"Remaining balance: {remaining_balance:.2f}")

    return summary

def main():
    try:
        payment = float(input("Enter the initial payment amount: "))
    except ValueError:
        print("Please provide a valid number for the amount of money.")
        return

    expenses = {}
    while True:
        expense_name = input("Enter the name of the expense (or type 'done' to finish): ")
        if expense_name.lower() == 'done':
            break
        try:
            expense_amount = float(input("Enter the amount for this expense: "))
        except ValueError:
            print("Please provide a valid number for the amount of money.")
            continue
        expenses[expense_name] = expense_amount

    summary = calculate_remaining_balance(payment, expenses)

    for line in summary:
        print(line)

if __name__ == "__main__":
    main()
