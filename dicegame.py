import random

SCORE_PLAYER1 = 0
SCORE_PLAYER2 = 0

round = 1
N = 0


def show_title():
    print("Welcome to Katarina's Dice Game.")
    print("\n")


def player1_details():
    namePlayer1 = str(input("Player 1, please enter your name: "))
    namePlayer1 = namePlayer1.capitalize()
    print("Welcome,", namePlayer1)

    return namePlayer1


def player2_details():
    namePlayer2 = str(input("Player 2, please enter your name: "))
    namePlayer2 = namePlayer2.capitalize()
    print("Welcome,", namePlayer2)
    print("\n")

    return namePlayer2


def round_display(round):
    print("Please get ready for Round: ", round)
    print("\n")


def player1_rolling(namePlayer1):
    print(namePlayer1, "get ready to roll your dice.")
    player1Input = str(input("Player 1, enter any key to roll your dice: "))

    return player1Input


def player1_roll1(namePlayer1):
    player1FirstResult = random.randint(1, 6)
    print(namePlayer1, "your first dice reads: ", player1FirstResult)

    return player1FirstResult


def player1_roll2(namePlayer1):
    player1SecondResult = random.randint(1, 6)
    print(namePlayer1, "your second dice reads: ", player1SecondResult)
    print("\n")

    return player1SecondResult


def player2_rolling(namePlayer2):
    print(namePlayer2, "get ready to roll your dice.")
    player2Input = str(input("Player 2, enter any key to roll your dice: "))

    return player2Input


def player2_roll1(namePlayer2):
    player2FirstResult = random.randint(1, 6)
    print(namePlayer2, "your first dice reads: ", player2FirstResult)

    return player2FirstResult


def player2_roll2(namePlayer2):
    player2SecondResult = random.randint(1, 6)
    print(namePlayer2, "your second dice reads: ", player2SecondResult)
    print("\n")

    return player2SecondResult


def player1_cumulative_score(namePlayer1, player1FirstResult, player1SecondResult, round):
    player1TotalResult = int(player1FirstResult) + int(player1SecondResult)
    if player1TotalResult % 2 == 0:
        player1Score = player1TotalResult + 10
        print(namePlayer1, "your score after Round",
              round, "is: ", player1Score)
    else:
        player1Score = player1TotalResult - 5
        print(namePlayer1, "your score after Round",
              round, "is: ", player1Score)

    return player1Score


def player2_cumulative_score(namePlayer2, player2FirstResult, player2SecondResult, round):
    player2TotalResult = int(player2FirstResult) + int(player2SecondResult)
    if player2TotalResult % 2 == 0:
        player2Score = player2TotalResult + 10
        print(namePlayer2, "your score after Round",
              round, "is: ", player2Score)
    else:
        player2Score = player2TotalResult - 5
        print(namePlayer2, "your score after Round",
              round, "is: ", player2Score)
    print("\n")

    return player2Score


def winner_decider(namePlayer1, namePlayer2, player1Score, player2Score):
    if player1Score > player2Score:
        print("The winner of this game is: ", namePlayer1)
        winner = namePlayer1
    elif player1Score == player2Score:
        print("The game has ended in a draw. Proceed to the tiebreaker:")
        print("\n")
        tie_breaker(namePlayer1, namePlayer2, player1Score, player2Score)
    else:
        print("The winner of this game is: ", namePlayer2)
        winner = namePlayer2
    print("\n")

    return winner


def winner_score_calculator(winner, player1Score, player2Score):
    if winner == namePlayer1:
        winnerScore = player1Score
    else:
        winnerScore = player2Score

    return winnerScore


def tie_breaker(namePlayer1, namePlayer2, player1Score, player2Score):
    print("Welcome to the tiebreaker.")

    player1Score = 0
    player2Score = 0

    player1Input = str(input("Player 1, enter any key to roll your dice: "))
    player1TBRoll = random.randint(1, 6)
    player2Input = str(input("Player 2, enter any key to roll your dice: "))
    player2TBRoll = random.randint(1, 6)

    print("Player 1, your tiebreaker dice reads: ", player1TBRoll)
    print("Player 2, your tiebreaker dice reads: ", player2TBRoll)

    if player1TBRoll % 2 == 0:
        player1Score = player1TBRoll + 10
        print("Player 1, your score for the tiebreaker is: ", player1Score)
    else:
        player1Score = player1TBRoll - 5
        print("Player 1, your score for the tiebreaker is: ", player1Score)

    if player2TBRoll % 2 == 0:
        player2Score = player2TBRoll + 10
        print("Player 2, your score for the tiebreaker is: ", player2Score)
    else:
        player2Score = player2TBRoll - 5
        print("Player 2, your score for the tiebreaker is: ", player2Score)
    print("\n")

    winner_decider(namePlayer1, namePlayer2, player1Score, player2Score)


def save_winner_details(winner, winnerScore):
    print("Saving Data...")

    file = open("WinnerDetails.txt", "a")
    outputData = winner + "," + str(winnerScore) + "\n"
    file.write(outputData)
    file.close()
    print("\n")


def display_scoreboard():
    file = open("WinnerDetails.txt", "r")
    list = file.read()
    print(list)
    file.close()

#####################################################################


show_title()
namePlayer1 = player1_details()
namePlayer2 = player2_details()

while N < 5:
    round_display(round)

    player1Input = player1_rolling(namePlayer1)
    player1FirstResult = player1_roll1(namePlayer1)
    player1SecondResult = player1_roll2(namePlayer1)

    player2Input = player2_rolling(namePlayer2)
    player2FirstResult = player2_roll1(namePlayer2)
    player2SecondResult = player2_roll2(namePlayer2)

    player1Score = player1_cumulative_score(
        namePlayer1, player1FirstResult, player1SecondResult, round)
    player2Score = player2_cumulative_score(
        namePlayer2, player2FirstResult, player2SecondResult, round)

    round = round + 1
    N = N + 1

if player1Score != player2Score:
    winner = winner_decider(namePlayer1, namePlayer2,
                            player1Score, player2Score)
    winnerScore = winner_score_calculator(winner, player1Score, player2Score)
else:
    tie_breaker(namePlayer1, namePlayer2, player1Score, player2Score)

save_winner_details(winner, winnerScore)
display_scoreboard()
