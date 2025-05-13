# Number guessing game
import random as r

print("-"*10+"wellcom to game"+"-"*10)
while True:
    print("1) Start game\n2) Exit the game")
    Choice_number = input("choice the number :")
    choices = ["stone","Paper","Scissors"]
    if Choice_number == "1":
        print('-'*20)
        print("Numbers:\n1)stone\n2)Paper\n3)Scissors")
        choice_humen = input("please enter your number : ")
        choice_computer = r.choice(choices)
        print('-'*10)
        print(f"your number : {choice_humen}\ncomputer number : {choice_computer}")
        if choice_humen == choice_computer:
                print("It's a tie!")
        elif (choice_humen == "stone" and choice_computer == "scissors") or \
             (choice_humen == "paper" and choice_computer == "stone") or \
             (choice_humen == "scissors" and choice_computer == "paper"):
            print("You win!")
        else:
            print("Computer wins!")
        print('-'*10)
    elif Choice_number == "2":
        print("Thanks for playing! Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1 or 2.")      