from kivy.app import App
from kivy.uix.button import Button

class Basic_Class1(App):
    def build(self):
        btn = Button(text='кнопка',
                     size_hint=(.5, .5),
                     pos_hint={'center_x': .5, 'center_y': .5})
        return btn

    def press_button(self):
        print("вы нажали на кнопку")

my_app = Basic_Class1()
my_app.run()