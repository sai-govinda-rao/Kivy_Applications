from kivymd.app import MDApp
from kivy.lang import Builder
class CardDesignApp(MDApp):
    def build(self):
        return Builder.load_file("CardDesign.kv")
if __name__ == "__main__":
    CardDesignApp().run()