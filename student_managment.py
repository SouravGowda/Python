def calculate_highest_in_maths(student_list):
    highest = 0
    highest_name = ''
    for student in student_list:
        if(student.get("Maths")> highest):
            highest = student.get("Maths")
            highest_name = student.get("name")

    print(f"highest marks in maths is {highest} by {highest_name}")

def calculate_highest_in_Social(student_list):
    highest = 0
    highest_name = ''
    for student in student_list:
        if(student.get("Social")> highest):
            highest = student.get("Social")
            highest_name = student.get("name")

    print(f"highest marks in Social is {highest} by {highest_name}")


student_1 = {
    "Maths" : 45,
    "Social" : 75,
    "Science" : 96,
    "name" : "Tanmay"
}

student_2 = {
    "Maths" : 56,
    "Social" : 53,
    "Science" : 43,
    "name" : "Dheeraj"
}

student_3 = {
    "Maths" : 100,
    "Social" : 24,
    "Science" : 53,
    "name" : "Sooraj"
}

student_list = [student_1,student_2,student_3]

calculate_highest_in_maths(student_list)
calculate_highest_in_Social(student_list)