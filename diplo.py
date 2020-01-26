# A simple program to randomly decide the respective nation of each Diplomacy player
#Prgrammed by Nick Mascitti 

import random 

countries = ["Great Britain", "France", "Italy", "Germany", 
"Austria-Hungary", "Russia", "Ottoman Empire"]

players = []
playerCount = 1

#OBTAIN PLAYERS AND APPEND THEM TO PLAYER LIST
for i in range(7):
	players.append(input(f"ENTER PLAYER {playerCount}'s NAME: "))
	playerCount += 1

print("\n")
#SELECT WHAT COUNTRY WILL GO TO ALL PLAYERS
idx = 0

for i in range(7):
	randomCountry = random.choice(countries)
	print(f"{players[idx]}: {randomCountry}")
	countries.remove(randomCountry)
	idx += 1

print("\n\"In wartime, truth is so precious that she should always be attended by a\
 bodyguard of lies.\"- Winston Churchill\
	\n\nGOOD LUCK GENTLEMEN, THE WORLD IS WATCHING.")