from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
import math
import pandas as pd
class HomeScreen(Screen):
    pass
class FirstScreen(Screen):
    pass
class SecondScreen(Screen):
    pass
class ThirdScreen(Screen):
    def Correlation_find(self):
        a = self.ids.x.text
        b = self.ids.y.text
        if a == "" and b == "":
            self.ids.label_text.text = f"You didn't Enter Data"
        else:
            c = a.split(" ")
            d = b.split(" ")
            count_1 = 0
            past_data_1 = []
            for i in c:
                count_1 += 1
                i = int(i)
                past_data_1.append(i)
            count_2 = 0
            past_data_2 = []
            for j in d:
                count_2 += 1
                j = int(j)
                past_data_2.append(j)
            def finding_x_values():
                summation_x = 0
                for i in past_data_1:
                    summation_x += i
                x_bar = summation_x/count_1
                x_values = []
                for i in past_data_1:
                    x_values.append(i-x_bar)
                x_square_values = []
                for i in x_values:
                    x_square_values.append(i**2)
                summation_x_square = 0
                for i in x_square_values:
                    summation_x_square += i
                return x_values,x_square_values,summation_x_square
            def finding_y_values():
                summation_y = 0
                for i in past_data_2:
                    summation_y += i
                y_bar = summation_y/count_2
                y_values = []
                for i in past_data_2:
                    y_values.append(i-y_bar)
                y_square_values = []
                for i in y_values:
                    y_square_values.append(i**2)
                summation_y_square = 0
                for i in y_square_values:
                    summation_y_square += i
                return y_values,y_square_values,summation_y_square
            if count_1 == count_2:
                x_values,x_square_values,summation_x_square = finding_x_values()
                y_values,y_square_values,summation_y_square = finding_y_values()
                xy_values = []
                summation_xy = 0
                for i,j in zip(x_values,y_values):
                    xy_values.append(i*j)
                    summation_xy += (i*j)
                correlation = summation_xy/math.sqrt(summation_x_square*summation_y_square)
                data = {
                    "A": past_data_1,
                    "B": past_data_2,
                    "X-Values": x_values,
                    "Y-Values": y_values,
                    "XY-Values": xy_values,
                    "X-Square": x_square_values,
                    "Y-Square": y_square_values
                }
                table = pd.DataFrame(data)
                self.ids.label_text.text = f"{table}\nCorrelation : {correlation}"
            else:
                self.ids.label_text.text = f"Enter Valid Data"

class WindowScreen(ScreenManager):
    pass
class CorrelationApp(MDApp):
    def Back(self):
        self.root.current = "home"
        self.root.transition.direction = "right"
    def build(self):
        return Builder.load_file("CorrelationApp.kv")
if __name__ == "__main__":
    CorrelationApp().run()