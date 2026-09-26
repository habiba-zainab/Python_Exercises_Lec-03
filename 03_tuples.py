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
