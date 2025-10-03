import random

# 1. Define password lists by difficulty
easy_words = ["apple", "train", "tiger", "money", "india"]
medium_words = ["python", "bottle", "monkey", "planet", "laptop"]
hard_words = ["elephant", "diamond", "umbrella", "computer", "mountain"]

# 2. User chooses difficulty
print("Welcome to the Password Guessing Game!")
level = input("Enter difficulty (easy, medium, or hard): ").lower()

if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid choice. Defaulting to easy level.")
    secret = random.choice(easy_words)

# 3. Let the user guess the password
attempts = 3
while attempts > 0:
    guess = input("Guess the password: ")
    if guess == secret:
        print("Congratulations! You guessed it right!")
        break
    else:
        attempts -= 1
        print(f"Wrong password. {attempts} attempts left.")
else:
    print(f"Sorry! The correct password was: {secret}")
    



