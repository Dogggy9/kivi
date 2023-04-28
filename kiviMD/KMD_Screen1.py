from kivymd.app import MDApp
from kivy.lang.builder import Builder
# from kivymd.uix.toolbar.toolbar import To

KV = '''
Screen:
    MDTopAppBar:
        title: 'Приложение на KivyMD'
        elevation: 10
        md_bg_color: app.theme_cls.primary_color
        left_action_items: [['menu', lambda x: x]]
        pos_hint: {'top': 1}
        
    MDRaisedButton:
        text: 'Кнопка KivyMD'
        pos_hint: {'center_x': .5, 'center_y': .5}
'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MyApp().run()