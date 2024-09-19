import random

def roll():
    min_value = 1
    max_value = 6
    roll_value = random.randint(min_value, max_value)
    return roll_value

while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
players_scores = [0 for _ in range(players)]

while max(players_scores) < max_score:
    for player_idx in range(players):
        print(f"It's player number {player_idx+1} turn.")
        print(f"Your total score is: {players_scores[player_idx]}\n")
        current_score = 0

        while True:
            decision = input("Would you like to roll a dice?(y) ")
            if decision.lower().strip() != "y":
                break

            roll_res = roll()
            if roll_res == 1:
                current_score = 0
                print("You got 1! Your points are lost.")
                break
            else:
                current_score += roll_res
                print(f"You've got {roll_res} points")

        players_scores[player_idx] += current_score
        print(f"Your total score is {players_scores[player_idx]}\n")

max_score = max(players_scores)
winner_idx = players_scores.index(max_score)
print(f"Congratulation! Player number {players_scores[winner_idx]} won!")
