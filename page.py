from kivy.app import App
from kivy.lang.builder import Builder

KV = '''
<MyBtn@Button>
    size_hint_y: None
    height: 40
    
ScrollView:
    do_scroll_x: False
    do_scroll_y: True
    
    GridLayout:
        cols: 1
        spacing: 10
        size_hint_y: None
        height: self.minimum_height
        
        MyBtn:
            text: 'knopka 1'
        MyBtn:
            text: 'knopka 2'
        MyBtn:
            text: 'knopka 3'
        MyBtn:
            text: 'knopka 4'
        MyBtn:
            text: 'knopka 5'
        MyBtn:
            text: 'knopka 6'
        MyBtn:
            text: 'knopka 7'
        MyBtn:
            text: 'knopka 8'
        MyBtn:
            text: 'knopka 9'
        MyBtn:
            text: 'knopka 10'
        MyBtn:
            text: 'knopka 11'
        MyBtn:
            text: 'knopka 12'
        MyBtn:
            text: 'knopka 13'
        MyBtn:
            text: 'knopka 14'
        MyBtn:
            text: 'knopka 15'
        MyBtn:
            text: 'knopka 16'
        MyBtn:
            text: 'knopka 17'
        MyBtn:
            text: 'knopka 18'
        MyBtn:
            text: 'knopka 19'
        MyBtn:
            text: 'knopka 20'
'''

class MyApp(App):
    def build(self):
        return Builder.load_string(KV)

MyApp().run()