# 10. Write a function that takes a sentence as input from the user and calculates the frequency of each letter.
# Use a variable of dictionary type to maintain the count.

def letter_frequency(sentence, char_dict):
    for char in sentence:
        if char in char_dict.keys():
            char_dict[char] += 1
        elif char.isalpha():
            char_dict[char] = 1


def main():
    char_dict = {}
    sentence = input("Enter a sentence:")
    letter_frequency(sentence, char_dict)
    for char, count in char_dict.items():
        print(char, count)


if __name__ == "__main__":
    main()
