from kivy.app import App
# from kivy.lang import Builder
from kivy.lang.builder import Builder

KV = '''
BoxLayout:
    orientation: 'vertical'
    Button:
        text: root.orientation
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()