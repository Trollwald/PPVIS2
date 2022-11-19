from kivy.config import Config
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from Screens import *

Config.set('graphics', 'resizable', '0')

Builder.load_file("/Users/johnmg/Downloads/PPVIS-2/my.kv")


class MyMainApp(App):
    Window.clearcolor = (.67,.73,.89,1)
    def build(self):
        self.title="Main Window"
        Window.size = (450, 600)
        sm = ScreenManager()
        sm.add_widget(StartWindow(name='start'))
        sm.add_widget(Registration_coach(name='registration_coach'))
        sm.add_widget(Registration_player(name='registration_player'))
        sm.add_widget(Login(name='login'))
        sm.add_widget(PersonalDataForCoach(name='coach_data'))
        sm.add_widget(PersonalDataForPlayer(name='player_data'))
        sm.add_widget(FindTeamForPlayer(name='find_team_player'))
        sm.add_widget(MobileCoachForPlayer(name='coach_player'))
        sm.add_widget(MobileCoachForCoach(name = 'coach_coach'))
        sm.add_widget(FindTeamForCoach(name='find_team_coach'))
        return sm

