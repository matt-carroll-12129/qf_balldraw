import random 

teams = {
		1: "Manchester United", 2 : "Manchester City", 3: "Liverpool", 4: "Tottenham",
		5: "Barcelona", 6: "Porto", 7: "Ajax", 8: "Juventus"
		}

ballorder = list(range(1,9))
random.shuffle(ballorder)
matchups = int((len(ballorder) /2))

teamorder = []
for x in ballorder:
	teamorder.append(teams.get(x))

def print_matchups():
	print(teamorder.pop(0), " vs ", teamorder.pop(0))

for x in range(matchups):
	print_matchups()

