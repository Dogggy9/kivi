from kivymd.app import MDApp
from kivy.lang.builder import Builder

KV = '''
MDScreen:
    MDCard:
        orientation: 'vertical'
        padding: '8dp'
        size_hint: None, None
        size: '280dp', '180dp'
        pos_hint: {'center_x': .5, 'center_y': .5}
        
        MDLabel:
            text: 'Заголовок'
            theme_text_color: 'Secondary'
            size_hint_y: None
            height: self.texture_size[1]
        MDSeparator:
            height: '1dp'
        
        MDLabel:
            text: 'Тело карточки'
'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MyApp().run()