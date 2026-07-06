from dataclasses import *
from tkinter import *
from prodraw.models.circle import Circle

from prodraw.config import SHAPE_COLORS

@dataclass
class circleView:
     canvas: Canvas

     def draw(self, circle: Circle):
          self.canvas.delete("circles")
          self.canvas.create_oval(circle.start_x-circle.raio, circle.start_y-circle.raio, circle.start_x+circle.raio, circle.start_y+circle.raio,
                                   fill=SHAPE_COLORS.get(circle.bg), outline=circle.bg, tags=("circles", "shape"))
          
     def draw_all(self, figures: dict):
        self.canvas.delete("circles")
        for circle in figures['Circle']:
            print(circle)
            x,y,r,bg = circle
            print(x,y,r)
            self.canvas.create_oval(x-r,y-r,x+r,y+r, fill=SHAPE_COLORS.get(bg), outline=bg, tags=("circle", "shape"))

     def delete(self):
        self.canvas.delete('circle')