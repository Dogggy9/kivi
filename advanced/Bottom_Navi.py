from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.toolbar.toolbar import MDBottomAppBar

KV = '''
BoxLayout:
    orientation: 'vertical'
    
    MDTopAppBar:
        title: "Пример Bottom Navigation"
        # pos_hint: {'top': 1}
        # elevation: 10
        
    MDBottomNavigation:
        panel_color: 255/255, 255/255, 204/255, 1
        # panel_color: 0,0,1,1
        
        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Python'
            icon: 'language-python'
            MDLabel:
                text: "Вкладка программирование на Python"
                halign: 'center'
        MDBottomNavigationItem:
            name: 'screen2'
            text: 'C++'
            icon: 'language-cpp'
            MDLabel:
                text: "Вкладка программирование на C++"
                halign: 'center'
        MDBottomNavigationItem:
            name: 'screen3'
            text: 'Java'
            icon: 'language-javascript'
            MDLabel:
                text: "Вкладка программирование на Java Script"
                halign: 'center'
'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MyApp().run()
