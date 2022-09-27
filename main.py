from kivy.app import App
from plyer import gps

class MainApp(App):
    def on_start(self):
        gps.configure(on_location=self.on_gps_location)
        gps.start()
    def on_gps_location(self, **kwargs):
        latitude, longitude, altitude = kwargs["lat"], kwargs["lon"], kwargs["altitude"]
        print(kwargs)

MainApp().run()