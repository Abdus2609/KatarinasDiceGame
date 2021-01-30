import random


def enter_details():
    player1Name = str(input("Player 1, please enter your name: ")).capitalize()
    player2Name = str(input("Player 2, please enter your name: ")).capitalize()
    print("Hello, " + player1Name + " and " +
          player2Name + ", welcome to the game.")
    print("\n")

    return player1Name, player2Name


def roll_Two_Dice(name):
    print(name + ", please get ready. It's your turn...")
    playerRoll1 = random.randint(1, 6)
    playerRoll2 = random.randint(1, 6)
    print(name + ", your first roll was: " + str(playerRoll1))
    print(name + ", your second roll was: " + str(playerRoll2))
    points = calculate_score(name, playerRoll1 + playerRoll2)
    if playerRoll1 == playerRoll2:
        extraRoll = roll_One_Dice(name)
        extraScore = calculate_score(name, extraRoll)
        points += extraScore

    return points


def roll_One_Dice(name):
    print(name + ", you need to roll one extra die.")
    extraRoll = random.randint(1, 6)
    print(name + ", your extra roll was: " + str(extraRoll))

    return extraRoll


def calculate_score(name, score):
    if score % 2 == 0:
        score += 10
    else:
        score -= 5

    return score


def tie_breaker(player1Name, player2Name):
    print("Welcome to the tie breaker. Get ready!")
    player1TB = roll_One_Dice(player1Name)
    player2TB = roll_One_Dice(player2Name)
    player1TBScore = calculate_score(player1Name, player1TB)
    player2TBScore = calculate_score(player2Name, player2TB)
    winner = winner_decider(player1Name, player2Name,
                            player1TBScore, player2TBScore)

    return winner


def winner_decider(player1Name, player2Name, player1Score, player2Score):
    if player1Score > player2Score:
        winner = player1Name
        print("Congratulations, " + player1Name + ", you have won!!!")
    elif player1Score < player2Score:
        winner = player2Name
        print("Congratulations, " + player2Name + ", you have won!!!")
    else:
        winner = tie_breaker(player1Name, player2Name)

    return winner


def save_data(winnerName, winnerScore):
    print("Saving data...")
    print()

    file = open("winnerdetails.txt", "a")
    outputData = winnerName + "," + str(winnerScore) + "\n"
    file.write(outputData)
    file.close()


def load_data():
    dataBase = []
    file = open("winnerdetails.txt", "r")
    line = file.readline().rstrip()
    while line != "":
        winnerName, winnerScore = line.split(",")
        record = []
        record.extend((winnerName, int(winnerScore)))
        dataBase.append(record)
        line = file.readline().rstrip()
    file.close()

    return dataBase


def leaderboard(dataBase):
    print("*" * 30)
    print("LEADERBOARD")
    print()
    sortedDataBase = sorted(dataBase, key=lambda x: x[1], reverse=True)
    if len(sortedDataBase) < 5:
        for record in sortedDataBase:
            print(record)
    else:
        for record in sortedDataBase[:5]:
            print(record)

    print()
    print("*" * 30)

##############################################################################


PLAYER_1_SCORE = 0
PLAYER_2_SCORE = 0

ROUND = 1

player1Name, player2Name = enter_details()

while ROUND <= 5:
    print("Round", ROUND, "is about to start.")
    player1Points = roll_Two_Dice(player1Name)
    player1Score = calculate_score(player1Name, player1Points)
    print(player1Name + ", your score for this round is: " + str(player1Score))
    print()

    player2Points = roll_Two_Dice(player2Name)
    player2Score = calculate_score(player2Name, player2Points)
    print(player2Name + ", your score for this round is: " + str(player2Score))
    print()

    if player1Score < 0:
        print(player1Name + ", you have LOST. " + player2Name + " wins.")
        exit()

    ROUND += 1
    PLAYER_1_SCORE += player1Score
    PLAYER_2_SCORE += player2Score

    print(player1Name + ", your total score so far is: " + str(PLAYER_1_SCORE))
    print(player2Name + ", your total score so far is: " + str(PLAYER_2_SCORE))
    print()

print("\n")
print("RESULTS:")
print(player1Name + ", your total score this game was: " + str(PLAYER_1_SCORE))
print(player2Name + ", your total socre this game was: " + str(PLAYER_2_SCORE))
print()

winner = winner_decider(player1Name, player2Name,
                        PLAYER_1_SCORE, PLAYER_2_SCORE)
print()

if winner == player1Name:
    winnerScore = PLAYER_1_SCORE
else:
    winnerScore = PLAYER_2_SCORE

save_data(winner, winnerScore)
dataBase = load_data()
leaderboard(dataBase)
