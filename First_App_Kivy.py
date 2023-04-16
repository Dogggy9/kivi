from kivy.app import App # Импорт фреймврка kivy
from kivy.uix.label import Label # импорт визуального элемента label

class MainApp(App):
    def build(self):
        return Label(text='Привет от Kivy!')

app = MainApp(title='Первое приложение на Kivy') # Задание имени
app.run()