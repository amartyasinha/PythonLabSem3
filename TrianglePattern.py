def right_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("* ", end="")
        print()

def inverted_triangle(n):
    for i in range(n, 0, -1):
        for space in range(0, n - i):
            print("  ", end="")

        for j in range(i, 2 * i):
            print("* ", end="")

        for j in range(1, i):
            print("* ", end="")
        print()

def main():
    n = int(input("Enter n: "))

    choice = int(input("Select from the given patterns:\n1. Right Triangle\n2. Inverted Triangle\n\nChoice: "))

    if choice == 1:
        right_triangle(n)

    elif choice == 2:
        inverted_triangle(n)

    else:
        print("Wrong Choice!\n")

if __name__ == '__main__':
    main()
