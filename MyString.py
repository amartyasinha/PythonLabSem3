def string_length(string):
    length = 0
    for _ in string:
        length += 1
    return length


def max_string(string1, string2, string3):
    if string_length(string1) > string_length(string2) and string_length(string1) > string_length(string3):
        return string1
    elif string_length(string2) > string_length(string1) and string_length(string2) > string_length(string3):
        return string2
    else:
        return string3


def replace_vowel(string):
    vowel = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    for char in string:
        if char in vowel:
            string = string.replace(char, "#")
    return string


def no_of_words_in_string(string):
    count = 1
    for i in string:
        if i == " ":
            count += 1
    return count


def palindrome(string):
    for i in range(0, int(string_length(string)/2)):
        if string[i] != string[string_length(string)-i-1]:
            return False
    return True
