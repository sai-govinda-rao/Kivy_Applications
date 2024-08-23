from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.core.window import Window
class HomeScreen(Screen):
    pass
class FirstScreen(Screen):
    def on_enter(self, *args):
        stories_list = ["Story","Animal","Donkey","Lion"]
        for i in stories_list:
            item = OneLineListItem(text=i,on_release=lambda instance,story_name=i:self.Change(story_name))
            self.ids.id_list.add_widget(item)
    def on_leave(self, *args):
        self.ids.id_list.clear_widgets()
    def Change(self,name):
        self.manager.get_screen("second").ScrollStory(name)
        self.manager.current = "second"
class SecondScreen(Screen):
    def back(self):
        self.manager.current = "first"
        self.manager.transition.direction = "right"
    def ScrollStory(self,name):
        file = open(f"{name}", "r")
        story = file.read()
        self.ids.label_text.text = f"{story}"
    def Slide(self,*args):
        self.ids.label_text.font_size = f"{args[1]}"
class WindowScreen(ScreenManager):
    pass
class MyListStoriesApp(MDApp):
    def Back(self):
        self.root.current = "home"
        self.root.transition.direction = "right"
    def build(self):
        Window.size = 300,500
        return Builder.load_file("EnglishStoriesApp.kv")
MyListStoriesApp().run()