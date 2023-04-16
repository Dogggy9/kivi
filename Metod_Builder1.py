from kivy.app import App
from kivy.lang.builder import Builder

# создание текстовой строки
my_str = '''
Label:
    text: ('Загрузка метки из текстовой строки')
    font_size: '16pt'
'''

# загрузка кода из текстовой строки
kv_str = Builder.load_string(my_str)

class Basic_Class(App):
    def build(self):
        return kv_str

MyApp = Basic_Class()
MyApp.run()