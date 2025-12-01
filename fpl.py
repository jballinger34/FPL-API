from bs4 import BeautifulSoup
import requests

class Player:
    def __init__(self,id,name,team,cost,points,minutes, position):
        self.id = id
        self.name = name
        self.team = team
        self.cost = cost
        self.points = points
        self.minutes = minutes
        self.position = position
    def printStats(self):
        print(self.name + " position: " + self.position + ", team: " + self.team +", costs: " + str(self.cost) + ", points: " + str(self.points))

def sortByPoints(playerList):
    playerList.sort(key=lambda p: p.points, reverse =True)
    return playerList

def sortByPointsOverCost(playerList):
    playerList.sort(key=lambda p: (p.points/p.cost), reverse = True)
    return playerList

def getPosition(playerList, position):
    toReturn = []
    for player in playerList:
        if player.position == position:
            toReturn.append(player)
    return toReturn


teams = [ "Arsenal", "Villa", "Burnley", "Bournemouth",
         "Brentford", "Brighton", "Chelsea", "Palace", "Everton",
         "Fulham", "Leeds", "Liverpool", "Man City", "Man United",
         "Newcastle", "Forest", "Sunderland", "Spurs", "West Ham", "Wolves" ]
positions = ["GK","DEF","MID","FWD"]

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
        minutes = p["minutes"],
        position = positions[p["element_type"]-1]
    ))
#playerList = sortByPoints(playerList)
#playerList[0].printStats()
playerList = getPosition(playerList,"FWD")
playerList = sortByPointsOverCost(playerList)
for x in range(0,10):
    playerList[x].printStats()
