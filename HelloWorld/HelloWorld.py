# Import Statements
import kivy
from kivy.app import App
from kivy.uix.label import Label

# Requires an up to date version of kivy
kivy.require("2.0.0")


# My application, subclass of App
class myApp(App):
    # Build is ran when the python code
    def build(self):
        # Gives a title to the window application
        self.title = "Hello World"
        # Label is just a display, in this case, the words hello world
        return Label(text="Hello World")


# Runs the application
myApp().run()
