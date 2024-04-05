'''
2. Python Data Structure Challenges in Real-World Scenarios
Objective:
This assignment is designed to enhance your understanding and application of Python's core data structures - 
tuples, lists, and dictionaries - in real-world contexts. By engaging with these tasks, you will practice 
manipulating these data structures, applying built-in Python methods, and implementing error handling in practical situations.

Task 1: Library System Enhancement
Sharpen your skills in managing and modifying data within tuples and lists.

Problem Statement:
You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this 
system by adding new books and ensuring no duplicates.

Existing Library Data:

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
Add functionality to insert new books into library.
Ensure that adding a duplicate book is handled appropriately.
'''


def add(library):
  name_of_book = input("Enter the name the book: ").title()
  author = input("Enter the Author: ").title()
  found = [book for book in library if book[0].lower() == name_of_book.lower()]
  if found:
    print("That Book is already in our library")
  else:
    library.append((name_of_book,author))
    


def main():
  library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
  print("Welcome to L.M.S (Library Management System)")
  while True:
    print("\nMain Menu:\n1. Add Books\n2. Exit")
    user_input = input("Enter your choice: ")
    if user_input == "1":
      add(library)
    elif user_input == "2":
      print("Thank you for using L.M.S")
      break
    else:
      print("Invalid Input") 

main()   

