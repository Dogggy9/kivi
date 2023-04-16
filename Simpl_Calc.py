from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout


KV = '''
Box:

    # корневой виджет
    id: root_widget
    orientation: 'vertical'
    
    # поле ввода исходных данных
    TextInput:
        id: entry
        font_size: 32
        multline: False
        
    # кнопка для выполнения расчета
    Button:
        text: '='
        font_size: 64
        on_press: root_widget.result(entry.text)
        
    # поле для показа результатов
    Label:
        id: itog
        text: 'Итого'
        font_size: 64    
'''

class Box(BoxLayout):
    def result(self, entry_text):
        if entry_text:
            try:
                result = str(eval(entry_text))
                self.ids['itog'].text = result
            except Exception:
                self.ids['itog'].text = 'Ошибка'

class MaynApp(App):
    def build(self):
        return Builder.load_string(KV)

MaynApp().run()
