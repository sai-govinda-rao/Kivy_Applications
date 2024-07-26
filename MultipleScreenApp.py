import logging
import requests
logging.getLogger("requests").setLevel(logging.WARNING)
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy_garden.mapview import MapView
from kivy.uix.screenmanager import ScreenManager,Screen

class HomeScreen(Screen):
    def clear(self):
        self.ids.name.text = ""
        self.ids.password.text = ""
class WelcomeScreen(Screen):
    pass
class FirstScreen(Screen):
    pass
class SecondScreen(Screen):
    pass
class ThirdScreen(Screen):
    pass
class WindowScreen(ScreenManager):
    pass
class SampleApp(MDApp):
    def Theme(self):
        pass

    def build(self):
        self.theme_cls.theme_style = "Light"
        return Builder.load_file("MultipleScreenApp.kv")
    def back(self):
        self.root.current = "home"
        self.root.transition.direction = "right"
    def Back(self):
        self.root.current = "welcome"
        self.root.transition.direction = "right"
if __name__ == "__main__":
    SampleApp().run()