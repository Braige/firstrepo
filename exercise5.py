"""
Exercise 5: Ticket Price by Age

Instructions:
- Create a variable called `age`.
- Use if/elif/else to:
    - Print "Child ticket" if age is less than 13.
    - Print "Teen ticket" if age is between 13 and 17 (inclusive).
    - Print "Adult ticket" if age is 18 or older.
"""

age = 16  # you can change this value

# Write your if/elif/else statements below:

if age < 13:
    print("Child ticket")
elif age < 18:
    print("Teen ticket")
else:
    print("Adult ticket")
