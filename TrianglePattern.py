#function to print right triangle
def right_triangle(n):
    #this for loop is to manage rows in increasing order
    for i in range(1, n + 1):

        #this for loop is to pring starts in increasing order
        for j in range(1, i + 1):
            print("* ", end="")

        #this print is to move to next row after the completion of one row
        print()

#function to print inverted triangle
def inverted_triangle(n):
    #this for loop is to manage rows in decreasing order
    for i in range(n, 0, -1):

        #this for loop is to print spaces in increasing order (0 space in first row, 1 in 2nd, and so on)
        for space in range(0, n - i):
            print("  ", end="")

        #this for loop is to print the first half part of the inverted triangle i.e. the inverted right triangle part
        for j in range(i, 2 * i):
            print("* ", end="")

        #this for loop is to print the remaining stars of the inverted triangle in decreasing order (increasing loop is used as i will be decreasing)
        for j in range(1, i):
            print("* ", end="")

        # this print is to move to next row after the completion of one row
        print()

#main function
def main():
    #taking number of rows from user
    n = int(input("Enter n: "))

    #giving choices to the user
    choice = int(input("Select from the given patterns:\n1. Right Triangle\n2. Inverted Triangle\n\nChoice: "))

    #if elif else condition to call the correct function
    if choice == 1:
        right_triangle(n)
    elif choice == 2:
        inverted_triangle(n)
    else:
        print("Wrong Choice!\n")

#calling main function
if __name__ == '__main__':
    main()
