
class VendingMachine:
    credit_card_data = {123321: 123}
    
    def __init__(self, coffee_menu: dict, addidtional_menu: dict, some_credit_card: CreditCard, supplies: dict):
        self.coffee_menu = coffee_menu
        self.addidtional_menu = addidtional_menu
        self.supplies = supplies

    def get_drinks_names_lst(self):

        return list(self.coffee_menu.keys())

    def print_menu(self):
        drink_menu_name = self.get_drinks_names_lst()

        for drink_number, drink in enumerate(drink_menu_name, 1):
            print(f"{drink_number}. {drink.title()}")

    def selected_drink(self):
        drink_number = int(input("Please select your drink: "))
        drink_menu_name = self.get_drinks_names_lst()
        return drink_menu_name[drink_number - 1]

    def drink_cook(self):
        self.print_menu()
        print(self.selected_drink())

#следующий шаг, проверка и списаниe базовых ингридиентов


menu_coffee = {"Espresso" : {"price" : 1.25, 
                          "water" : 50, 
                          "coffee" : 18,                        
                          "milk" : 0},

                "Latte" : {"price" : 2.25, 
                            "water" : 200,  
                            "coffee" : 150, 
                            "milk" : 24},      
                                
                "Cappucino" : {"price" : 3.25, 
                                "water" : 250,  
                                "coffee" : 100, 
                                "milk" : 24}}
                            


additional_menu = {"sugar" : 1.00, "milk" : 1.25}

supplies = {"water"  : 300,
                         "coffee" : 200,
                         "milk"   : 100}

some_credit_card = CreditCard(123321, 123)
vending_machine = VendingMachine(menu_coffee, additional_menu, some_credit_card, supplies)


vending_machine.drink_cook()