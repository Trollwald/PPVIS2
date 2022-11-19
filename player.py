from team import Team

class Player:

    def __init__(self,id,password,email,name):
        self.id = id
        self.password = password
        self.email = email
        self.name = name
        self.stats = None
        self.physical_data = None
        self.team = []

    def add_team(self, team):
        self.team.append(team)

    def confirm_authorization(self):
        pass

    def get_id(self):
        return self.id

    def get_password(self):
        return self.password

    def get_email(self):
        return self.email

    def get_name(self):
        return self.name

    def get_team(self):
        return self.team

    def get_stats(self):
        return self.stats

    def get_physical_data(self):
        return self.physical_data