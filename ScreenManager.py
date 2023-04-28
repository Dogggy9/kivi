from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

KV = '''
WindowManager:
    MainWindow:
    Screen_2:
    Screen_3:
    
<MainWindow>:
    name: 'main'
    
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Главный экран'
        Button:
            text: 'К экрану 2 ->'
            size_hint: (.2,.1)
            on_release:
                app.root.current = 'second'
                root.manager.transition.direction = 'left'
                
<Screen_2>
    name: 'second'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Это второй экран'
        Button:
            text: '<- Назад'
            size_hint: (.2,.1)
            on_release:
                app.root.current = 'main'
                root.manager.transition.direction = 'right'
        Button:
            text: 'К экрану 3 ->'
            size_hint: (.2,.1)
            on_release:
                app.root.current = 'third'
                root.manager.transition.direction = 'left'
                
<Screen_3>
    name: 'third'
    
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Это третий экран'
        Button:
            text: '<- Назад'
            size_hint: (.2,.1)
            on_release:
                app.root.current = 'second'
                root.manager.transition.direction = 'right'
'''

class MainWindow(Screen):
    pass

class Screen_2(Screen):
    pass

class Screen_3(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        return Builder.load_string(KV)

MyApp().run()

