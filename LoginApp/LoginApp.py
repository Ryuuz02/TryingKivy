# Import statements
import kivy
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

# Require most recent kivy version
kivy.require("2.0.0")


# Creates a subclass of gridlayout display called login
class login(GridLayout):
    # initialization function
    def __init__(self, **kwargs):
        # super __init__ to properly initialize itself
        super(login, self).__init__(**kwargs)
        # 2 columns
        self.cols = 2
        # Adds a widget prompting for user name
        self.add_widget(Label(text="User Name"))
        # Creates an input for the username
        self.username = TextInput(multiline=False)
        # Adds that username widget to the grid
        self.add_widget(self.username)
        # Does the exact same for password, prompting for password
        self.add_widget(Label(text="Password"))
        # Input for password
        self.password = TextInput(multiline=False)
        # Adds that input to the grid display
        self.add_widget(self.password)


# Subclass of the App class, for logins
class loginApp(App):
    # Ran when python code is ran
    def build(self):
        # Gives a title
        self.title = "Login"
        # Displays the grid layout information from above
        return login()


# Runs the login app
loginApp().run()
