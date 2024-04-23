from math import pi
from e_utils import Vec3

class PhysicsBody():
  def __init__(self, id: int, x: float, y: float, z: float, radius: float, mass: float = None, speed: Vec3 = None) -> None:
    self.id = id

    if mass:
      self.mass = mass
    else:
      self.mass = (4/3)*pi*(radius**3)  *10000

    self.radius = radius
    self.r = Vec3(x,y,z)
    if speed:
      self.v = speed
    else:
      self.v = Vec3(0,0,0)
    self.a = Vec3(0,0,0)

  def current_acceleration(self) -> Vec3:
    return self.a

  def current_speed(self) -> Vec3:
    return self.v

  def current_position(self) -> Vec3:
    return self.r

  def attraction_force_from(self, other: 'PhysicsBody') -> Vec3:
    G = 6.67430e-11
    r = other.r - self.r
    r_mag = (r.x**2 + r.y**2 + r.z**2)**0.5
    if r_mag == 0: # not sure if this make sense but kind of does??
      return Vec3(0,0,0)
    F = (G*self.mass*other.mass)/(r_mag**2)

    F_vec = (r*(1/r_mag))*F
    return F_vec

  def surface_distance_magnitude(self, other: 'PhysicsBody') -> float:
    return (self.r - other.r).magnitude() - self.radius - other.radius