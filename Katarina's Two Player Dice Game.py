import random

ScorePlayer1 = 0
ScorePlayer2 = 0

Round = 1 
N = 0

def ShowTitle():
  print("Welcome to Katarina's Dice Game.")
  print("\n")

def Player1Details():
  NamePlayer1 = str(input("Player 1, please enter your name: "))
  NamePlayer1 = NamePlayer1.capitalize()
  print("Welcome,", NamePlayer1)
  
  return NamePlayer1

def Player2Details():
  NamePlayer2 = str(input("Player 2, please enter your name: "))
  NamePlayer2 = NamePlayer2.capitalize()
  print("Welcome,", NamePlayer2)
  print("\n")
  
  return NamePlayer2

def RoundDisplay(Round):
  print("Please get ready for Round: ", Round)
  print("\n")

def Player1Rolling(NamePlayer1):
  print(NamePlayer1, "get ready to roll your dice.")
  Player1Input = str(input("Player 1, enter any key to roll your dice: "))

  return Player1Input

def Player1Roll1(NamePlayer1):
  Player1FirstResult = random.randint(1,6)
  print(NamePlayer1, "your first dice reads: ", Player1FirstResult)
  
  return Player1FirstResult

def Player1Roll2(NamePlayer1):
  Player1SecondResult = random.randint(1,6)
  print(NamePlayer1, "your second dice reads: ", Player1SecondResult)
  print("\n")

  return Player1SecondResult

def Player2Rolling(NamePlayer2):
  print(NamePlayer2, "get ready to roll your dice.")
  Player2Input = str(input("Player 2, enter any key to roll your dice: "))

  return Player2Input

def Player2Roll1(NamePlayer2):
  Player2FirstResult = random.randint(1,6)
  print(NamePlayer2, "your first dice reads: ", Player2FirstResult)

  return Player2FirstResult

def Player2Roll2(NamePlayer2):
  Player2SecondResult = random.randint(1,6)
  print(NamePlayer2, "your second dice reads: ", Player2SecondResult)
  print("\n")

  return Player2SecondResult

def Player1CumulativeScore(NamePlayer1, Player1FirstResult, Player1SecondResult, Round):
  Player1TotalResult = int(Player1FirstResult) + int(Player1SecondResult)
  if Player1TotalResult % 2 == 0:
    Player1Score = Player1TotalResult + 10
    print(NamePlayer1, "your score after Round", Round, "is: ", Player1Score)
  else:
    Player1Score = Player1TotalResult - 5
    print(NamePlayer1, "your score after Round", Round, "is: ", Player1Score)
  
  return Player1Score

def Player2CumulativeScore(NamePlayer2, Player2FirstResult, Player2SecondResult, Round):
  Player2TotalResult = int(Player2FirstResult) + int(Player2SecondResult)
  if Player2TotalResult % 2 == 0:
    Player2Score = Player2TotalResult + 10
    print(NamePlayer2, "your score after Round", Round, "is: ", Player2Score)
  else:
    Player2Score = Player2TotalResult - 5
    print(NamePlayer2, "your score after Round", Round, "is: ", Player2Score)
  print("\n")

  return Player2Score

def WinnerDecider(NamePlayer1, NamePlayer2, Player1Score, Player2Score):
  if Player1Score > Player2Score:
    print("The winner of this game is: ", NamePlayer1)
    Winner = NamePlayer1
  elif Player1Score == Player2Score:
    print("The game has ended in a draw. Proceed to the tiebreaker:")
    print("\n")
    TieBreaker(NamePlayer1, NamePlayer2, Player1Score, Player2Score)
  else:
    print("The winner of this game is: ", NamePlayer2)
    Winner = NamePlayer2
  print("\n")

  return Winner

def WinnerScoreCalculator(Winner, Player1Score, Player2Score):
  if Winner == NamePlayer1:
    WinnerScore = Player1Score
  else:
    WinnerScore = Player2Score

  return WinnerScore

def TieBreaker(NamePlayer1, NamePlayer2, Player1Score, Player2Score):
  print("Welcome to the tiebreaker.")

  Player1Score = 0
  Player2Score = 0

  Player1Input = str(input("Player 1, enter any key to roll your dice: "))
  Player1TBRoll = random.randint(1,6)
  Player2Input = str(input("Player 2, enter any key to roll your dice: "))
  Player2TBRoll = random.randint(1,6)

  print("Player 1, your tiebreaker dice reads: ", Player1TBRoll)
  print("Player 2, your tiebreaker dice reads: ", Player2TBRoll) 

  if Player1TBRoll % 2 == 0:
    Player1Score = Player1TBRoll + 10
    print("Player 1, your score for the tiebreaker is: ", Player1Score)
  else:
    Player1Score = Player1TBRoll - 5
    print("Player 1, your score for the tiebreaker is: ", Player1Score)
  
  if Player2TBRoll % 2 == 0:
    Player2Score = Player2TBRoll + 10
    print("Player 2, your score for the tiebreaker is: ", Player2Score)
  else:
    Player2Score = Player2TBRoll - 5
    print("Player 2, your score for the tiebreaker is: ", Player2Score)
  print("\n")

  Winner = WinnerDecider(NamePlayer1, NamePlayer2, Player1Score, Player2Score)

def SaveWinnerDetails(Winner, WinnerScore):
  print("Saving Data...")

  file = open("WinnerDetails.txt", "a")
  OutputData = Winner + "," + str(WinnerScore) + "\n"
  file.write(OutputData)
  file.close()
  print("\n")

def DisplayScoreboard():
  file = open("WinnerDetails.txt", "r")
  List = file.read()
  print(List)
  file.close()

#####################################################################

ShowTitle()
NamePlayer1 = Player1Details()
NamePlayer2 = Player2Details()

while N < 5:
  RoundDisplay(Round)

  Player1Input = Player1Rolling(NamePlayer1)
  Player1FirstResult = Player1Roll1(NamePlayer1)
  Player1SecondResult = Player1Roll2(NamePlayer1)

  Player2Input = Player2Rolling(NamePlayer2)
  Player2FirstResult = Player2Roll1(NamePlayer2)
  Player2SecondResult = Player2Roll2(NamePlayer2)

  Player1Score = Player1CumulativeScore(NamePlayer1, Player1FirstResult, Player1SecondResult, Round)
  Player2Score = Player2CumulativeScore(NamePlayer2, Player2FirstResult, Player2SecondResult, Round)

  Round = Round + 1
  N = N + 1

if Player1Score != Player2Score:
  Winner = WinnerDecider(NamePlayer1, NamePlayer2, Player1Score, Player2Score)
  WinnerScore = WinnerScoreCalculator(Winner, Player1Score, Player2Score)
else:
  TieBreaker(NamePlayer1, NamePlayer2, Player1Score, Player2Score)

SaveWinnerDetails(Winner, WinnerScore)
DisplayScoreboard()
