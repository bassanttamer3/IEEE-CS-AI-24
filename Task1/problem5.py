input_word = input("Enter a word: ")


if input_word == input_word[::-1]:
    print(f"The word '{input_word}' is a palindrome.")
else:
    print(f"The word '{input_word}' is not a palindrome.")
