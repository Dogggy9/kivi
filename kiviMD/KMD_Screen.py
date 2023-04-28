from kivymd.uix.label import MDLabel
from kivymd.app import MDApp
from kivymd.uix.button.button import MDRectangleFlatButton
from kivy.uix.screenmanager import Screen
from kivymd.uix.screen import MDScreen

class MyApp(MDApp):
    def build(self):
        screen = MDScreen()
        screen.add_widget(MDLabel(text='Привет от KivyMD!',
                                  halign='center'))
        screen.add_widget(MDRectangleFlatButton(
            text='Кнопка KMD', pos_hint={ 
                'center_x': 0.5,'center_y': 0.4}))
        return screen

MyApp().run()