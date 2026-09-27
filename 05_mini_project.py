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

print("All Students:")
for student in students:
    print(student[0]) + ":", student[1]

# ----------------------------------------------------------
#    STEP 03:     Top Student
# ----------------------------------------------------------

print("\n--- Top Student ---")

# Sort grades
grades.sort(reverse = True)
print("Sorted Grades:", grades)

# Find top student
sorted_student = sorted(students, key = lambda x: x[1], reverse = True)
print("Top Student:", sorted_student[0][0], "-", sorted_student[0][1])

# ----------------------------------------------------------
#    STEP 04:     Analysis
# ----------------------------------------------------------

print("\n--- Analysis ---")

# Slicing
print("Top 3 Grades:", grades[:3])
print("Bottom 2 Grades:", grades[-2:])

# Search
print("Count of 90:", grades.count(90))
print("Index of 92:", grades.index(92))
