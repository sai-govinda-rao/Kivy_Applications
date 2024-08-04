from kivymd.app import MDApp
from kivy.lang import Builder
from deep_translator import GoogleTranslator
import arabic_reshaper
from bidi.algorithm import get_display
#global from_lang, to_lang
from_lang = "lang"
to_lang = "lang"
language_ttf_dict = {
            "Telugu" : "C:\\Users\\srini\\OneDrive\\Desktop\\Langs\\Telugu.ttf",
            "Hindi": "C:\\Users\\srini\\OneDrive\\Desktop\\Langs\\Hindi.ttf",
            "Arabic": "C:\\Users\\srini\\OneDrive\\Desktop\\Langs\\Arabic.ttf",
            "English": "C:\\Users\\srini\\OneDrive\\Desktop\\Langs\\Hindi.ttf"
        }
class TranslatorApp(MDApp):
    def Select_from(self, val):
        global from_lang, language_ttf_dict
        from_lang = val
        self.root.ids.translate_input.font_name = language_ttf_dict[from_lang]
    def Select_to(self, val):
        global to_lang, language_ttf_dict
        to_lang = val
        self.root.ids.translate_output.font_name = language_ttf_dict[to_lang]
    def Translate(self):
        try:
            language_dict = \
            {
                            "Telugu": "te",
                            "English": "en",
                            "Hindi": "hi",
                            "Sanskrit": "sa",
                            "Kannada": "kn",
                            "Arabic": "ar",
                            "Nepali": "ne",
                            "Marathi": "mr",
                            "Dutch": "nl",
                            "German": "de",
                            "Norwegian": "no",
                            "French": "fr",
                            "Latin": "la",
                            "Italian": "it",
                            "Spanish": "es",
                            "Romanian": "ro",
                            "Mizo(Mizoram)": "lus",
                            "Zulu(SouthAfrica)": "zu",
                            "Esperanto(UK)": "eo"
            }
            global from_lang, to_lang
            text = self.root.ids.translate_input.text
            if from_lang != "lang" and to_lang != "lang" and text != "":
                translator = GoogleTranslator(source=language_dict[from_lang], target=language_dict[to_lang])
                translation = translator.translate(text)
                self.root.ids.translate_output.text = f"{translation}"
            else:
                pass
        except:
            pass
    def Clear(self):
        self.root.ids.translate_input.text = ""
        self.root.ids.translate_output.text = ""
    def build(self):
        return Builder.load_file("LanguageTranslator.kv")
if __name__ == "__main__":
    TranslatorApp().run()