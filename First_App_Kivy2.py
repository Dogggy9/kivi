from kivy.app import App # Импорт фреймврка kivy
from kivy.uix.label import Label # импорт визуального элемента label

class MainApp(App):
    def build(self):
        self.title = "Приложение на Kivy"
        self.icon = 'Support.ico'
        label = Label(text='Привет от Kivy и Python!')
        return label

if __name__ == '__main__':
    app = MainApp()
    app.run()