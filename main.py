import random
from art import logo, vs
from game_data import data

# Pair Generation
def pair_generator():
    a = random.randint(0, len(data) - 1)
    b = random.randint(0, len(data) - 1)
    while a == b:
        b = random.randint(0, len(data) - 1)
    return a, b

# Main Game
def game(compare_index, against_index):
    score = 0
    print(logo)
    while True:
        a_followers = data[compare_index]['follower_count']
        b_followers = data[against_index]['follower_count']

        # Display the two options to the user
        print(f"Compare A: {data[compare_index]['name']}, a {data[compare_index]['description']} from {data[compare_index]['country']}.")
        print(vs)
        print(f"Against B: {data[against_index]['name']}, a {data[against_index]['description']} from {data[against_index]['country']}.")

        # Get user input
        user_answer = input("Who has more followers? Type 'A' or 'B' (or 'exit' to quit): ")
        if user_answer.lower() == 'exit':
            print(f"Thanks for playing! Your final score is: {score}.")
            return

        # Validate user input
        while user_answer.upper() not in ['A', 'B']:
            print("Invalid Input! Try Again!")
            user_answer = input("Who has more followers? Type 'A' or 'B' (or 'exit' to quit): ")
            if user_answer.lower() == 'exit':
                print(f"Thanks for playing! Your final score is: {score}.")
                return

        # Check if the user's answer is correct
        if (user_answer.upper() == "A" and a_followers > b_followers) or (
                user_answer.upper() == "B" and b_followers > a_followers):
            score += 1
            print("\n" * 20)
            print(logo)
            print(f"You're correct! Your current score is: {score}.")
            compare_index = against_index  # Move B to A
            while True:
                _, new_against_index = pair_generator()  # Generate a new B
                if new_against_index != compare_index:
                    against_index = new_against_index
                    break
        else:
            print("\n" * 20)
            print(f"Sorry, that's wrong! Final Score: {score}.")
            return

# Variable Declaration
compare_index, against_index = pair_generator()

# Calling Main Game
game(compare_index, against_index)