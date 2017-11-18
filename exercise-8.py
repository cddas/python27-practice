import random

user_choice = 'y'
counter = 0
try:
    while user_choice.lower() != 'exit':
        counter += 1
        user_input = raw_input("Guess a number between 1 to 9 : ")
        user_input = int(user_input)
        rand_number = random.randint(1, 9)
        if rand_number == user_input:
           print("Bingo !!! Your guess is correct. The hidden number is : " + str(rand_number))
        elif rand_number < user_input:
            print("Oops !!! Your guess was too high. The hidden number is : " + str(rand_number))
        else:
            print("Oops !!! Your guess was too low. The hidden number is : " + str(rand_number))

        user_choice = raw_input("Type 'exit' to stop the game :")
except ValueError:
    print("No Value Specified for the game to begin. Exiting with error")
finally:
    print("\nYou played the game " + str(counter) + " times")