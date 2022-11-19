class Team:

    def __init__(self,id, name, statistics =''):
        self.id = id
        self.name = name
        self.players = []
        self.statistics = statistics

    def add_player(self, player):
        self.players.append(player)

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_statistics(self):
        return self.statistics

    def get_players(self):
        return self.players

