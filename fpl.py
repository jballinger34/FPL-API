from bs4 import BeautifulSoup
import requests

class Player:
    def __init__(self,id,name,team,cost,points,minutes):
        self.id = id
        self.name = name
        self.team = team
        self.cost = cost
        self.points = points
        self.minutes = minutes
    def printStats(self):
        print(self.name)

def sortByPoints(playerList):
    playerList.sort(key=lambda p: p.points, reverse =True)
    return playerList

def sortByPointsOverCost(playerList):
    playerList.sort(key=lambda p: (p.points/p.cost), reverse = True)
    return playerList
teams = [ "Arsenal", "Villa", "Burnley", "Bournemouth",
         "Brentford", "Brighton", "Chelsea", "Palace", "Everton",
         "Fulham", "Leeds", "Liverpool", "Man City", "Man United",
         "Newcastle", "Forest", "Sunderland", "Spurs", "West Ham", "Wolves" ]
"""
url = "https://fantasy.premierleague.com/api/fixtures/"
fixtures = requests.get(url).json()


for fixture in fixtures:
    if fixture["finished"]:
        print(fixture["kickoff_time"] + " " + teams[fixture["team_h"]-1] + " " + str(fixture["team_h_score"]) + " - " + str(fixture["team_a_score"]) + " " +teams[fixture["team_a"] -1])
    else:
        print(fixture["kickoff_time"] + " " + teams[fixture["team_h"]-1] + " v " + teams[fixture["team_a"] -1])
"""

url2 = "https://fantasy.premierleague.com/api/bootstrap-static/"
res = requests.get(url2).json()

#print(res["chips"])

#gameweek general stats
#for x in res["events"]:
#    print(x)

#player stats
#for x in res["elements"]:
#    print(x)


playerList = []
for p in res["elements"]:
    playerList.append(Player(
        id = 23,
        name = p["first_name"] + " " + p["second_name"],
        team = teams[p["team"]-1],
        cost = p["now_cost"],
        points = p["total_points"],
        minutes = p["minutes"]
    ))

playerList = sortByPoints(playerList)
playerList[0].printStats()
playerList = sortByPointsOverCost(playerList)
playerList[0].printStats()
