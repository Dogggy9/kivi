from kivy.app import App
from kivy.uix.slider import Slider

class MainApp(App):
    def build(self):
        slide = Slider(orientation='horizontal',
                       value_track=True,
                       value_track_color=(0,0,1,1),
                       value=50,
                       max=500,
                       step=25)
        return slide

MainApp().run()