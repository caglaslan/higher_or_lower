import art
import random
from game_data import data
import os
from time import sleep
def clear():
    os.system('cls')

def higher_or_lower_game():
    print(art.logo)
    first_person = random.choice(data)



    def compare_followers(A, B):
        follow_count_a = A["follower_count"]
        # print(follow_count_a)
        follow_count_b = B["follower_count"]
        # print(follow_count_b)
        if follow_count_b >= follow_count_a:
            winner = B
        else:
            winner = A
        return winner

    user_right_count = 0
    end_of_game = False
    while not end_of_game:

        print(f"Compare A: {first_person['name']}, a {first_person['description']}, from {first_person['country']}.")
        second_person = random.choice(data)
        while second_person == first_person:
            second_person = random.choice(data)
        print(art.vs)
        print(f"Compare B: {second_person['name']}, a {second_person['description']}, from {second_person['country']}.")
        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if user_guess == "a":
            user_guess = first_person
        elif user_guess == "b":
            user_guess = second_person


        if compare_followers(first_person,second_person) == user_guess:
            user_right_count += 1
            clear()
            print(f"\nYou're right! Current score: {user_right_count}")
            first_person = second_person
        else:
            clear()
            print(f"Sorry, that's wrong. Final score: {user_right_count}")
            restart_or_not = input("\n Do you want to restart the game? Type 'y' to restart, 'n' to quit: ").lower()
            if restart_or_not == "y":
                clear()
                higher_or_lower_game()
            elif restart_or_not == "n":
                sleep(1)
                end_of_game = True

higher_or_lower_game()