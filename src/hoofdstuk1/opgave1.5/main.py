# This file should be used to show the implementation of finance.py
# For instructions read the README.md
from finance import *

hobby = Grouping("Hobby")
travel_expenses = Grouping("Travel Expenses")
animals = Grouping("Animals")

hobby.deposit(500, "Maandgeld")
travel_expenses.deposit(1000, "Loon")
animals.deposit(1500, "Zwart werk")

hobby.withdraw(100)
hobby.withdraw(200)
hobby.withdraw(300)
travel_expenses.withdraw(300, "Hollywood")
travel_expenses.withdraw(150, "Genk")
travel_expenses.withdraw(800, "Malaga")
animals.withdraw(400, "Eten voor de hond en zijn puppy")
animals.withdraw(50, "Eten voor de buurman zijn kat")
animals.transfer(500, travel_expenses)
travel_expenses.withdraw(800, "NY")
animals.withdraw(200, "Dog house")

print(hobby)
print(travel_expenses)
print(animals)
