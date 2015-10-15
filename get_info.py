__author__='edinkelspiel'

game_location = None

class Team:

    def __init__(self, roster, record, location):
        self.roster = roster
        self.record = record
        self.location = location

    def is_home(self, location):
        return game_location == location

    def get_starters(self, roster):
        starter_list = []
        for player in roster:
            if player.starter == True:
                starter_list.append(player)



class Player:
    def __init__(self, team, stats, starter=False, position=None):
        self.team = team
        self.stats = stats
        self.starter = starter
        self.position = position

    def set_as_starter(self, position_input):
        position = position_input
        starter = True
