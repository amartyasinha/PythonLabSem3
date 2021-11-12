# 15.Define a class Student to store his/her name and marks in three subjects. Use a class variable to store
# the maximum average marks of the class. Use constructor and destructor to initialize and destroy the objects.

class Student:
    name = str()
    marks = list()

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.avg_marks = 0

    def __del__(self):
        print('Object has been deleted successfully')

    def avg_marks_fun(self):
        self.avg_marks = sum(self.marks) / len(self.marks)
        return self.avg_marks


def main():
    name = input("Enter you name: ")
    marks = []
    for i in range(3):
        mrk = int(input("Enter marks {}: ".format(i + 1)))
        marks.append(mrk)

    stu = Student(name, marks)
    print("The name of student is", stu.name)
    print("The marks of the student are", stu.marks)
    print("Average marks is %0.2f" % stu.avg_marks_fun())

    del stu


if __name__ == '__main__':
    main()
