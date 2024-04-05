'''
3. Python Loops and Tuples in Analytical Applications
Objective:

This assignment is designed to strengthen your expertise in using Python loops and tuples, particularly 
in data analysis and processing scenarios. By completing these tasks, you will gain practical experience in handling 
and analyzing data using these fundamental Python concepts.

Task 1: Stock Market Data Analysis
Enhance your skills in data manipulation and analysis using tuples and loops.

Problem Statement:
You have been provided with stock market data, where each data point is a tuple containing a company's stock symbol, 
the date, and the closing price. Your task is to analyze this data to find the average closing price of a specified stock over a given period.

Sample Data:

stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    # More data...
]

Create a function to calculate the average closing price of a specific stock symbol over all dates.
Ensure your solution handles cases where the stock symbol does not exist in the data.


Task 2: Event Attendance Tracker
Apply loops and tuples to track and report on event attendance.

Problem Statement:
Your goal is to manage an attendance system for various events. Each attendee's data is stored as a tuple 
containing their name and the event they attended.

Develop a function to list all attendees of a specific event.
Implement a feature to count the number of attendees for each event.
Example Attendee Data:

attendees = [
    ("Alice", "Python Conference"),
    ("Bob", "Python Conference"),
    ("Charlie", "AI Summit"),
    # More attendees...
]
'''


#Task one

def average_stock_price(stock_data):
  days_selected_data = []
  user_choice = input("Enter the date you want to use: YYYY-MM-DD: ")
  days_selected = [stock for stock in stock_data if stock[1] == user_choice]
  if days_selected:
    days_selected_data.append((days_selected))
    sum_data = sum(avg[2] for avg in days_selected)
    average = sum_data / len(days_selected)
    print(f"The average price for {user_choice} is ${average}")
  else:
    print("Date Not Found")


stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
]

def main():
  print("Welcome to S.D.A (Stock Data Analysis)")
  while True:
    print("\nMain Menu:\n1. Average Stock price\n2. Exit")
    user_input = input("Enter your choice: ")
    if user_input == "1":
      average_stock_price(stock_data)
    elif user_input == "2":
      print("Thank you for using S.D.A")
      break
    else:
      print("Invalid Input") 

main()


# Task Two


def attendance_tracker(attendees):
  event_counter = 0
  found_event = []
  user_choice = input("Enter the event: ").title()
  tracked_event = [event for event in attendees if event[1].lower() == user_choice.lower()]
  if tracked_event:
    found_event.append((tracked_event))
    print(f"\nPeople that attended {user_choice}:")
    
    for people in found_event:
      for count, person in enumerate(people):
        event_counter += 1 
        print(f"{count +1 }. {person[0]}")
    print(f"The total amount of people at '{user_choice}' was '{event_counter}' people!")
  else:
    print("Event not found")

attendees = [
    ("Alice", "Python Conference"),
    ("Bob", "Python Conference"),
    ("Charlie", "AI Summit"),
]



def main():
  print("Welcome to Attendance Tracker")
  while True:
    print("\nMain Menu:\n1. Check Attendance\n2. Exit")
    user_input = input("Enter your choice: ")
    if user_input == "1":
      attendance_tracker(attendees)
    elif user_input == "2":
      print("Thank you for using Attendance Tracker")
      break
    else:
      print("Invalid Input") 


main()