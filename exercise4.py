"""
Exercise 4: Simple Login Check

Instructions:
- Create two variables:
    - `username`
    - `password`
- Use an if/else statement to:
    - Print "Access granted" if username is "admin" AND password is "secret123".
    - Print "Access denied" for anything else.

Hints:
- Use `==` to compare values.
- Use `and` to require both conditions to be True.
"""

username = "admin"      # you can change this value
password = "secret123"  # you can change this value

# Write your if/else statement below:
username = "admin"
password = "secret123"

if username == "admin" and password == "secret123":
        print("Access granted")
else:
    print("Access denied")