from kivy.app import App
from kivy.lang.builder import Builder

kv_file = Builder.load_file('./KV_file/main_screen.kv')

class Basic_Class(App):
    def build(self):
        return kv_file

MyApp = Basic_Class()
MyApp.run()