from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.carousel import MDCarousel
from kivymd.uix.pickers import MDDatePicker

class MainApp(MDApp):
    def build(self):
        # создать объект
        carousel = MDCarousel(direction='right')
        img = Image(source='./Images/aircrack-ng.png')
        carousel.add_widget(img)
        img = Image(source='./Images/wifiphisher.png')
        carousel.add_widget(img)
        img = Image(source='./Images/kot_glaza_goluboj.jpg')
        carousel.add_widget(img)
        dat = MDDatePicker()
        carousel.add_widget(dat)

        return carousel

MainApp().run()
