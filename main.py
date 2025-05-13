import random

def rps():
    choises = ["rock","paper","scissor"]
    u_s = 0
    c_s = 0
    print("Welcome Bro at my first python game with importing something")
    while True:
        print("Mr your choise is [rock,paper,scissor]")
        c = input("Enter your choise (or write quit to exit): ").lower()
        if c == "quit":
            print("Thanks for playing my goodest game.")
            print(f"Final Score is {u_s} and computer score is {c_s}")
            break
        if c not in choises:
            print("Invaild Choise bro not fun with my best game")
            continue
        r = random.choice(choises)
        print(f"computer choise: {c_s}")
        if c == r:
            print("Its a tie!")
        elif (c == "rock" and r == "scissor") or \
             (c == "scissor" and r == "paper") or \
             (c == "paper" and r == "rock"):
            print("You win! Please play again my game")
            u_s += 1
        else:
            print("Computer Wins this round pls try again not leave now play more i want  money")
            c_s += 1
        print(f"Current Score: You: {u_s} Computer: {c_s}")

rps()
