from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty
Builder.load_file("loginapp.kv")
class AppInterFace(Widget):
    #name = ObjectProperty(None)
    #password = ObjectProperty(None)
    def press(self):
        name = self.name.text
        password = self.password.text
        if name != "" and password != "":
            password = int(password)
            pass_word = 1432
            if password == pass_word and password != "":
                print(f"Mr.{name} Your Account Successfully LogIn")
            else:
                print("Invalid Password")
        else:
            print("Enter Your Details")
        self.name.text = ""
        self.password.text = ""
class MainApp(App):
    def build(self):
        Window.clearcolor = "white"
        return AppInterFace()
if __name__ == "__main__":
    MainApp().run()