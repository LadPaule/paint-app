from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Ellipse, Color, Line
import random

#Accepting the RGBA color pattern
Window.clearcolor = (0, 0, 0, 1 )

class Paint_window(Widget):
    def on_touch_down(self, touch):

        color_red = random.randint(0, 255)
        color_green = random.randint(0, 255)
        color_blue = random.randint(0, 255)

        self.canvas.add(Color(rgb = (color_red/255.0, color_green/255.0, color_blue/255.0)))
        diameter = 10
        self.canvas.add(Ellipse(pos=(touch.x - diameter/2, touch.y - diameter/2), size=(diameter, diameter)))

        touch.ud['line'] = Line(points = (touch.x, touch.y), width = diameter)
        self.canvas.add(touch.ud['line'])

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

#      
class Paint_app(App):
    def build(self):

        root_window = Widget()
        self.paiter = Paint_window()

        clear_button = Button(text = 'new', font_size = 14, width = 40, height = 20)
        clear_button.bind(on_release = self.clear_canvas)

        root_window.add_widget(self.paiter)
        root_window.add_widget(clear_button)

        return root_window
    
    def clear_canvas(self, obj):
        self.paiter.canvas.clear()

Paint_app() .run()
