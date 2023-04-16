from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

KV = '''
<MyButton@Button>:
    pos_hint: {'center_x':.5, 'center_y':.6}
    font_size: '25sp'
    markup: True
    
BoxLayout:
    orientation: 'vertical'
    MyButton:
        text: 'кнопка1'
    MyButton:
        text: 'кнопка2'
    MyButton:
        text:'кнопка3'
'''

# class MyBox(BoxLayout):
#     pass

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()