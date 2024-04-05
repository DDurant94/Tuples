'''
5. Advanced Tuple Techniques: Joining and Nesting in Python
Objective:
This assignment is designed to advance your understanding and application of joining and nesting tuples in Python. 
You will engage in tasks that require organizing and manipulating complex data structures, improving your 
problem-solving skills in handling multi-dimensional data.

Task 1: Product Catalog Merging
Utilize tuple joining to combine multiple product catalogs.

Problem Statement:
You are managing the product catalogs for an online store. Each catalog is a tuple of products, and each 
product is a tuple containing the product name and price. Merge multiple catalogs into a single tuple.

Write a function to join two or more product catalogs into one.
Display the combined catalog, ensuring that it maintains the order of products as they were in their original catalogs.
Example Catalogs:

catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))
'''


def adding_catalogs(*catalog):
  new_catalog = ()
  for items in catalog:
    new_catalog+=items
  for count, item in enumerate(new_catalog):
    print(f"{count + 1}. {item[0]}: cost ${item[1]}")





catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))

def main():
  print("Welcome to Joining Catalogs")
  while True:
    print("\nMain Menu:\n1. Join Catalogs\n2. Exit")
    user_input = input("Enter your choice: ")
    if user_input == "1":
      adding_catalogs(catalog1,catalog2)
    elif user_input == "2":
      print("Good Bye")
      break
    else:
      print("Invalid Input") 


main()