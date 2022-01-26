from creditcard import CreditCard

class VendingMachine:
    credit_card_data = {123321: 123, 456654: 768}
    
    def __init__(self, coffee_menu: dict, addidtional_menu: dict, some_credit_card: CreditCard, supplies: dict):
        self.coffee_menu = coffee_menu
        self.addidtional_menu = addidtional_menu
        self.supplies = supplies
        self.some_credit_card = some_credit_card

    def get_drinks_names_lst(self):

        return list(self.coffee_menu.keys())

    def print_menu(self):
        drink_menu_name = self.get_drinks_names_lst()

        for drink_number, drink in enumerate(drink_menu_name, 1):
            print(f"{drink_number}. {drink.title()}")

    def get_drink_number(self):
        drink_number = int(input("Please select your drink: "))
        return drink_number
    
    def check_drink_number(self, drink_number: int):
        if 1 <= drink_number <= len(self.coffee_menu):
            return True

        print("Incorrect choice")
        return False

    def selected_drink(self, drink_number: int):
        # drink_number = self.get_drink_number() - вызовёт повторный ввод
        drink_menu_name = self.get_drinks_names_lst()
        return drink_menu_name[drink_number - 1]

    def check_supplies(self, selected_drink):
        selctted_drink_supplies = self.coffee_menu[selected_drink]

        for ingredient, num in selctted_drink_supplies.items():
            if ingredient in self.supplies:
                if num > self.supplies[ingredient]:
                    print(f"Not enough supplies: {ingredient}")
                    return False

        return True

    def minus_supplies(self, selected_drink):
        selctted_drink_supplies = self.coffee_menu[selected_drink]

        for ingredient, num in selctted_drink_supplies.items():
            if ingredient in self.supplies:
                self.supplies[ingredient] -= num
                # print(f"{ingredient} is decreased by {num}")

        # print(self.supplies)

    def check_card_validation(self):
        pin_code_input = int(input("Please input your pin code: "))
        for number, pin_number in self.credit_card_data.items():
            if number == self.some_credit_card.card_number:
                if self.some_credit_card.card_pin_num == pin_code_input:
                    return True
                    
        print("Card is not valid")
        return False

    def check_card_balance(self, selected_drink):
        if self.some_credit_card.card_blance >= self.coffee_menu[selected_drink]["price"]:
            return True

        print("You don't have enough money")
        return False

    def minus_card_balance(self, selected_drink):
        self.some_credit_card.card_blance -= self.coffee_menu[selected_drink]["price"]
        # print(self.some_credit_card.card_blance)

    def drink_can_be_cooked(self):
        drink_number = self.get_drink_number()
        if self.check_drink_number(drink_number):
            drink = self.selected_drink(drink_number)
            if self.check_supplies(drink):
                if self.check_card_validation():
                    if self.check_card_balance(drink):
                        self.minus_supplies(drink)
                        self.minus_card_balance(drink)
                        print(f"Your {drink} is ready! Enjoy ☕️")


    def drink_cook(self):
        self.print_menu()
        self.drink_can_be_cooked()

