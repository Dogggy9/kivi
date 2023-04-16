from kivy.lang.builder import Builder
from kivy.app import App

KV = '''
BoxLayout:
    Button:
        id: bnt
        text: 'Knopka'
        on_press: app.status(txt.text)
        on_release: app.status(bnt.state)
    TextInput:
        id: txt
        text: bnt.state
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

    def status(self, stt):
        print('Sostoyanie - '+ stt)

MainApp().run()