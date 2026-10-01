# Rock, Paper, Scissors
# Rock beats scissors; scissors beats paper; paper beats rock.
# For the basic version, assume the player enters a valid lowercase move.

import random

moves = ["rock", "paper", "scissors"]


# Complete the rules. Return "win", "draw", or "loss" for the player.
def compare_moves(player, opponent):
    if player == opponent:
        return "draw"
    elif player == "rock":
        # Win against scissors; otherwise lose.
        return "win" if opponent == "scissors" else "loss"
        pass
    elif player == "paper":
        # Compare with the opponent and return the result.
        return "win" if opponent == "rock" else "loss"
        pass
    else:  # The player chose scissors.
        # Compare with the opponent and return the result.
        return "win" if opponent == "paper" else "loss"
        pass



print(compare_moves("paper", "rock"))
print(compare_moves("rock", "paper"))
print(compare_moves("scissors", "scissors"))

# Play five rounds.
wins = 0
losses = 0
draws = 0

for round_number in range(1, 6):
    print("Round:", round_number)
    player = input("rock, paper, scissors or q: ").lower().strip() 
    if player == "q":
        break
    opponent = random.choice(moves)
    print("Computer:", opponent)
    result = compare_moves(player, opponent)
    print(result)
    if result == "win":
        wins += 1
    elif result == "loss":
        losses += 1
    else:
        draws += 1
    print("wins:", wins) 
    print("losses:", losses)
    print("draws:", draws)

    
    

    

# Optional extensions:
# - Reject entries that are not in moves; ask again without using a round.
# - Convert uppercase input to lowercase and strip outer spaces.
# - Let the player enter q to quit.
# - Count wins, draws, and losses across the five rounds.
# - Simulate 600 rounds using random choices for both players.
#   Print the totals and calculate wins / 600 * 100 as the win percentage.
