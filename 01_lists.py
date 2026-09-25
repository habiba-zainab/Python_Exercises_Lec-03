"""

===========================================================
   LECTURE 03 - SET 01 : BASICS OF LISTS
   Topics : List Basics - Creating, Accessing, & Operations
   Total Questions :  
============================================================

"""

# ==========================================================
# PART A:   List Creation & Types
# ==========================================================

# Q1: Create and display different types of lists
#    Create:
#    - Empty list
#    - List of 5 integers
#    - Lists of 3 strings (fruits)
#    - Lists with mixed data types
#    Print each with its length

print("\n--- Q1: Creating Lists ---")

empty = []
integers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'mango']
mixed = [1, 'hello', 25.5, True]

print("Empty:", empty, "(Length:", len(empty), ")")
print("Integers:", integers, "(Length:", len(integers), ")")
print("Fruits:", fruits, "(Length:", len(fruits), ")")
print("Mixed:", mixed, "(Length:", len(mixed), ")")

# ----------------------------------------------------------