from screen import ScreenManager


if __name__ == "__main__":

  sc_manager = ScreenManager(600, 600)
  sc_manager.add_body(100, 100, 20, color="red")
  sc_manager.add_body(500, 500, 20, mass=30000000000, color="green")
  sc_manager.add_body(800, 700, 5, mass=100000000000, color="orange")
  sc_manager.add_body(200, 700, 60, color="yellow")
  # sc_manager.add_body(1000, 1000, 30, mass=-5000000000, color="blue")
  sc_manager.add_body(550, 900, 30, mass=800000000, color="purple")
  sc_manager.add_body(990, 777, 30, mass=8888888888, color="pink")


  sc_manager.run()





# TODO
# 1 - need to add collision
#     - currently the collision causes one of the bodies to turn black and then both stop moving
#       seems like its almost working but not quite...
# 1 - mass of 0 does not work right now
# 2 - should calculate speed based on momentum
# 1 - add initial velocity
# 1 - need to add body combination
# 1 - need to add keybinds for zoom feature (maybe mouse scroll wheel)
# 3 - should break screen manager and other screen class into different files
# 2 - want to add static bodies
# 4 - might to add body splitting
# 4 - need to add z axis
# 3 - need to add doc strings and typing
# 3 - should add keybinds to control time
# 3 - it would be cool if there was interactive adding objects, llike click and hold for the size than then flick release to start with an initioal speed