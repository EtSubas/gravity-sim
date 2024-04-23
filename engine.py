
from typing import Dict, List
from copy import deepcopy
from e_utils import Vec3
from physicsBody import PhysicsBody


class Engine():

  def __init__(self) -> None:
    self.bodies: Dict[int, PhysicsBody] = {}
    self.current_collision_dict: Dict[int, List[int]] = {}
    pass

  def add_object(self, id:int, x: float, y: float, z: float, mass: float, radius: float):
    self.bodies[id] = PhysicsBody(id, x, y, z, radius, mass)

  def update_objects(self, dt: float = 1):
    updated_objects: Dict[int, PhysicsBody] = {}
    for id, body1 in self.bodies.items():
      total_force = Vec3()
      for body2 in self.bodies.values():
        if body1.id == body2.id:
          continue
        total_force += body1.attraction_force_from(body2)

      updated_body = deepcopy(body1)

      updated_body.a = total_force*(1/body1.mass)
      updated_body.v += body1.a*dt
      updated_body.r += body1.v*dt
      updated_objects[id] = updated_body

    self.bodies = updated_objects
    self._check_collisions()


  def get_body_speed(self, id:int) -> Vec3:
    return self.bodies[id].current_speed()

  def get_body_position(self, id:int) -> Vec3:
    return self.bodies[id].current_position()

  def get_body_radius(self, id:int) -> float:
    return self.bodies[id].radius

  def get_collision_list(self, id:int) -> List[int]:
    if id not in self.current_collision_dict:
      return []
    return self.current_collision_dict[id]

  def _check_collisions(self) -> bool:
    for i, body1 in self.bodies.items():
      for j, body2 in self.bodies.items():
        if i == j:
          continue

        if 0 >= body1.surface_distance_magnitude(body2):
          if i not in self.current_collision_dict:
            self.current_collision_dict[i] = [i, j]
          else:
            self.current_collision_dict[i].append(j)

  def combine_objects(self, id_list: List[int]) -> int:
    """
    Returns the new id

    Args:
        id_list (List[int]): _description_

    Returns:
        int: _description_
    """
    new_mass = 0
    new_radius = 0
    new_position = Vec3()
    new_speed = Vec3()
    new_id = min(id_list)
    for i in id_list:
      new_mass += self.bodies[i].mass
      # Higher mass bodies, impact the new radius, position and speed more
      new_radius += self.bodies[i].radius*self.bodies[i].mass
      new_position += self.bodies[i].r*self.bodies[i].mass
      new_speed += self.bodies[i].v*self.bodies[i].mass
      self.bodies.pop(i)

    new_radius = new_radius/new_mass
    new_position = new_position*(1/new_mass)
    new_speed = new_speed*(1/new_mass)

    self.bodies[new_id] = PhysicsBody(new_id,
                                      new_position.x,
                                      new_position.y,
                                      new_position.z,
                                      new_radius,
                                      new_mass,
                                      speed=new_speed)

    return new_id

  def update_id(self, current_id:int, new_id:int):
    self.bodies[new_id] = self.bodies.pop(current_id)

  def remove_object(self, id:int):
    self.bodies.pop(id)
