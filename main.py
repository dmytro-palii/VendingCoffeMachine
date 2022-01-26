from creditcard import CreditCard
from vendingmachine import VendingMachine


    
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

some_credit_card = CreditCard(123321, 123, 10)
vending_machine = VendingMachine(menu_coffee, additional_menu, some_credit_card, supplies)

vending_machine.drink_cook()

