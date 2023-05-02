from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.factory import Factory

Builder.load_string('''
<ExampleBanner@Screen>
    MDBanner:
        id: banner
        text: ["Это однострочный баннер"]
        over_widget: screen
        vertical_pad: toolbar.height
        
    MDTopAppBar:
        id: toolbar
        title: "компонент Banner"
        elevation: 10
        pos_hint: {'top': 1}
        
    BoxLayout:
        id: screen
        orientation: 'vertical'
        size_hint_y: None
        height: Window.height-toolbar.height
        
        OneLineListItem:
            text: "Отобразить баннер"
            on_release: banner.show()
            
        Widget:
''')

class MyApp(MDApp):
    def build(self):
        return Factory.ExampleBanner()

MyApp().run()