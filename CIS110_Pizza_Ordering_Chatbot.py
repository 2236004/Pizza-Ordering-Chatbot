print("Hello, my name is Austin your virtual assistant. I will help you order a pizza!")
print("I am going to ask you a few questions. After typing an answer, press enter.")
username = input("\nEnter your name:  ")
print(f"\nHello, {username}. Nice to meet you!")

size = input("\nWhat size do you want? Enter small medium and large:  ")
flavor = input("\nEnter the flavor of the pizza:  ")
crusttype = input("\nWhat type of crust do you want:  ")
quantity = input("\nHow many of these do you want to order? Enter a numeric value:  ")
quantity = int(quantity)
method = input("\nIs this carryout or delivery:  ")

salestax = 1.1
pizzacost = 14.99
total = (pizzacost * quantity) * salestax
print(total)

print("-" * 10)
print(f"Thank you {username} for your order")
print(f"Your {quantity} {size} {flavor} pizza(s) with {crusttype} crust costs ${total:,.2f}.")
