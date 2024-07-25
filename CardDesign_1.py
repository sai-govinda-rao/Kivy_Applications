from kivymd.app import MDApp
from kivy.lang import Builder
class CardDesignLogInApp(MDApp):
    def build(self):
        return Builder.load_file("CardDesing_1.kv")
if __name__ == "__main__":
    CardDesignLogInApp().run()