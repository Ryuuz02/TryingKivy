# Import Statements
from random import random
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line

# !------- This is the from the tutorial on the kivy website with slight modification, this is not my own work --------!

# Ensure correct kivy version
kivy.require("2.0.0")


# Create our widget class
class paintWidget(Widget):
    def __init__(self):
        super().__init__()
        # Some variables we use for user to have say in what they draw
        self.drawtype = ""
        self.color = (1, 1, 1)

    def on_touch_down(self, touch):
        # When the mouse button is pressed
        with self.canvas:
            # With the canvas open, passes down the color
            Color(*self.color)
            # If the drawing type is currently circle, will draw a circle
            if self.drawtype == "circle":
                d = 30
                Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            # If it drawing lines, it will create a miniscule line
            if self.drawtype == "line":
                touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        # If current drawing style is line, will continue the line, else will do nothing
        if self.drawtype == "line":
            touch.ud["line"].points += [touch.x, touch.y]


class paintApp(App):
    def build(self):
        # Large widget for the entire application
        parent = Widget()
        # Adds the painter widget
        self.painter = paintWidget()
        parent.add_widget(self.painter)
        # Adds a button to clear the canvas
        clear_button = Button(text="Clear")
        clear_button.bind(on_release=self.clear_canvas)
        parent.add_widget(clear_button)
        # Adds a button to draw lines instead
        line_button = Button(text="Draw Lines", pos=[100, 0])
        line_button.bind(on_press=self.line_draw)
        parent.add_widget(line_button)
        # Adds a button to draw circles instead
        circle_button = Button(text="Draw Circles", pos=[200, 0])
        circle_button.bind(on_press=self.circle_draw)
        parent.add_widget(circle_button)
        # Adds a button to draw in red
        red_button = Button(text="Red", color=(1, 0, 0), pos=[0, 100], size=[50, 50])
        red_button.bind(on_press=self.red_draw)
        parent.add_widget(red_button)
        # Adds a button to draw in green
        red_button = Button(text="Green", color=(0, 1, 0), pos=[0, 150], size=[50, 50])
        red_button.bind(on_press=self.green_draw)
        parent.add_widget(red_button)
        # Adds a button to draw in blue
        red_button = Button(text="Blue", color=(0, 0, 1), pos=[0, 200], size=[50, 50])
        red_button.bind(on_press=self.blue_draw)
        parent.add_widget(red_button)
        # Adds a button to draw in a random color
        red_button = Button(text="Random", color=(random(), random(), random()), pos=[0, 250], size=[50, 50])
        red_button.bind(on_press=self.random_draw)
        parent.add_widget(red_button)
        # Returns the widget
        return parent

    # Below are various functions for the buttons to use

    # This one clears the canvas
    def clear_canvas(self, obj):
        self.painter.canvas.clear()

    # This one switches to drawing lines
    def line_draw(self, obj):
        self.painter.drawtype = "line"

    # Switches the drawing circles
    def circle_draw(self, obj):
        self.painter.drawtype = "circle"

    # Switches to drawing red
    def red_draw(self, obj):
        self.painter.color = (1, 0, 0)

    # Switches to drawing green
    def green_draw(self, obj):
        self.painter.color = (0, 1, 0)

    # Switches to drawing blue
    def blue_draw(self, obj):
        self.painter.color = (0, 0, 1)

    # Switches to drawing a random color
    def random_draw(self, obj):
        self.painter.color = (random(), random(), random())


# Runs the application
paintApp().run()
