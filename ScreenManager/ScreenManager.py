# Import Statements
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
from kivy.lang import Builder

"""
!!!------------------------------------------------------------------------------------------------------------------!!!
!!!-------------------This is not my work, this is taken from the kivy ScreenManager Basic Usage Tutorial------------!!!
!!!------------------------------------------------------------------------------------------------------------------!!!
"""
Builder.load_string("""
<MainScreen>:
    BoxLayout:
        Button:
            text: "Go to new Screen"
            on_press: root.manager.current = "Selected"
        Button:
            text: "Quit"
<SelectedScreen>:
    BoxLayout:
        Button:
            text: "Go to Main Screen"
            on_press: root.manager.current = "Main"
        Button:
            text: "Quit"

""")


class MainScreen(Screen):
    pass


class SelectedScreen(Screen):
    pass


class ScreenApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="Main"))
        sm.add_widget(SelectedScreen(name="Selected"))
        return sm


screentesting = ScreenApp()
screentesting.run()
