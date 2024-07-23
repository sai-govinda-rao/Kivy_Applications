from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
class Home(Screen):
    pass
class First(Screen):
    pass
class WindowScreen(ScreenManager):
    pass
class DrawerApp(MDApp):
    def back(self):
        self.root.current = "home"
        self.root.transition.direction = "right"
    def dictionary(self):
        self.root.current = "first"
        self.root.transition.direction = "left"
    def build(self):
        return Builder.load_file("App.kv")
if __name__ == "__main__":
    DrawerApp().run()