import random
def guessing_game():

    target_number = random.randint(1, 100)
    num_guesses = 0

    while True:

        guess = int(input("Guess the number between 1 and 100: "))
        num_guesses += 1


        if guess == target_number:
            print("Congratulations!")
            break
        elif guess < target_number:
            print("Too low")
        else:
            print("Too high")


if __name__ == "__main__":
    guessing_game()
