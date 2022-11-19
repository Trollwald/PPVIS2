from kivy.uix.screenmanager import Screen
from team import Team
from player import Player
from physical_data import PhysicalData
from stats import Stats
from training_plan import ExercisePlan
from exercise import Exercise

class PersonalDataForCoach(Screen):
    __team: Team
    __player: list[Player]

    def change_team_name(self):
        pass
    def change_player(self):
        pass
    def show_players(self):
        pass

class Login(Screen):

    def ask_login(self):
        pass

    def ask_password(self):
        pass

class StartWindow(Screen):
    def checkbox_click(self, instance, value):
        if value is True:
            print("Checkbox Checked")
        else:
            print("Checkbox Unchecked")

class PersonalDataForPlayer(Screen):
    __personal_data: PhysicalData
    __statistics: Stats

    def show_physical_data(self):
        pass
    def show_statistics(self):
        pass

class Registration_coach(Screen):
    def ask_login(self):
        pass

    def ask_password(self):
        pass

    def ask_personal_data(self):
        pass

class Registration_player(Screen):
    def ask_login(self):
        pass

    def ask_password(self):
        pass

    def ask_personal_data(self):
        pass

class FindTeamForPlayer(Screen):
    __team: list[Team]

    def request_to_join(self):
        pass
    def accept_request_from_coach(self):
        pass

class MobileCoachForPlayer(Screen):
    __exercise_plan: ExercisePlan

    def create_training_plan(self):
        pass

    def show_training_plan(self):
        pass

class MobileCoachForCoach(Screen):
    __exercise_list: list[Exercise]

    def add_exercise(self):
        pass

    def delete_exercise(self):
        pass

    def change_exercise(self):
        pass

    def show_list_of_exercises(self):
        pass

class FindTeamForCoach(Screen):
    __player: list[Player]

    def request_to_join(self):
        pass

    def accept_request_from_player(self):
        pass