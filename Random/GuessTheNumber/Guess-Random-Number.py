#This is a random guess number game
def guess(): 
    import random   
    randumnumber=random.randint(1,20) #Computer will pick one random number between 1 to 20
    n=1
#Ask User to guess the number 7 times
    print("I am thinking of a number between 1 and 20")
    while n<=7:
        guesstaken=int(input("Take a Guess :"))
        
        if (guesstaken<randumnumber):
            print("Your guess is too low")
            n=n+1
        elif(guesstaken>randumnumber):
            print("Your guess is too high")
            n=n+1
        else:
            break   #If the guess is right condition will break

    if(guesstaken==randumnumber):
        print(f"Good Job! You guessed my number in {n} guesses")
    else:
        print(f"Nope! The number i was thinking of was {randumnumber}")

#Function Call.
guess()