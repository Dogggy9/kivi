from kivy.app import App
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        btn = Button(text='кнопка',
                     size_hint=(.5,.5),
                     pos_hint={'center_x': .5, 'center_y': .5})
        btn.bind(on_press=self.press_button)
        return btn

    def press_button(self, instance):
        print('вы нажали на кнопку!')

MainApp().run()