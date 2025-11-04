# This project created in 2025/10/31 at 11:40 PM
# Created by Khaled Mahmoud 

import random


guess = 0
winning_score = 0
last_winstreak = 0
max_winning_streak = 0
loosing_score = 0
draw_score = 0
attempts = 0
passkey = "999"


while True:
    Number = random.choice(["paper", "rock", "scissor"])
    guess = input("Guess a type (paper, rock, scissor) or type info or exit: ").lower()
    print("=" * 70)

    if guess == "exit":
        print("Will miss you! :(")
        print("=" * 70)
        break

    elif guess == "info":
        print("This game created by Khaled Mahmoud in 2025/10/31 at 11:53PM")
        print("=" * 70)
        chose = input("If you want to give feedback type (y/n): ").lower()
        if chose.lower() == "n":
            print("OK!")
            print("=" * 70)
            continue
        if chose.lower() == "y":
            print("Thank You For Help Me !")
            Name = input("Your Name?: ")
            Age = input("Your age?: ")
            Country = input("Your Country?: ")
            Feedback = input("Can You Tell Me your feedback please ?: ")
            print("=" * 70)
            table = {
                "Name" :Name,
                "Age" : Age,
                "Country" : Country,
                "Feedback" : Feedback
            }

            last = input("Thanks you for talking with me, type (continue or exit)): ")
            if last == "continue":
                print("=" * 70)
                continue
            elif last == "exit":
                print("=" * 70)
                break
            elif last == passkey:
                print(table)
                print("=" * 70)
                continue
            else:
                print("not defined type")
                continue
        


    if guess in ["paper", "rock", "scissor"]:
        attempts += 1

    if guess == Number:
        print("Draw!")
        print(f"Computer Chose: {Number}")
        print(f"Winning streak: {last_winstreak}")
        draw_score += 1
        print("=" * 70)

    elif guess == "paper" and Number == "rock":
        print("You Won!")
        last_winstreak += 1
        print(f"Computer Chose: {Number}")
        print(f"Winning streak: {last_winstreak}")
        winning_score += 1
        if last_winstreak > max_winning_streak:
            max_winning_streak = last_winstreak
        print("=" * 70)

    elif guess == "paper" and Number == "scissor":
        print("You Lose!")
        last_winstreak = 0
        print(f"Computer Chose: {Number}")
        print(f"Winning streak: {last_winstreak}")
        loosing_score += 1
        print("=" * 70)

    elif guess == "rock" and Number == "paper":
        print("You Lose!")
        last_winstreak = 0
        print(f"Computer Chose: {Number}")
        print(f"Winning streak: {last_winstreak}")
        loosing_score += 1
        print("=" * 70)

    elif guess == "rock" and Number == "scissor":
        print("You Won!")
        last_winstreak += 1
        print(f"Computer Chose: {Number}")
        print(f"Winning streak: {last_winstreak}")
        winning_score += 1
        if last_winstreak > max_winning_streak:
            max_winning_streak = last_winstreak
        print("=" * 70)

    elif guess == "scissor" and Number == "paper":
        print("You Won!")
        last_winstreak += 1
        print(f"Computer Chose: {Number}")
        print(f"Winning streak: {last_winstreak}")
        winning_score += 1
        if last_winstreak > max_winning_streak:
            max_winning_streak = last_winstreak
        print("=" * 70)

    elif guess == "scissor" and Number == "rock":
        print("You Lose!")
        last_winstreak = 0
        print(f"Computer Chose: {Number}")
        print(f"Winning streak: {last_winstreak}")
        loosing_score += 1
        print("=" * 70)

    else:
        print("not defined type")
        print("=" * 70)

print("=" * 15, "Leaderboard", "=" * 15)
print(f"Your attempts is: {attempts} Times")
print(f"Your winning_score is: {winning_score} Times")
print(f"Your loosing_score is: {loosing_score} Times")
print(f"Your Draw_score is: {draw_score} Times")
print(f"Your last_winningstreak is: {last_winstreak} Times")
print(f"Your max_winningstreak is: {max_winning_streak} Times")
print("=" * 70)