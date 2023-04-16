from kivy.app import App
from kivy.uix.label import Label
from kivy.lang.builder import Builder

KV = '''
Label:
    text: 'Это текст'
    font_size: 50
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()