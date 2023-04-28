from kivymd.app import MDApp  # Импорт фреймврка kivy
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder

KV = '''
MDStackLayout:
    padding: "10dp"
    spacing: "10dp"
    # adaptive_height: True
    # adaptive_width: True
    adaptive_size: True
    # md_bg_color: app.theme_cls.primary_color
    
    MDRaisedButton:
        text: "Кнопка 1"
    MDRaisedButton:
        text: "Кнопка 2"
    MDRaisedButton:
        text: "Кнопка 3"
    MDRaisedButton:
        text: "Кнопка 4"
        
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()
