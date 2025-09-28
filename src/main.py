from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class DemoApp(MDApp):
    def build(self):
        return MDLabel(
            text="Hello, KivyMD + Poetry + Git!",
            halign="center"
        )

if __name__ == "__main__":
    DemoApp().run()
