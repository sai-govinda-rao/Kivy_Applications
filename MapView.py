from kivymd.app import MDApp
from kivy.lang import Builder
from kivy_garden.mapview import MapView
class MapApp(MDApp):
    def build(self):
        return Builder.load_file("MapView.kv")
if __name__ == "__main__":
    MapApp().run()