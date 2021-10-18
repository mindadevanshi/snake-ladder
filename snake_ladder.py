import random
# Player's list:
#     Includes players as dictionary with following atttributes
#     Attributes = 
#         name = name of player
#         pos = position of the player
#         isActive = shows the status which player is playing
#         winner = shows which player has reached 100

players = [
    {
        "name": "a",
        "pos": 0,
        "isActive": True,
        "winner": False,
    },
    {
        "name": "b",
        "pos": 48,
        "isActive": False,
        "winner": False,
    },
    {
        "name": "c",
        "pos": 0,
        "isActive": False,
        "winner": False,
    },
    {
        "name": "d",
        "pos": 0,
        "isActive": False,
        "winner": False,
    }
]

# Board's list:
#     Includes 100 dictionary for each position of the board
#     Attributes = 
#         pos = gives the block number
#         snake = shows if there is snake at that position
#             if not found -> "NULL"
#             if found -> gives the redirected position of the token
#         ladder = shows if there is ladder at that position
#             if not found -> "NULL"
#             if found -> gives the redirected position of the token

board = [
    {"pos": 0, "snake": "Null", "ladder": "Null"},
    {"pos": 1, "snake": "Null", "ladder": "Null"},
    {"pos": 2, "snake": "Null", "ladder": "Null"},
    {"pos": 3, "snake": "Null", "ladder": "Null"},
    {"pos": 4, "snake": "Null", "ladder": 14},
    {"pos": 5, "snake": "Null", "ladder": "Null"},
    {"pos": 6, "snake": "Null", "ladder": "Null"},
    {"pos": 7, "snake": "Null", "ladder": "Null"},
    {"pos": 8, "snake": "Null", "ladder": "Null"},
    {"pos": 9, "snake": "Null", "ladder": "Null"},
    {"pos": 10, "snake": "Null", "ladder": "Null"},
    {"pos": 11, "snake": "Null", "ladder": "Null"},
    {"pos": 12, "snake": "Null", "ladder": "Null"},
    {"pos": 13, "snake": "Null", "ladder": "Null"},
    {"pos": 14, "snake": "Null", "ladder": "Null"},
    {"pos": 15, "snake": "Null", "ladder": "Null"},
    {"pos": 16, "snake": "Null", "ladder": "Null"},
    {"pos": 17, "snake": "Null", "ladder": "Null"},
    {"pos": 18, "snake": "Null", "ladder": 45},
    {"pos": 19, "snake": "Null", "ladder": "Null"},
    {"pos": 20, "snake": "Null", "ladder": "Null"},
    {"pos": 21, "snake": "Null", "ladder": "Null"},
    {"pos": 22, "snake": "Null", "ladder": "Null"},
    {"pos": 23, "snake": "Null", "ladder": "Null"},
    {"pos": 24, "snake": "Null", "ladder": "Null"},
    {"pos": 25, "snake": "Null", "ladder": "Null"},
    {"pos": 26, "snake": "Null", "ladder": "Null"},
    {"pos": 27, "snake": "Null", "ladder": "Null"},
    {"pos": 28, "snake": "Null", "ladder": 84},
    {"pos": 29, "snake": "Null", "ladder": "Null"},
    {"pos": 30, "snake": "Null", "ladder": "Null"},
    {"pos": 31, "snake": "Null", "ladder": "Null"},
    {"pos": 32, "snake": "Null", "ladder": "Null"},
    {"pos": 33, "snake": "Null", "ladder": "Null"},
    {"pos": 34, "snake": "Null", "ladder": "Null"},
    {"pos": 35, "snake": "Null", "ladder": "Null"},
    {"pos": 36, "snake": "Null", "ladder": "Null"},
    {"pos": 37, "snake": "Null", "ladder": "Null"},
    {"pos": 38, "snake": "Null", "ladder": "Null"},
    {"pos": 39, "snake": "Null", "ladder": "Null"},
    {"pos": 40, "snake": "Null", "ladder": "Null"},
    {"pos": 41, "snake": "Null", "ladder": "Null"},
    {"pos": 42, "snake": "Null", "ladder": "Null"},
    {"pos": 43, "snake": "Null", "ladder": "Null"},
    {"pos": 44, "snake": "Null", "ladder": "Null"},
    {"pos": 45, "snake": "Null", "ladder": "Null"},
    {"pos": 46, "snake": "Null", "ladder": "Null"},
    {"pos": 47, "snake": "Null", "ladder": "Null"},
    {"pos": 48, "snake": "Null", "ladder": "Null"},
    {"pos": 49, "snake": "Null", "ladder": "Null"},
    {"pos": 50, "snake": "Null", "ladder": "Null"},
    {"pos": 51, "snake": "Null", "ladder": 67},
    {"pos": 52, "snake": "Null", "ladder": "Null"},
    {"pos": 53, "snake": "Null", "ladder": "Null"},
    {"pos": 54, "snake": 26, "ladder": "Null"},
    {"pos": 55, "snake": "Null", "ladder": "Null"},
    {"pos": 56, "snake": "Null", "ladder": "Null"},
    {"pos": 57, "snake": "Null", "ladder": "Null"},
    {"pos": 58, "snake": "Null", "ladder": "Null"},
    {"pos": 59, "snake": "Null", "ladder": "Null"},
    {"pos": 60, "snake": "Null", "ladder": "Null"},
    {"pos": 61, "snake": "Null", "ladder": "Null"},
    {"pos": 62, "snake": 19, "ladder": "Null"},
    {"pos": 63, "snake": "Null", "ladder": "Null"},
    {"pos": 64, "snake": "Null", "ladder": "Null"},
    {"pos": 65, "snake": "Null", "ladder": "Null"},
    {"pos": 66, "snake": "Null", "ladder": "Null"},
    {"pos": 67, "snake": "Null", "ladder": "Null"},
    {"pos": 68, "snake": "Null", "ladder": "Null"},
    {"pos": 69, "snake": "Null", "ladder": "Null"},
    {"pos": 70, "snake": "Null", "ladder": "Null"},
    {"pos": 71, "snake": "Null", "ladder": "Null"},
    {"pos": 72, "snake": "Null", "ladder": 91},
    {"pos": 73, "snake": "Null", "ladder": "Null"},
    {"pos": 74, "snake": "Null", "ladder": "Null"},
    {"pos": 75, "snake": "Null", "ladder": "Null"},
    {"pos": 76, "snake": "Null", "ladder": "Null"},
    {"pos": 77, "snake": "Null", "ladder": "Null"},
    {"pos": 78, "snake": "Null", "ladder": "Null"},
    {"pos": 79, "snake": "Null", "ladder": "Null"},
    {"pos": 80, "snake": "Null", "ladder": "Null"},
    {"pos": 81, "snake": "Null", "ladder": "Null"},
    {"pos": 82, "snake": "Null", "ladder": "Null"},
    {"pos": 83, "snake": "Null", "ladder": "Null"},
    {"pos": 84, "snake": "Null", "ladder": "Null"},
    {"pos": 85, "snake": "Null", "ladder": "Null"},
    {"pos": 86, "snake": "Null", "ladder": "Null"},
    {"pos": 87, "snake": "Null", "ladder": "Null"},
    {"pos": 88, "snake": "Null", "ladder": "Null"},
    {"pos": 89, "snake": "Null", "ladder": "Null"},
    {"pos": 90, "snake": "Null", "ladder": "Null"},
    {"pos": 91, "snake": "Null", "ladder": "Null"},
    {"pos": 92, "snake": "Null", "ladder": "Null"},
    {"pos": 93, "snake": 73, "ladder": "Null"},
    {"pos": 94, "snake": "Null", "ladder": "Null"},
    {"pos": 95, "snake": 75, "ladder": "Null"},
    {"pos": 96, "snake": "Null", "ladder": "Null"},
    {"pos": 97, "snake": "Null", "ladder": "Null"},
    {"pos": 98, "snake": 7, "ladder": "Null"},
    {"pos": 99, "snake": "Null", "ladder": "Null"}
]

# function = find_player()
# task = finds the player which is active and not the winner
# return = player(dict): current active player
# variables = player(dict): object to iterate the player list

def find_player():
    for player in players:
        if(player["isActive"] == True and player["winner"] == False):
            return player

# function = change_player()
# argument list = curr_player(dict): current player 
# task = changes the player acc to the following conditions
#         set the current player's is active status as false
#         finds the current player's index and increases it
#         if the index reaches at last position, iterating it to the first
#         setting the is active attribute of the next player as true
#         if the next player is winner then recursively calling the function to find the player which is not winner
# return = player(dict): current active player
# variables = player_index(int): index of the current player 

def change_player(curr_player):
    curr_player["isActive"] = False
    player_index = players.index(curr_player)
    player_index += 1
    if player_index == len(players):
        players[0]["isActive"] = True
        player = players[0]
    
    else:
        players[player_index]["isActive"] = True
        player = players[player_index]
    
    if(player["winner"] == True):
        change_player(player)
    
    return player

# function = move_player()
# argument list = dice_value(int): value of dice
#                 curr_player(dict): current player 
# task = computing new position of the current player
#         if the new position > 100, then changing the player
#         if new position = 100, then setting the winner attribute of the player as True
#         if there is snake at new position, then changing the new position at snakes's tail
#         if there is ladder at new position, then changing the new position at ladder's tail
#         setting current position of the current player as new position
# return = curr_player(dict): current active player
# variables = new_position(int): counts the new position of the current player by adding its position to the dice value

def move_player(dice_value,curr_player):
    new_position = curr_player["pos"] + dice_value
    if(new_position > 100):
        return change_player(curr_player)
    
    elif(new_position == 100):
        curr_player["winner"] = True
        

    elif(board[new_position]["snake"] != "Null"):
        new_position = board[new_position]["snake"]

    elif(board[new_position]["ladder"] != "Null"):
        new_position = board[new_position]["ladder"]
        
    curr_player["pos"] = new_position

    return curr_player
    
# function = roll_dice()
# task = computes dice_value
#         finds the current player and store it in curr_player
#         checks if the position of the current player is 0 and there is no luck with six then the player is changed
#             and if it is six then the player moves to position 1 and then changed
#         if the player is at some other position then six, then the player moves to the location and then changed
# variables = dice _value(int): random value of dice between 1-6 
#             curr_player(dict): current player

def roll_dice():
    dice_value = random.randint(1,6)
    print(dice_value)
    curr_player = find_player()
    

    if(curr_player["pos"] == 0):
        if(dice_value != 6):
            curr_player = change_player(curr_player)
        else:
            curr_player["pos"] = 1
            curr_player = change_player(curr_player)

    else:
        curr_player = move_player(dice_value,curr_player)
        curr_player = change_player(curr_player)
    

# main function
if __name__=="__main__":
    for player in players:
        if player["winner"] is False:
            roll_dice()
        print(player)