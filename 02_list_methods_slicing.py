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

print("Original:", list1)

copy1.append(list2)
print("After append([4, 5, 6]):", copy1)

copy2.extend(list2)
print("After extend([4, 5, 6]):", copy2)

# ----------------------------------------------------------

# ==========================================================
# PART B:   List Removing Methods
# ==========================================================

# Q3: remove() and pop() methods
#    Given: numbers = [10, 20, 30, 40, 50, 30]
#    - Remove first occurrence of 30
#    - Pop last element 
#    - Pop element at index 1
#    Print list after each operation

print("\n--- remove() & pop() ---")

numbers = [10, 20, 30, 40, 50, 30]
print("Original:", numbers)

numbers.remove(30)
print("After remove(30):", numbers)

removed1 = numbers.pop()
print("After pop():", numbers, "(removed:", str(removed1) + ")")

removed2 = numbers.pop(1)
print("After pop(1):", numbers, "(removed:", str(removed2) + ")")

# ----------------------------------------------------------

# Q4: copy() and clear() methods
#    Given: original = [1, 2, 3, 4, 5]
#    - Create a copy using copy()
#    - Modify the copy
#    - Show original is unchanged
#    - Clear the copy
#    - Show original still has data

print("\n--- Q4: copy() & clear() ---")

original = [1, 2, 3, 4, 5]
print("Original:", original)
