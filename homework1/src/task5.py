"""
Task 5: Lists and Dictionaries
Create a new file named task5.py and inside create a list of your favorite books, including book
titles and authors. Use list slicing to print the first three books in the list. Create a dictionary that
represents a basic student database, including student names and their corresponding student IDs.
Implement pytest test cases to verify the correctness of your code for each data structure.
"""

# List containing favorite book names and authors in tuples
fav_books = [("1984", "George Orwell"), ("Algorithms to Live By", "Brian Christian and Tom Griffiths"), ("Paper Towns", "John Green"), ("Everything Everything", "Nicola Yoon"), ("Percy Jackson & the Olympians: The Lightning Thief", "Rick Riordan")]
# Printing the first three books using list slicing
print(fav_books[0:3])

# Student database held in a dictionary
student_data = {'Avalee Cruz': '0000', 'Isabel Rivera': '0101', 'Jackson Seales': '3005', 'Addy Rohr': '2004', 'Senna Smoak': '0123', 'John Smith': '1968'}