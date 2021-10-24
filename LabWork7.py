# 7.Write a menu driven program to perform the following on strings:
# a) Find the length of string.
# b) Return maximum of three strings.
# c) Accept a string and replace all vowels with “#”
# d) Find number of words in the given string.
# e) Check whether the string is a palindrome or not


from MyString import *


def main():
    while True:
        print("\n------------------------------------------------------------------------")
        print("It is a menu driven program to perform the following String operations:")
        print("""\t\t1. Find the length of string
        2. Return the maximum of three strings
        3. Accept a string and replace all vowels with \"#\"
        4. Find number of words in the given string
        5. Check whether the string is a palindrome or not
        6. Exit Program""")
        print("------------------------------------------------------------------------")

        choice = int(input("Enter Choice: "))
        print("------------------------------------------------------------------------\n")
        if choice == 1:
            string = input("Enter String: ")
            print("Your string has {0} characters".format(string_length(string)))
        elif choice == 2:
            string1 = input("Enter String1: ")
            string2 = input("Enter String2: ")
            string3 = input("Enter String3: ")
            print("The maximum of these three string is", max_string(string1, string2, string3))
        elif choice == 3:
            string = input("Enter String: ")
            print("Your string after replacing vowels with \"#\" is", replace_vowel(string))
        elif choice == 4:
            string = input("Enter String: ")
            print("There are {0} words in this string".format(no_of_words_in_string(string)))
        elif choice == 5:
            string = input("Enter String")
            if palindrome(string):
                print("This string is Palindrome")
            else:
                print("This string is not Palindrome")
        elif choice == 6:
            break
        else:
            print("Wrong Choice")


if __name__ == "__main__":
    main()
