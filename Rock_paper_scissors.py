import random
from random import randint

available_options = {1: "Kamien", 2: "Papier", 3: "Nozyce"}
counter_user = 0
counter_pcu = 2

while counter_user < 3 and not counter_pcu >= 3:

    random_choice = random.randint(1, 3)
    user_choice2 = int(input(f"Wybierz jedną z dostpnych opcji --> {available_options} :"))

    if user_choice2 == 1 and random_choice == 2:
        counter_pcu += 1
        print(f"PCU won. \nUser: {counter_user} vs PCU: {counter_pcu}")
    elif user_choice2 == 1 and random_choice == 3:
        counter_user += 1
        print(f"User won! \nUser: {counter_user} vs PCU: {counter_pcu}")
    elif user_choice2 == 1 and random_choice == 1:
        print(f"Draw. \nUser: {counter_user} vs PCU: {counter_pcu}")
    elif user_choice2 == 2 and random_choice == 1:
        counter_user += 1
        print(f"User won! \nUser: {counter_user} vs PCU: {counter_pcu}")
    elif user_choice2 == 2 and random_choice == 2:
        print(f"Draw! User: {counter_user} vs PCU: {counter_pcu}")
    elif user_choice2 == 2 and random_choice == 3:
        counter_pcu += 1
        print(f"PCU won. \nUser: {counter_user} vs PCU: {counter_pcu}")
    elif user_choice2 == 3 and random_choice == 1:
        counter_pcu += 1
        print(f"PCU won. \nUser: {counter_user} vs PCU: {counter_pcu}")
    elif user_choice2 == 3 and random_choice == 2:
        counter_user += 1
        print(f"User won! \nUser: {counter_user} vs PCU: {counter_pcu}")
    elif user_choice2 == 3 and random_choice == 3:
        print(f"Draw! \nUser: {counter_user} vs PCU: {counter_pcu}")
    else:
        print("You selected a number out of range")
print (f"\nFinal results: User: {counter_user} vs PCU: {counter_pcu}!")
