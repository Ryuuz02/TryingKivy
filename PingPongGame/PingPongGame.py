# Import Statements
import kivy
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector

# !------- This is the from the tutorial on the kivy website with slight modification, this is not my own work --------!

# Only works if kivy is up to date
kivy.require("2.0.0")


class PingPongGame(Widget):
    # Creates the different objects we use
    game_ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    # Serves the ball at the beginning and whenever a point is earned
    def serve_ball(self, vel=(4, 0)):
        self.game_ball.center = self.center
        self.game_ball.velocity = vel

    # Updates the game display
    def update(self, dt):
        # Moves the ball, and checks if it hit a paddle
        self.game_ball.move()
        self.player1.bounce_ball(self.game_ball)
        self.player2.bounce_ball(self.game_ball)

        # Checks if the ball is too high or too low
        if (self.game_ball.y < 0) or (self.game_ball.top > self.height):
            self.game_ball.velocity_y *= -1

        # Checks if the ball is in player1's goal
        if self.game_ball.x < 0:
            # Gives a point and re-serves ball
            self.player2.score += 1
            self.serve_ball(vel=(4, 0))
        # Checks if the ball is in player2's goal
        if self.game_ball.x > self.width:
            # Gives a point and re-serves ball
            self.player1.score += 1
            self.serve_ball(vel=(-4, 0))

    # When the player moves their mouse
    def on_touch_move(self, touch):
        # Depending on which side of the app they are on, moves that appropriate paddle
        if touch.x <= self.center_x:
            self.player1.center_y = touch.y
        if touch.x > self.center_x:
            self.player2.center_y = touch.y


# Paddle for the players to use
class PingPongPaddle(Widget):
    # Score to display
    score = NumericProperty(0)

    # Function for when the ball collides with the paddle, checked every game_update
    def bounce_ball(self, game_ball):
        # If it collides
        if self.collide_widget(game_ball):
            # Takes the velocity
            velocity_x, velocity_y = game_ball.velocity
            # Creates a speedup scalar
            speedup = 1.1
            # Creates an offset based on where it was hit
            offset = (game_ball.center_y - self.center_y) / (self.height / 2)
            # Creates the directional velocity
            bounce_velocity = Vector(-1 * velocity_x, velocity_y)
            # Speeds it up
            new_velocity = bounce_velocity * speedup
            # Sets the game ball's velocity
            game_ball.velocity = new_velocity.x, new_velocity.y + offset


# Main app for the game
class PingPongApp(App):
    def build(self):
        # Creates the widget
        game = PingPongGame()
        # Serves the ball
        game.serve_ball()
        # Starts a timer to update the game
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


# Widget for the ping pong ball
class PingPongBall(Widget):
    # Velocity on x and y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # Allows us to access both velocity_x and velocity_y in one variable, like self.pos, or self.size
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # Moves the position of the ball by its velocity vector
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


# Runs the app
PingPongApp().run()
