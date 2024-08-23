import random as rd

while True: 
    number = rd.randint(1, 10)
    answer = 0
    
    while answer < 3:
        guess = int(input("Guess the hidden number (1-10): "))
        if guess == number:
            print("Congratulations! You guessed the right number!")
            break
        elif guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
        answer += 1
    
    if answer == 3 and guess != number:
        print(f"Sorry, you've used all attempts. The correct number was {number}.")
    
    play_again = input("Do you want to play again? (y/n): ").strip().lower()
    if play_again != "y":
        print("Thank you for playing!")
        break
