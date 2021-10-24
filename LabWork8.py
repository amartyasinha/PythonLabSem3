# 8. Write a Python program to perform the following using list:
# a) Check if all elements in list are numbers or not.
# b) If it is a numeric list,then count number of odd values in it.
# c) If list contains all Strings,then display largest String in the list.
# d) Display list in reverse form.
# e) Find a specified element in list.
# f) Remove the specified element from the list.
# g) Sort the list in descending order.
# h) accept 2 lists and find the common members in them.

from MyList import *


def main():
    choice = ""
    lst = input_list()

    while choice != 0:
        print('''
---------------------------------------------------------------------------
0. Quit
1. Check if all elements in list are numbers or not.
2. If it is a numeric list,then count number of odd values in it.
3. If list contains all Strings,then display largest String in the list.
4. Display list in reverse form.
5. Find a specified element in list.
6. Remove the specified element from the list.
7. Sort the list in descending order.
8. accept 2 lists and find the common members in them.
---------------------------------------------------------------------------
''')

        choice = int(input("Enter your Choice:"))

        if choice == 0:
            quit(0)

        elif choice == 1:
            check = check_number_in_list(lst)
            if check:
                print("It is a numeric list")
            else:
                print("It is a non-numeric list")

        elif choice == 2:
            print("The odd values in the list are", count_odd_values(lst))

        elif choice == 3:
            print("The largest string in the list is ", display_largest_string(lst))

        elif choice == 4:
            print("The list in reversed form is ", lst_rev(lst))

        elif choice == 5:
            ele = input("Enter the element that you want to search:")

            print(find_element(lst, ele))

        elif choice == 6:
            ele = input("Enter the element that you want to remove:")

            check = remove_element(lst, ele)
            if check:
                print("{} is removed from the list".format(ele))
            else:
                print("{} not found in the list".format(ele))

        elif choice == 7:
            sort_dec(lst)
            print("The list after sorting in descending order is ", lst)

        elif choice == 8:
            lst1 = input_list()
            lst2 = input_list()

            print("The common members in these lists are ", common_members(lst1, lst2))
        else:
            print("Wrong Choice!")


if __name__ == '__main__':
    main()
