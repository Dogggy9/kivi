from kivy.app import App
from kivy.uix.togglebutton import ToggleButton

class MainApp(App):
    def build(self):
        my_text = ToggleButton(text='knopka', font_size=50)
        return my_text

MainApp().run()