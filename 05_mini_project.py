"""

===========================================================
   LECTURE 03 - SET 05 : MINI PROJECT
   Topics :     All Topics are included
============================================================

"""

# ===========================================================
#               STUDENT GRADE MANAGER
# ===========================================================

# ----------------------------------------------------------
#    STEP 01:     Add Grades
# ----------------------------------------------------------

print("\n--- Grade List ---")

# Create and add grades using list
grades = [85, 92, 78, 90, 88]

print("Grades:", grades)
print("Total Students:", len(grades))
print("Highest:", max(grades))
print("Lowest:", min(grades))
print("Average:", sum(grades) / len(grades))

# ----------------------------------------------------------
#    STEP 02:     Student Records
# ----------------------------------------------------------

print("\n--- Student Records ---")

# Use tuples for student data (name, grade)
students = [
    ("Alice", 92)
    ("Bob", 85)
    ("Charlie", 90)
]