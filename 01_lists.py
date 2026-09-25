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

# Q2: List with range() function
#    Create lists using range():
#    - Numbers from 1 to 10
#    - Even numbers from 0 to 20
#    - Numbers from 50 to 10 (descending, step -5)
#    - Multiples of 3 from 3 to 30

print("\n--- Q2: Lists with range() ---")

range1 = list(range(1, 11))
print("1 to 10:", range1)

range2 = list(range(0, 21, 2))
print("Even 0-20:", range2)

range3 = list(range(50, 9, -5))
print("50 to 10 (step -5):", range3)

range4 = list(range(3, 31, 3))
print("Multiples of 3:", range4)

# ----------------------------------------------------------

# ==========================================================
# PART B:   List Indexing
# ==========================================================

#    ***** Positive Indexing *****

# Q3: Access list elements using positive indexing
#    Given: colors = ["red", "green", "blue", "yellow",
#           "purple"]
#    Print:
#    - First color (index 0)
#    - Third color (index 2)
#    - Last color (index 4)