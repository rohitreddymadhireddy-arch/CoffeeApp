class CoffeeMachine:

    def __init__(self):
        self.menu = {
            "espresso": 50,
            "latte": 80,
            "cappuccino": 100
        }

    def show_menu(self):
        print("\nCoffee Menu")
        print("-----------")

        for item in self.menu:
            print(item.title(), "- ₹", self.menu[item])

    def order(self):
        coffee = input("Enter coffee name: ").lower()

        if coffee in self.menu:
            amount = int(input("Enter amount: ₹"))

            if amount >= self.menu[coffee]:
                print("Your", coffee.title(), "is ready.")

                change = amount - self.menu[coffee]
                print("Change: ₹", change)
            else:
                print("Not enough money.")
        else:
            print("Coffee is not available.")


machine = CoffeeMachine()

while True:
    machine.show_menu()
    machine.order()

    choice = input("\nDo you want another coffee? (yes/no): ").lower()

    if choice != "yes":
        print("Thank you. Visit again!")
        break