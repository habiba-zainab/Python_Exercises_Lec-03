"""

===========================================================
   LECTURE 03 - SET 04 : TUPLES METHODS & SLICING
   Topics : Tuples Methods & Slicing(+VE, -VE, Steps)
   Total Questions :  
============================================================

"""

# ==========================================================
#                TUPLE METHODS
# ==========================================================

# Q1:  count() method
#    Given: numbers = (1, 2, 3, 2, 4, 2, 5, 6, 2)
#    Count:
#    - How many times 2 appears
#    - How many times 5 appears
#    - How many times 10 appears (not in tuple)

print("\n--- Q1: count() method ---")

numbers = (1, 2, 3, 2, 4, 2, 5, 6, 2)

print("Tuple:", numbers)
print("Count of 2:", numbers.count(2))
print("Count of 5:", numbers.count(5))
print("Count of 10:", numbers.count(10))

# ----------------------------------------------------------

# Q2:  index() method
#    Given: letters = ('a', 'b', 'c', 'd', 'c', 'e', 'c')
#    Find:
#    - Index of first 'c'
#    - Index of 'c' starting from position 3

print("\n--- Q2: index() method ---")

letters = ('a', 'b', 'c', 'd', 'c', 'e', 'c')

print("Tuple:", letters)
print("First 'c' at index:", letters.index('c'))
print("'c' from index 3:", letters.index('c', 3))

# ----------------------------------------------------------

# ==========================================================
#                TUPLE SLICING
# ==========================================================

# Q3:  Basic tuple slicing
#    Given: nums = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
#    Extract:
#    - First 5 elements [0:5]
#    - Last 5 elements [5:]
#    - Middle elements [3:7]
#    - Every element [:]

print("\n--- Q3; Basic Slicing ---")

nums = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print("Original:", nums)
print("First 5:", nums[0:5])
print("Last 5:", nums[5:])
print("Middle:", nums[3:7])
print("All:", nums[:])

# ----------------------------------------------------------
