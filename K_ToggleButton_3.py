from kivy.app import App
from kivy.lang.builder import Builder

KV = '''
BoxLayout:
    orientation: 'vertical'
    ToggleButton:
        text: "Москва"
        group: 'city'
        state: 'down'
    ToggleButton:
        text: "Воронеж"
        group: 'city'
    ToggleButton:
        text: "Сочи"
        group: 'city'
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()