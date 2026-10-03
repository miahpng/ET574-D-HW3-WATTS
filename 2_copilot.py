# Each student's name is a key.
# The value is a list containing the student's GPA and major.
students = {
    "Jon": [3.25, "Math"],
    "Kim": [2.25, "Biology"],
    "Lee": [2.30, "Math"],
    "Sara": [4.00, "Math"],
    "Miko": [1.90, "Math"],
    "Lin": [2.10, "Biology"],
    "Toby": [2.89, "Biology"],
    "Ben": [2.75, "Math"],
    "Mark": [2.34, "Math"],
    "Xia": [3.53, "Biology"]
}

# Add all the GPAs together
total_gpa = 0

for student in students:
    total_gpa = total_gpa + students[student][0]

# Calculate and print the average GPA
average_gpa = total_gpa / len(students)
print(f"Average GPA: {average_gpa:.2f}")

# Print students whose GPA is above average
print("\nAbove-average students:")

for student in students:
    gpa = students[student][0]

    if gpa > average_gpa:
        print(f"{student}: GPA {gpa:.2f}")

# Check scholarship eligibility using the student's major
print("\nPredicted scholarship recipients:")

for student in students:
    gpa = students[student][0]
    major = students[student][1]

    if major == "Math" and gpa >= 3.5:
        print(f"{student}: GPA {gpa:.2f}, {major}")
    elif major == "Biology" and gpa >= 2.75:
        print(f"{student}: GPA {gpa:.2f}, {major}")