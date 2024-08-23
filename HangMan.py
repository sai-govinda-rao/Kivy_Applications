from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.core.window import Window
from HangMan_Diagrams import figures
Window.size = (400,600)
class HomeScreen(Screen):
    pass
class GameScreen(Screen):

    def back(self):
        self.manager.current = "home"
        self.manager.transition.direction = "right"
    def Start(self):
        self.ids.game_label.text = f"HangMan Game\nPlay Carefully\nYou Are Playing With My Life"
        global count, display, word, lifes
        import random
        file = open("animal_names", "r")
        file_content = file.read()
        animals = file_content.split(",")
        animals_list = []
        lifes = 6
        for i in animals:
            animals_list.append(i)
        random_word = random.choice(animals_list)
        word = random_word.lower()
        count = len(word)
        display = []
        for i in range(count):
            display += "_"
        result = ""
        for i in display:
            result += f"{i} "
        self.ids.hint_label.text = f"{result}"
    def Hangman(self,instance):
        global count, display, word,lifes
        game = True
        guessed_letter = (self.ids.input_label.text).lower()
        if guessed_letter != "":
            self.ids.input_label.text = ""
            for position in range(count):
                letter = word[position]
                if letter == guessed_letter:
                    display[position] = guessed_letter
            result = ""
            for i in display:
                result += f"{i} "
            self.ids.hint_label.text = f"{result}"
            if guessed_letter not in word:
                lifes -= 1
                self.ids.game_label.text = f"{figures[lifes]}"
                if lifes == 0:
                    game = False
                    self.ids.hint_label.text = f"You Lose\n{word}"
            if "_" not in display:
                self.ids.hint_label.text = f"You Won"
                game = False
        else:
            pass
class WindowManager(ScreenManager):
    pass
class HangmanGame(MDApp):
    def build(self):
        return Builder.load_file("HangMan.kv")
if __name__ == "__main__":
    HangmanGame().run()