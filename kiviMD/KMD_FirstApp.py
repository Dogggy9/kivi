from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class MyApp(MDApp):
    def build(self):
        return MDLabel(text='Привет от KivyMD!',
                       font_size=64,
                       halign='center')

app = MyApp()
app.run()