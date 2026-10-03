import csv

students = {}

# Read the student data from the CSV file
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["Name"]
        gpa = float(row["GPA"])
        major = row["Major"]

        students[name] = [gpa, major]

# Add the GPAs to calculate the average
total_gpa = 0

for name in students:
    total_gpa = total_gpa + students[name][0]

average_gpa = total_gpa / len(students)
print(f"Average GPA: {average_gpa:.2f}")

# Print students whose GPA is above average
print("\nAbove-average students:")

for name in students:
    gpa = students[name][0]

    if gpa > average_gpa:
        print(f"{name}: {gpa:.2f}")

# Predict scholarship eligibility using the major and GPA rules
print("\nPredicted scholarship recipients:")

for name in students:
    gpa = students[name][0]
    major = students[name][1]

    if major == "Math" and gpa >= 3.50:
        print(f"{name}: {gpa:.2f}, {major}")
    elif major == "Biology" and gpa >= 2.75:
        print(f"{name}: {gpa:.2f}, {major}")