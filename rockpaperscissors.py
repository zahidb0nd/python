import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper,'s' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
    user_score = 0
    computer_score = 0
    print(f"the computer chose {computer}")
    if user == computer:
        return 'it is a tie!'

# r > s, s > p, p > r
    elif is_win(user,computer):
        user_score+=1
        print(user_score)
        return 'you won!'

    else:
        computer_score+=1
        print(computer_score)
        return 'you lost'

def is_win(player, opponent):
    #return true if player wins
    # r > s, s > p, p > r
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True 

print(play())
