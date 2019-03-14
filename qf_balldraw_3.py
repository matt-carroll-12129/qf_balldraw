import random 
import time 

teams = [ "Manchester United", "Manchester City", "Liverpool", "Tottenham", "Barcelona", "Porto", "Ajax", "Juventus"]

ties = ["first", "second", "third", "final"]
 
def draw_ball(): 
	draw = random.choice(teams)
	return(teams.pop(teams.index(draw)))

print("Good Evening ladies and gentlemen. The ties are as follows.")

for tie in ties: 
	time.sleep(5)
	print("The {} tie is {} vs {}".format(tie, draw_ball(), draw_ball()))




