"""

===========================================================
   LECTURE 03 - SET 02 : LIST METHODS & SLICING
   Topics : List Methods & Slicing(Positive, Negative, Step)
   Total Questions :  
============================================================

"""

# ==========================================================
#                LIST METHODS
# ==========================================================

# ==========================================================
# PART A:   List Adding Methods
# ==========================================================

# Q1: append() and insert() methods
#    Start with: fruits = ["apple", "banana"]
#    - Append "cherry"
#    - Insert "mango" at index 1
#    - Append "orange"
#    Print list after each operation

print("\n--- Q1: append() & insert() ---")

fruits = ["apple", "banana"]
print("Start:", fruits)

fruits.append("cherry")
print("After append 'cherry':", fruits)

fruits.insert(1, "mango")
print("After insert 'mango' at 1:", fruits)

fruits.append("orange")
print("After append 'orange':", fruits)

# ----------------------------------------------------------

# Q2: extend() vs append() with lists
#    Given:   list1 = [1, 2, 3]
#             list2 = [4, 5, 6]
#    Create two copies of list1
#    On first copy: use append(list2)
#    On second copy: use extend(list2)
#    Compare results

print("\n--- Q2: extend() vs append() ---")

list1 = [1, 2, 3]
list2 = [4, 5, 6]

copy1 = list1.copy()
copy2 = list1.copy()
