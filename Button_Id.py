from kivy.app import App
from kivy.lang.builder import Builder

KV = '''
BoxLayout:
    orientation: 'vertical'
    Button:
        id: bt1
        text: 'Кнопка 1'
        on_press: lb1.text = bt1.text
    Button:
        id: bt2
        text: 'Кнопка 2'
        on_press: lb1.text = bt2.text
    Label:
        id: lb1
        text: 'Метка'
        on_touch_down: self.text = 'метка'
'''

class MaynApp(App):
    def build(self):
        return Builder.load_string(KV)

MaynApp().run()