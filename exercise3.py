"""
Exercise 3: Score to Grade

Instructions:
- Create a variable called `score` with a number from 0 to 100.
- Use if/elif/else to:
    - Print "Pass" if score is 60 or higher.
    - Print "Fail" if score is less than 60.

Extra (optional):
- Instead of just "Pass", you can print:
    - "Excellent" if score is 90 or higher
    - "Good" if score is 75–89
    - "Pass" if score is 60–74
    - "Fail" otherwise
"""

score = 92  # you can change this value

# Write your if/elif/else statements below:


if score >=90:
    print("Excellent")
elif score >= 75:
    print("Good")
elif score >= 60:
    print("Pass")
else:
    print("Fail")