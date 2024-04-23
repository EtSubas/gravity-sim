import tkinter as tk
from engine import Engine
from e_utils import Vec3

VIRTUAL_WIDTH = 1000
VIRTUAL_HEIGHT = 1000

class DisplayCanvas(tk.Canvas):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.dt = 1

    self.canvas_bodies = []
    self.eng = Engine()

  def run(self):
    self.tick()

  def tick(self):
    self.update()
    self.after(self.dt, self.tick)

  def update(self) -> None:
    self.eng.update_objects(1)

    for body in self.canvas_bodies:

      # collision_list = self.eng.get_collision_list(body)
      # if collision_list:
      #   new_id = self.eng.combine_objects(collision_list)
      #   for collided_id in sorted(collision_list, reverse=True):
      #     temp = self.canvas_bodies.index(collided_id)
      #     del self.canvas_bodies[self.canvas_bodies.index(collided_id)]

      #   radius = self.eng.get_body_radius(new_id)
      #   r = self.eng.get_body_position(new_id)
      #   body = self.create_oval(r.x-radius, r.y-radius, r.x+radius, r.y+radius, fill="black")
      #   self.eng.update_id(new_id, body)
      #   continue

      v = self.eng.get_body_speed(body)
      self.move(body, v.x, v.y)

  def add_body(self, x: float, y: float, radius: float, mass: float, color: str):
    body = self.create_oval(x-radius, y-radius, x+radius, y+radius, fill=color)
    self.eng.add_object(body, x, y, 0, mass, radius)
    self.canvas_bodies.append(body)

class ScreenManager():

  def __init__(self, x:int, y:int):
    """
    Initialize the ScreenManager class

    Args:
        x (int): The actual width of the window in font size
        y (int): The actual height of the window in font size
    """
    ScreenManager.width = x
    ScreenManager.height = y
    self.top = tk.Tk()
    self.top.geometry(f"{x}x{y}")
    # self.top.resizable(0,0)

    self.cvs = DisplayCanvas(self.top)
    self.cvs.pack(fill="both", expand=True)

    self._register_keybinds()

  def run(self):
    self.cvs.run()
    self.top.mainloop()

  @staticmethod
  def _convert_virtual_to_real(x: float, y: float):
    real_x = x/1000*ScreenManager.width
    real_y = y/1000*ScreenManager.height
    return real_x, real_y

  def add_body(self, x: float, y: float, radius: float, color: str, mass: float = None):
    x, y = self._convert_virtual_to_real(x, y)
    self.cvs.add_body(x, y, radius, mass, color)

  def _register_keybinds(self):
    # self.top.bind("<KeyPress-Left>", lambda _: self.cvs.change_heading(-self.ds, 0))
    # self.top.bind("<KeyPress-Right>", lambda _: self.cvs.change_heading(self.ds, 0))
    # self.top.bind("<KeyPress-Up>", lambda _: self.cvs.change_heading(0, -self.ds))
    # self.top.bind("<KeyPress-Down>", lambda _: self.cvs.change_heading(0, self.ds))
    pass
