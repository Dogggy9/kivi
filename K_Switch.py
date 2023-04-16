from kivy.app import App
from kivy.uix.video import Video

class MainApp(App):
    def build(self):
        switch = Video(source='qq.mp4', play=True)
        return switch

MainApp().run()