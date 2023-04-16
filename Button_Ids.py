from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout


KV = '''
Box:
    Button:
        text: 'Кнопка'
        on_press: root.result('нажата кнопка')
    Label:
        id: itog
        on_touch_down: self.text = 'lopata'
'''

class Box(BoxLayout):
    def result(self, entry_text):
        self.ids['itog'].text = entry_text

class MaynApp(App):
    def build(self):
        return Builder.load_string(KV)

MaynApp().run()
