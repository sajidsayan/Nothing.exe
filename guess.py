import random

def start():
    choise = [1,2,3,4,5,6,7,8,9,10]
    u_s = 0
    print("Guess 1-10 number")
    while True:
        print("Guess a number under 1-10")
        c = (input("Enter the number under 1-10 or (write quit to exit game): ")).lower()
        
        if c == "quit":
            print("Thanks for playing Guess game")
            print(f"Final Score and computer score is {u_s}")
            break
        
        if not c.isdigit() or int(c) not in choise:
            print("Invaild number input number again")
            continue
        
        c = int(c)
        
        r = random.choice(choise)
        if c == r:
            print("You got a score")
            u_s += 1
            print(f"Current Score: You: {u_s}")
        elif not c == r:
            print("Wrong Answer!")
            print(f"Current Score: You: {u_s}")
            
start()
