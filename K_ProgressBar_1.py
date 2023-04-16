from kivy.app import App
from kivy.uix.progressbar import ProgressBar

class MainApp(App):
    def build(self):
        progress = ProgressBar(max=1000, value=650)
        # progress.max = 1000
        # progress.value = 650
        return progress

MainApp().run()