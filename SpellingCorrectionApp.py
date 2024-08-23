from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.spelling import Spelling
class SpellingCorrectionApp(MDApp):
    def Check(self):
        spell = Spelling()
        spell.select_language("en_US")
        word = self.root.ids.input_text.text.title()
        if word != "":
            self.root.ids.input_text.text = ""
            suggest_word = spell.suggest(word)
            if word in suggest_word:
                self.root.ids.label.text = f"Your Spelling Is Correct"
            else:
                related_words = ""
                for i in suggest_word:
                    related_words += f"{i}, "
                self.root.ids.label.text = f"Here Are Some Related Words\n{related_words}"
        else:
            self.root.ids.label.text = f"You Didn't Enter Word"
    def build(self):
        return Builder.load_file("SpellingCorrectionApp.kv")
if __name__ == "__main__":
    SpellingCorrectionApp().run()