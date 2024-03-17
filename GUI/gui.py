import kivy
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.graphics import Rectangle
from kivy.graphics import Line
from kivy.graphics import Color

class Menu_bar(BoxLayout):
    pass

class Enterance_part(GridLayout):
    
    slot_count : int = 4

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.rows = 2
        for i in range(self.slot_count):
            l = Label(text="Slot "+str(i+1))
            l.font_size = dp(35)
            l.font_name = "fonts/Lcd.ttf"
            l.color = (0,0,0,1)
            self.add_widget(l)
            # Bind the Rectangle instruction to update when position or size changes
            l.bind(pos=self.update_rect, size=self.update_rect)
            # Draw a rectangle around each label
            self.update_rect(l, l.pos)  # Call update_rect initially

    def update_rect(self, label, pos):
        # Clear previous instructions
        label.canvas.before.clear()
        # Draw a rectangle around the label
        with label.canvas.before:
            Color(0,1,0.5,1)
            Rectangle(pos=(label.x,label.y),size=(label.width,label.height))
            Color(0,0,1,1)
            Line(rectangle=(label.x,label.y,label.width,label.height),width=dp(3))

class MainFrame(BoxLayout):
    pass

class gui(App):
    pass

if __name__ == "__main__":
    gui().run()
