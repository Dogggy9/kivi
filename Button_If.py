from kivy.app import App
from kivy.lang.builder import Builder


KV = '''
BoxLayout:
    orientation: 'vertical'
    Button:
        id: bt1
        text: 'кнопка 1'
    Label:
        text: 'отпущена' if bt1.state == 'normal' else 'нажата'
'''

class MaynApp(App):
    def build(self):
        return Builder.load_string(KV)

MaynApp().run()
