def add_expense(expenses, amount, category):
    expenses.append({"amount": amount, "category": category})
    print(f"Expenses {expenses[len(expenses)-1]} added successfully")


def print_expenses(expenses):
    for expense in expenses:
        print(f"Amount: {expense['amount']}\nCategory: {expense['category']}\n")


def expenses_total(expenses):
    return sum(map(lambda expense: expense["amount"], expenses))


def filter_by_category(expenses, category):
    return filter(lambda expense: expense["category"] == category, expenses)


def main():
    expenses = []

    while True:
        print("1. Add an Expense\t2. View expenses\t3. Get Total Amount\t4. Filter by category\t5. Quit")
        answer = input(": ")

        if answer == "1":
            amount = float(input("Enter Amount: "))
            category = input("Enter Category: ")
            add_expense(expenses, amount, category)
        elif answer == "2":
            print_expenses(expenses)
        elif answer == "3":
            print("Total: ", expenses_total(expenses))
        elif answer == "4":
            category = input("Enter Category: ")
            print_expenses(filter_by_category(expenses, category))
        else:
            break


if __name__ == "__main__":
    main()