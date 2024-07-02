def eat_ghost(has_power_pellet, touches_ghost):
  return has_power_pellet and touches_ghost
    
def score(has_power_pellet, touches_dot):
  return has_power_pellet or touches_dot
  
def lose(has_power_pellet, touches_ghost):
  return touches_ghost and not has_power_pellet
  
def win(ate_all_dots, has_power_pellet, touches_ghost):
  return ate_all_dots and not lose(has_power_pellet, touches_ghost)

print(win(True, True, False))