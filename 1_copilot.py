# list of three students named Jon, Kim and Lee
students = ["Jon", "Kim", "Lee"]
# change Jon to John
students[0] = 'John'
# add more students after the list is created
students.append("Sara")
students.append("Miko")

# function to print 'Hi name' for each student in the list
def print_his():
    print(f"Total students: {len(students)}")
    for student in students:
        print(f"Hi {student}")

# call the function
print_his()




