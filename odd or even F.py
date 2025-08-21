import random

print("Welcome to Odd or Even Game!")
print("Guess whether the number is Odd or Even.")
print("Type 'exit' anytime to quit.\n")

score=0

while True:
    user_input=input("Type 'odd' or 'even':").lower()

    if user_input=="exit":
        print("Thanks for playing!")
        break

    if user_input not in ["odd","even"]:
        print("Invalid input. Please type 'Odd' or 'even'.")
        continue

    number = random.randint(0, 100)
    print(f"random number generated: {number}")

    if number==0:
        pass
    print("that's a neutral zero! Let's see if your guess counts.")

    if number % 2==0 and user_input=="even":
        print("Currect guess! it's even.")
        score +=1
    elif number % 2!=0 and user_input=="odd":
            print("Correct guess! It's odd.")
            score+=1
    else:
        print("wrong guess.")

    print(f"Your current score:{score}\n")                                                          
                      
