class BankManagementSystem:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer_id, name, balance):
        self.customers[customer_id] = {'Name': name, 'Balance': balance}
        print(f"Customer {name} added successfully!")

    def view_customer(self, customer_id):
        customer = self.customers.get(customer_id)
        if customer:
            print(f"Customer ID: {customer_id}")
            for key, value in customer.items():
                print(f"{key}: {value}")
        else:
            print(f"Customer with ID {customer_id} not found.")

    def search_customer(self, name):
        found_customers = [(customer_id, customer) for customer_id, customer in self.customers.items() if name.lower() in customer['Name'].lower()]
        if found_customers:
            for customer_id, customer in found_customers:
                print(f"Customer ID: {customer_id}, Name: {customer['Name']}, Balance: {customer['Balance']}")
        else:
            print(f"No customers found with the name {name}.")

    def view_all_customers(self):
        if self.customers:
            for customer_id, customer in self.customers.items():
                print(f"Customer ID: {customer_id}, Name: {customer['Name']}, Balance: {customer['Balance']}")
        else:
            print("No customers in the bank.")

    def total_amount_in_bank(self):
        total_amount = sum(customer['Balance'] for customer in self.customers.values())
        print(f"Total amount in the bank: {total_amount}")


class CustomerApp:
    def __init__(self, bank_system):
        self.bank_system = bank_system
        self.customer_id = None

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def withdraw_amount(self, amount):
        if self.customer_id in self.bank_system.customers:
            if amount > 0 and amount <= self.bank_system.customers[self.customer_id]['Balance']:
                self.bank_system.customers[self.customer_id]['Balance'] -= amount
                print(f"Withdrawal of {amount} successful. Updated balance: {self.bank_system.customers[self.customer_id]['Balance']}")
            else:
                print("Invalid withdrawal amount.")
        else:
            print("Customer not found.")

    def deposit_amount(self, amount):
        if self.customer_id in self.bank_system.customers:
            if amount > 0:
                self.bank_system.customers[self.customer_id]['Balance'] += amount
                print(f"Deposit of {amount} successful. Updated balance: {self.bank_system.customers[self.customer_id]['Balance']}")
            else:
                print("Invalid deposit amount.")
        else:
            print("Customer not found.")

    def view_balance(self):
        if self.customer_id in self.bank_system.customers:
            print(f"Current balance: {self.bank_system.customers[self.customer_id]['Balance']}")
        else:
            print("Customer not found.")


def main():
    bank_system = BankManagementSystem()
    customer_app = CustomerApp(bank_system)

    while True:
        print("\nWELCOME TO PYTHON BANK MANAGEMENT SYSTEM")
        print("Select your role:")
        print("1) Banker")
        print("2) Customer")
        print("3) Exit")

        role_choice = input("Enter your choice: ")

        if role_choice == '1':
            while True:
                print("\nBanker Menu:")
                print("1) Add Customer")
                print("2) View Customer")
                print("3) Search Customer")
                print("4) View All Customers")
                print("5) Total Amount in Bank")
                print("6) Back to Main Menu")

                banker_choice = input("Enter your choice: ")

                if banker_choice == '1':
                    customer_id = input("Enter Customer ID: ")
                    name = input("Enter Customer Name: ")
                    balance = float(input("Enter Initial Balance: "))
                    bank_system.add_customer(customer_id, name, balance)
                elif banker_choice == '2':
                    customer_id = input("Enter Customer ID: ")
                    bank_system.view_customer(customer_id)
                elif banker_choice == '3':
                    name = input("Enter Customer Name to search: ")
                    bank_system.search_customer(name)
                elif banker_choice == '4':
                    bank_system.view_all_customers()
                elif banker_choice == '5':
                    bank_system.total_amount_in_bank()
                elif banker_choice == '6':
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif role_choice == '2':
            customer_id = input("Enter Your Customer ID: ")
            if customer_id in bank_system.customers:
                customer_app.set_customer_id(customer_id)
                while True:
                    print("\nCustomer's Menu:")
                    print("1) Withdraw Amount")
                    print("2) Deposit Amount")
                    print("3) View Balance")
                    print("4) Back to Main Menu")

                    customer_choice = input("Enter your choice: ")

                    if customer_choice == '1':
                        amount = float(input("Enter withdrawal amount: "))
                        customer_app.withdraw_amount(amount)
                    elif customer_choice == '2':
                        amount = float(input("Enter deposit amount: "))
                        customer_app.deposit_amount(amount)
                    elif customer_choice == '3':
                        customer_app.view_balance()
                    elif customer_choice == '4':
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Customer not found.")
        elif role_choice == '3':
            print("Exiting Bank Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
