def guess_game():
    name = input("input your name: ")
    greeting = f"Hello {name}, welcome to Toirat guessing game"
    print(greeting)
    print("In this game you are to guess a number, you have just 1 attempt.")
    
    attempt = 0
    max_attempt = 1
    secret_number = 22

    while attempt < max_attempt : 
        try:
            guess = int(input("Make a guess: "))
            attempt += 1
            if guess < secret_number:
                print("oops!, too low.")
                
            elif  guess > secret_number:
                print("your guess is higher than the secret number.")
            else:
                print(" CONGRATULATIONS!..You got the number correctly")
        except ValueError:
            print("Enter a valid number")
guess_game()

def play_again():
    guess = int(input("Make a guess: "))
    ask = input("Would you like to play again: ")
    answer1 = "yes, yeah, of course,"
    answer2 = "no, nah, nope, nop"

    if ask == answer1 :
        print(guess)
        guess_game()
    elif ask == answer2 :
        print("Thank you for playing the guess game")
play_again()
guess_game()





   


    
    

