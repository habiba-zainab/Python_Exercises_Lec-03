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

copy_list = original.copy()
print("Copy:", copy_list)

copy_list[1] = 999
print("Modified copy:", copy_list)
print("Original unchanged:", original)

copy_list.clear()
print("After clear copy:", copy_list)
print("Original still intact:", original)

# ----------------------------------------------------------

# ==========================================================
# PART C:   List Sorting & Searching Methods
# ==========================================================

#    ***** Sorting Method *****

# Q5: sort() and reverse() methods
#    Given: nums = [64, 34, 25, 12, 22, 11, 90]
#    - Sort in ascending order
#    - Reverse the sorted list
#    - Sort in descending order using sort(reverse=True)

print("\n--- Q5: sort() & reverse() ---")

nums = [64, 34, 25, 12, 22, 11, 90]
print("Original:", nums)

nums.sort()
print("Sorting ascending:", nums)

nums.reverse()
print("Reversed:", nums)

nums.sort(reverse=True)
print("Sorted descending:", nums)

# ----------------------------------------------------------

#    ***** Searching Method *****

# Q6: index() and count() methods
#    Given: items = ['a', 'b', 'c', 'd', 'c', 'e', 'c', 'f']
#    - Find index of first 'c'
#    - Count how many times 'c' appears
#    - Find index of 'c' starting from position 3

print("\n--- Q6: index() & count() ---")

items = ['a', 'b', 'c', 'd', 'c', 'e', 'c', 'f']
print("Items:", items)

first_c = items.index('c')
print("First 'c' at index:", first_c)

count_c = items.count('c')
print("Count of 'c':", count_c)

c_from_3 = items.index('c', 3)
print("'c' from index 3:", c_from_3)

# ----------------------------------------------------------

# ==========================================================
#                LIST SLICING
# ==========================================================

# ==========================================================
# PART D:   Basic & Step List Slicing
# ==========================================================

#    ***** Basic List Slicing *****

# Q7: Given: numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#    Extract:
#    - First 5 elements [0:5]
#    - Last 5 elements [5:]
#    - Elements from index 2 to 7 [2:7]
#    - Middle 4 elements

print("\n--- Q7: Basic Slicing ---")

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original:", numbers)

first_5 = numbers[0:5]
print("First 5:", first_5)

last_5 = numbers[5:]
print("Last 5:", last_5)

index_2_7 = numbers[2:7]
print("Index 2-7:", index_2_7)

middle_4 = numbers[3:7]
print("Middle 4:", middle_4)

# ----------------------------------------------------------

#    ***** Step Slicing *****

# Q8: Given: nums = list(range(0, 21))  # [0, 1, 2, ..., 20]
#    Extract:
#    - Every 2nd element [::2]
#    - Every 3rd element [::3]
#    - Odd positioned elements [1::2]
#    - Every 2nd element in reverse [::-2]

print("\n--- Q8: Step Slicing ---")

nums = list(range(0, 21))
print("Original:", nums)

every_2nd = nums[::2]
print("Every 2nd:", every_2nd)

every_3rd = nums[::3]
print("Every 3rd:", every_3rd)

odd_positions = nums[1::2]
print("Odd positions:", odd_positions)

every_2nd_reversed = nums[::-2]
print("Every 2nd reversed:", every_2nd_reversed)

# ----------------------------------------------------------

# ==========================================================
# PART E:   Negative Slicing
# ==========================================================

# Q9: Negative slicing
#    Given: letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
#    Extract:
#    - Last 3 elements [-3:]
#    - All except last 2 [:-2]
#    - Elements from -5 to -2
#    - Everything in reverse [::-1]

