import random 

#this function below is to get the random number first:
def roll():
    min_value = 1
    max_value = 6
    roll= random.randint(min_value, max_value)
    return roll 

#this while loop below is to make sure the number entered is between 2 and 4 else to retry:
while True:
    players = input("Enter the number of players (2-4) : ")
    if players.isdigit():
        players= int(players)
        if 2 <= players <=4:
            break
        else:
            print("Must be between 2-4.")
    else:
        print("Invalid try again! ")

#setting the defailt max score and also the range of players:
max_score = 50 
player_scores = [0 for _ in range(players)]

#the main function:
while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer number",player_idx +1 , "turn has just started\n")
        print("your total score is :", player_scores[player_idx], "\n")
        current_score = 0
        
        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break
            
            value=roll()
            if value==1:
                print("you rolled a 1! Turn done!! ")
                current_score=0
                break
            else:
                current_score += value
                print("you rolled a:", value)
            
            print("your score is:", current_score)
        
        player_scores[player_idx] += current_score
        print("your total score is:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx= player_scores.index(max_score)
print("Player number ", winning_idx +1,"is the winner with the score of :",max_score )