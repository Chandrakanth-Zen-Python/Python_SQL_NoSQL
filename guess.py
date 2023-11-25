
import random


def GuessNumber():

    'Guessing game to find the number in 3 trials'

    num_generated=random.randint(1,20)

    trials=0

    while trials<3:

        try:

            num_guessed=int(input("Enter the number between 1-20:")) 

            trials+=1           

            if num_guessed < 1 or num_guessed>20:

                raise ValueError("This is way off range.")
            
            else:

                if num_guessed<num_generated:

                    print("Number Generated is larger than your guess")
                
                elif num_guessed>num_generated:

                    print("Number Generated is smaller than your guess")
                
                else:

                    break
        
        except ValueError as V:

            print("Exception:",V)

            print("This is not a valid number:")
    
    if num_generated==num_guessed:

        print("Congrats !!!. You made it.")
    
    else:

        print("The Generated number is :",num_generated)

        print("Better luck next time")

        



GuessNumber()