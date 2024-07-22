from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
class HomeScreen(Screen):
    pass
class FirstScreen(Screen):
    pass
class SecondScreen(Screen):
    data = {
        "Python": "language-python",
        "Php": "language-php",
        "Java": "language-java"
    }
class ThirdScreen(Screen):
    def Back(self):
        self.root.current = "home"
class WindowManager(ScreenManager):
    pass
class MySampleApp(MDApp):
    def build(self):
        return Builder.load_file("accordion_carousal.kv")
    def Back(self):
        self.root.current = "home"
        self.root.transition.direction = "right"
if __name__ == "__main__":
    MySampleApp().run()