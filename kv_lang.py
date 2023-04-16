from kivy.app import App
from kivy.lang.builder import Builder


KV = '''

'''

class MaynApp(App):
    def build(self):
        return Builder.load_string(KV)

MaynApp().run()
