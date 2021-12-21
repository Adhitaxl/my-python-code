"""
All the basic syntax of a programming language consists of:
1. sequential: sequential steps
2. branching: jump step if condition is met
3. looping: repeating the same steps many times until the condition is met
"""

# Sequential
print('Mom said, "go to the store"')
print('Budi replied, "Ok what should I do go to the store"')
print('Mother answered, "Buy 1 bottle of milk, and buy 6 eggs"')
print('Budi replied, "OK"')
print("So Budi went to the store, and started shopping")

# Branching
number_of_milk_bottles = 50
number_of_eggs = 20
print(f"number of bottles of milk { number_of_milk_bottles} bottles")
print(f"number of eggs {number_of_eggs} eggs ")

if number_of_milk_bottles > 0:
     print("Budi checked the price, and found that he had enough money")
     print("Budi bought 1 bottle of milk")
if number_of_eggs == 0:
     print("Budi checked the price, and there was still enough money")
     print("Budi bought 6 eggs")
else:
     print("Budi buys everything Mom ordered")
     print("Buddy go home")
     print("Submit the result to mother")


