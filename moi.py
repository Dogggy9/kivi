from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MainApp(App):
    def build(self):
        lay1 = BoxLayout(orientation='vertical')
        lay2 = BoxLayout(orientation='horizontal')
        lay3 = BoxLayout(orientation='horizontal')
        btn1 = Button(text='кнопка 1')
        btn2 = Button(text='кнопка 2')
        btn3 = Button(text='кнопка 3')
        lay2.add_widget(btn1)
        lay3.add_widget(btn2)
        lay3.add_widget(btn3)
        lay1.add_widget(lay2)
        lay1.add_widget(lay3)

        return lay1

MainApp().run()
