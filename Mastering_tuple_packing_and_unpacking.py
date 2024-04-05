'''
4. Mastering Tuple Packing and Unpacking in Python
Objective:
The goal of this assignment is to deepen your understanding of tuple packing and unpacking in Python. 
You will apply these techniques in various practical scenarios, enhancing your ability to work with flexible 
data structures and improve data handling efficiency.

Task 1: Customer Order Processing
Refine your skills in tuple unpacking by managing customer orders.

Problem Statement:
You are given a list of tuples, each representing a customer's order. Each tuple contains the customer's name, 
the product ordered, and the quantity. Your task is to unpack each tuple and print the order details in a user-friendly format.

Sample Order Data:

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]
Write a function to iterate over the list of orders.
Unpack each tuple in the list and format the details for display.

Task 2: Sorting and Filtering Contact Information
Implement tuple packing and unpacking in sorting and filtering tasks.

Problem Statement:
You have a list of contacts, where each contact is represented as a tuple containing a name, email, and phone number. Your task is to:

Sort the contacts by name.
Filter and display contacts whose names start with a specific letter.
Sample Contact Data:

contacts = [
    ("Alice", "alice@email.com", "123-456-7890"),
    ("Bob", "bob@email.com", "234-567-8901"),
    # More contacts...
]
'''

# Task One

def customer_orders(orders):
  for order in orders:
    person, item, quantity = order
    print(f"\n{person}: Ordered {quantity} {item}")
      
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
]

def main():
  print("Welcome to Customer Order Tracker")
  while True:
    print("\nMain Menu:\n1. Customer orders\n2. Exit")
    user_input = input("Enter your choice: ")
    if user_input == "1":
      customer_orders(orders)
    elif user_input == "2":
      print("Thank you for using Customer Order Tracker")
      break
    else:
      print("Invalid Input") 

main()

# Task Two


def sorted_contacts(contacts):
  user_sorted_contacts = []
  user_input = input("What letter would you like to sort contacts by: ").upper()
  for contact in contacts:
    if user_input == contact[0][0]:
      user_sorted_contacts.append(contact)
      for info in user_sorted_contacts:
        print(f"{info[0]}: Email Address '{info[1]}', Phone Number '{info [2]}'")

     


contacts = [
    ("Alice", "alice@email.com", "123-456-7890"),
    ("Bob", "bob@email.com", "234-567-8901"),
]

def main():
  print("Welcome to Personal Contract Sorting")
  while True:
    print("\nMain Menu:\n1. Sort Contacts\n2. Exit")
    user_input = input("Enter your choice: ")
    if user_input == "1":
      sorted_contacts(contacts)
    elif user_input == "2":
      print("Thank you for using Personal Contract Sorting")
      break
    else:
      print("Invalid Input") 

main()