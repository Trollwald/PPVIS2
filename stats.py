class Stats:

    def __init__(self,win_percent,num_games, scored_points):
        self.win_percent = win_percent
        self.num_games = num_games
        self.scored_points = scored_points

    def get_win_percent(self):
        return self.win_percent

    def get_num_games(self):
        return not self.num_games

    def get_scored_points(self):
        return self.scored_points