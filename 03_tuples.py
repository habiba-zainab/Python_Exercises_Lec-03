"""

===========================================================
   LECTURE 03 - SET 03 : BASICS OF TUPLES
   Topics : Tuples Basics - Creating, Accessing & Operations
   Total Questions :  
============================================================

"""
# ==========================================================
# PART A:   Tuple Creation & Operation
# ==========================================================

# Q1: Create different types of tuples
#    Create:
#    - Empty tuple
#    - Single element tuple (remember comma!)
#    - Tuple with 5 integers
#    - Tuple with mixed types
#    - Nested tuple
#    Print each with type and length

print("\n--- Q1: Creating Tuples ---")

empty = ()
single = (5,)
integers = (1, 2, 3, 4, 5)
mixed = (1, 'hello', 25.5, True)
nested = ((1, 2), (3, 4), (5, 6))

print("Empty:", empty, "(Type: tuple, Length:", len(empty), ")") 
print("Single:", single, "(Type: tuple, Length:", len(single), ")") 
print("Integers:", integers, "(Length:", len(integers), ")") 
print("Mixed:", mixed, "(Length:", len(mixed), ")") 
print("Nested:", nested, "(Length:", len(nested), ")") 

# ----------------------------------------------------------

# Q2: Tuple operations
#    Given: tuple1 = (1, 2, 3)
#           tuple2 = (4, 5, 6)
#    Perform:
#    - Concatenation (tuple1 + tuple2)
#    - Reception (tuple1 * 3)
#    - Check if 3 in tuple1
#    - Find length of concatenated tuple

print("\n--- Q2: Tuple Operations ---")

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

print("tuple1:", tuple1)
print("tuple2:", tuple2)

concatenated = tuple1 + tuple2
print("Concatenated:", concatenated)

repeated = tuple1 * 3
print("Repeated:", repeated)

print("3 in tuple1:", 3 in tuple1)
print("Length:", len(concatenated))

# ----------------------------------------------------------

# ==========================================================
# PART B:   Tuple Indexing & Access
# ==========================================================

# Q3: Access tuple elements
#    Given:  coordinates = (10, 20, 30, 40, 50)
#    Access:
#    - First element (index 0)
#    - Third element (index 2)
#    - Last element (index -1)
#    - Second last (index -2)

print("\n--- Q3: Accessing Elements ---")

coordinates = (10, 20, 30, 40, 50)

print("Tuple:", coordinates)
print("First:", coordinates[0])
print("Third:", coordinates[2])
print("Last:", coordinates[-1])
print("Second last:", coordinates[-2])

# ----------------------------------------------------------

# Q4: Nested tuple access
#    Given:  matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
#    Access:
#    - First inner tuple
#    - Element at [1][2] (value 6)
#    - Last element of last tuple (value 9)
#    - Middle element (value 5)

print("\n--- Q4: Nested Tuples ---")

matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print("Matrix:", matrix)
print("First tuple:", matrix[0])
print("Element [1][2]:", matrix[1][2])
print("Last element:", matrix[-1][-1])
print("Middle:", matrix[1][1])

# ----------------------------------------------------------