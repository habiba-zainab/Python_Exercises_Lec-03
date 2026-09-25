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
#    Given: colors = ["red", "mint green", "blue", 
#           "burgundy", "maroon"]
#    Print:
#    - First color (index 0)
#    - Third color (index 2)
#    - Last color (index 4)

print("\n--- Q3: Positive Indexing ---")

colors = ["red", "mint green", "blue", "burgundy", "maroon"]

print("Colors:", colors)
print("First color:", colors[0])
print("Third color:", colors[2])
print("Last color:", colors[4])

# ----------------------------------------------------------

#    ***** Negative Indexing *****

# Q4: Access list elements using negative indexing
#    Given: numbers = [10, 20, 30, 40, 50]
#    Print:
#    - Last element (index -1)
#    - Second last element (index -2)
#    - First element using negative index (index -5)

print("\n--- Q4: Negative Indexing ---")

numbers = [10, 20, 30, 40, 50]

print("Numbers:", numbers)
print("Last element:", numbers[-1])
print("Second last element:", numbers[-2])
print("First element (using -5):", numbers[-5])

# ----------------------------------------------------------

# ==========================================================
# PART C:   List Modification & Operations
# ==========================================================

#    ***** List Modification *****

# Q5: Modify list elements
#   Given: grades = [85, 90, 78, 92, 88]
#   Modify:
#   - Change first grade to 95
#   - Change last grade to 90
#   - Change grade at index 2 to 80
#   Print list after each change

print("\n--- Q5: Modifying Elements ---")

grades = [85, 90, 78, 92, 88]
print("Original:", grades)

grades[0] = 95
print("After first change:", grades)

grades[-1] = 90
print("After last change:", grades )

grades[2] = 80
print("After middle change:", grades)

# ----------------------------------------------------------

#    ***** List Operations *****

# Q6: List concatenation and repetition
#   Given: list1 = [1, 2, 3]
#          list2 = [4, 5, 6]
#   Perform: 
#   - Concatenate list1 and list2
#   - Repeat list1 three times
#   - Create list3 combining list1 + list2 + list1

print("\n--- Q6: Concatenation and repition ---")

list1 = [1, 2, 3]
list2 = [4, 5, 6]

print("list1:", list1)
print("list2:", list2)
print("Concatenated:", list1 + list2)
print("list1 * 3:", list1 * 3)

list3 = list1 + list2 + list1
print("list3:", list3)

# ----------------------------------------------------------

# Q7: Membership operators (in, not in)
#   Given: fruits = ["apple", "mango", "cherry", "date"]
#   Check:
#   - Is "mango" in the list?
#   - Is "banana" in the list?
#   - Is "grape" not in the list?

print("\n--- Q7: Membership Operators ---")

fruits = ["apple", "mango", "cherry", "date"]

print("Fruits:", fruits)
print("'mango' in fruits:", 'mango' in fruits)
print("'banana' in fruits:", 'banana' in fruits)
print("'grape' not in fruits:", 'grape' not in fruits)

# ----------------------------------------------------------

# ==========================================================
# PART D:   Nested Lists
# ==========================================================

# Q8: Nested list operations
#    Given: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#    Access:
#    - First row
#    - Element at row 1, column 2 (value 6)
#    - Last element of last row (value 9)
#    - Modify element at row 0, column 1 to 99

print("\n--- Q8: Nested Lists ---")
