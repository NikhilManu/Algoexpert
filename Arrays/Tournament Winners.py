"""
"""
"""
We're asked to imagine there is an algorithms tournament taking place in which multiple teams compete against each other. 
In each competition there will be two teams that compete and there will be one winner and one loser out of all of these competitions; there are no ties. 
Each team will compete against all other teams exactly once. Every time a team wins a competition, it gets 3 points; when it loses, it gets 0 points. 
It's guaranteed that the tournament always has at least two teams and there will be only one tournament winner.

We are given two inputs, the competitions array and the results array, and we need to write a function that returns the winner of the tournament, or more specifically, 
the name of the team that has the most number of points. The competitions array is an array of pairs, representing all of the competitions in the tournament. 
Inside of these pairs, we have two strings. The first string is the name of the home team, the second string is the name of the away team. 
The results array represents the winner of each of these competitions. Inside the results array, a 1 means that the home team won and a 0 means the away team won. 
The results array is the same length as the competitions array, and the indices in the results array correspond with the indices in the competitions array.
"""

# O(n) Time and O(k) space where k is number of teams
-----------------------------------
def tournamentWinner(competitions, results):
    	dic = {}
	best = 0
	for team, winner in zip(competitions, results):
		home, away = team
		if winner == 1:
			update(dic, home)
		else:
			update(dic, away)
		
		
    	return max(dic, key = dic.get)

def update(dic, team):
	if team not in dic:
		dic[team] = 0
	dic[team] += 3
