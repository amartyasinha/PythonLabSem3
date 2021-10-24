# 9. Use dictionary to store marks of the students in 4 subjects. Write a function to find the name of the
# student securing highest percentage.(Hint: Names of students are unique).


def input_student_marks(total_stu, students_dict):
    for i in range(total_stu):
        name = input("Enter the name of Student {}: ".format(i + 1))
        marks = []
        for j in range(4):
            sub_marks = float(input("Enter the marks of Subject {}: ".format(j + 1)))
            marks.append(sub_marks)
        students_dict[name] = marks
        print("The Student {0} ({1}) marks are {2}".format(i + 1, name, students_dict[name]))


def highest_percentage(students_dict):
    top_stu = 'null'
    max_percentage = 0.0

    for key, value in students_dict.items():
        curr_percentage = sum(value)/4
        if curr_percentage > max_percentage:
            max_percentage = curr_percentage
            top_stu = key
    return top_stu, max_percentage


def main():
    students_dict = {}
    total_stu = int(input("Enter the total number of students"))
    input_student_marks(total_stu, students_dict)
    print("The student with highest percentage is ", highest_percentage(students_dict))


if __name__ == "__main__":
    main()
