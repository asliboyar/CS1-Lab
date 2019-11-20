import random
while True:
    print("Enter your choice: \n 1. Rock \n 2. Paper \n 3. Scissors \n")

    choice = int(input("What is your choice?(1, 2, 3) "))

    if choice == 1:
      choice_name = 'Rock'
      print("Your choice: Rock")
    elif choice == 2:
      choice_name = 'Paper'
      print("Your choice: Paper")
    else:
      choice_name = 'Scissors'
      print("Your choice: Scissors")

    comp_choice = random.randint(1, 3)

    if comp_choice == 1:
      comp_choice_name = 'Rock'
      print("Computer choice: Rock")
    elif comp_choice == 2:
      comp_choice_name = 'Paper'
      print("Computer choice: Paper")
    else:
      comp_choice_name = 'Scissors'
      print("Computer choice: Scissors")

    if((choice == 1 and comp_choice == 2) or
      (choice == 2 and comp_choice ==1 )):
      result = "Paper"
    elif((choice == 1 and comp_choice == 3) or
        (choice == 3 and comp_choice == 1)):  
      result = "Rock"
    else:
      result = "Scissors"

    if result == choice_name:
        print("You won! :)")
    elif choice==comp_choice:
      print("Tie!")
    else:
        print("Computer won! :(")

    print("Do you want to play again? If no please write n ")
    ans = input()
    if ans == 'n':
        break
