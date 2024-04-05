'''
1. Tuple Mastery in Python
Objective:
The aim of this assignment is to deepen your understanding of tuples in Python, along with their interaction with lists, 
dictionaries, and basic Python functionalities like functions, input handling, and string formatting. 
By completing this assignment, you will enhance your skills in data structuring, manipulation, and application of tuples in practical scenarios.

Task 1: Formatting Flight Itineraries
Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: 
(traveler_name, origin, destination). The function should format and return a string that lists each itinerary. For example, 
if the input is [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")], the output should be a string formatted as:

"Itinerary 1: Alice - From New York to London
 Itinerary 2: Bob - From Tokyo to San Francisco"

'''
# 
# add user inputs to get name and locations 
# need to loop the tuple
# need to use enumerate for the count of itineraries 
# print out the itineraries in a nice format


def add(itinerary):

  name = input("Enter name of passenger: ").title()
  origin = input("Where are you coming from: ")
  going = input("Where are you going too: ")
  itinerary.append((name,(origin,going)))
  print(f"{name} from {origin} to {going} has been add to itinerary")


def view(itinerary):
  for count, name in enumerate(itinerary):
    print(f"Itinerary {count +1}: {name[0]} - From {name[1][0]} to {name[1][1]}") 


def main():
  print("Hello Welcome to the Flight Itinerary Maker. ")
  itinerary = []
  while True:
    print("\nMain Menu:\n1. Add Itinerary\n2. View Itinerary\n3. Exit")
    user_input = input("Select an option: ")
    if user_input == "1":
      add(itinerary)
      print
    elif user_input == "2":
      view(itinerary)
    elif user_input == "3":
      print("Thank you for using Flight Itinerary Maker! Good Bye.")
      break
    else:
      print("Invalid Input")


main()