from kivy.app import App
from kivy.lang.builder import Builder

KV = '''
BoxLayout:
    orientation: 'vertical'
    Button:
        text: 'кнопка 1'
        on_press: app.press_button(self.text)
    Button:
        text: 'кнопка 2'
        on_press: app.press_button(self.text)
    Label:
        text: app.name
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

    def press_button(self, instance):
        print('Вы нажали на кнопку!')
        print(instance)

MainApp().run()
