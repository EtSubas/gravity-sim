from dataclasses import dataclass
from numbers import Number

@dataclass
class Vec3():
  def __add__(self,other):
    return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
  def __sub__(self,other):
    return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

  def __mul__(self,other):
    if isinstance(other, (float, int)):
      return Vec3(self.x * other, self.y * other, self.z * other)
    else:
      raise TypeError(f"unsupported operand type(s) for *: 'Vec3' and '{type(other)}'")

  def __div__(self,other):
    if isinstance(other, (float, int)):
      return Vec3(self.x / other, self.y / other, self.z / other)
    else:
      raise TypeError(f"unsupported operand type(s) for /: 'Vec3' and '{type(other)}'")

  def magnitude(self):
    return (self.x**2 + self.y**2 + self.z**2)**0.5

  x: float = 0
  y: float = 0
  z: float = 0