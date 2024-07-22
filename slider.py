from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.slider import Slider
Builder.load_file("slider.kv")
class SliderApp(Widget):
    def slide(self,*args):
        self.ids.label_text.text = str(args[1])
        self.ids.label_text.font_size = str(args[1]*5)
class MyApp(App):
    def build(self):
        #Window.clearcolor = (1,1,1,1)
        return SliderApp()
if __name__ == "__main__":
    MyApp().run()