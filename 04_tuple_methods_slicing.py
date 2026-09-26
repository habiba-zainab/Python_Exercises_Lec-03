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