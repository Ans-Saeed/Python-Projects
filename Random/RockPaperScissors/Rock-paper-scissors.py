import random,sys
print("    ROCK | PAPER | SCISSORS")
w=0
l=0
t=0
while True:
    print(f"{w} Wins,{l} Losses, {t} Ties")
    while True:
        print("Please Enter your move (p) Paper, (s) Scissors, (r) Rock, (q) Quit :")
        playerchoice=input()
        if(playerchoice=="p"):
            print("PAPER Versus.....")
            break
        elif(playerchoice=="s"):
            print("SCISSORS Versus.....")
            break
        elif(playerchoice=="r"):
            print("ROCK Versus.....")
            break
        elif(playerchoice=="q"):
            print("THANK YOU for Playing with me.")
            sys.exit()
        else:
            print("Please Enter a valid choice (p) Paper, (s) Scissors, (r) Rock, (q) Quit:")
    
    randnum=random.randint(1,3)
    if(randnum==1):
        compchoice="r"
        print("Rock")
    elif(randnum==2):
        compchoice="s"
        print("SCISSORS")
    else:
        compchoice="p"
        print("PAPER")

    if(compchoice==playerchoice):
        print("Its a tie.. Try Again")
        t+=1
    elif(compchoice=="r" and playerchoice=="p"):
        print("You Win!")
        w+=1
    elif(compchoice=="p" and playerchoice=="r"):
        print("You Lose!")
        l+=1
    elif(compchoice=="r" and playerchoice=="s"):
        print("You Lose!")
        l+=1
    elif(compchoice=="s" and playerchoice=="r"):
        print("You Win!")
        w+=1
    elif(compchoice=="p" and playerchoice=="s"):
        print("You Lose!")
        l+=1
    elif(compchoice=="s" and playerchoice=="p"):
        print("You Win!")
        w+=1    
        
