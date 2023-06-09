from kivy.app import App
from kivy.lang.builder import Builder

KV = '''
Button:
    text: 'Это кнопка'
    size_hint: None, None
    # size_hint: .5, .5
    # ----------------------
    # size_hint: .8, .5
    # size_hint: .5, .8
    
    pos_hint: {'x': .5, 'y': .5}
    # -------------------------------------------
    # size_hint: .2, .1
    # pos_hint: {'center_x': .15, 'center_y': .5}
    # pos_hint: {'center_x': .85, 'center_y': .5}
    # pos_hint: {'center_x': .5, 'center_y': .15}
    # pos_hint: {'center_x': .5, 'center_y': .85}
    size: 150, 150
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()