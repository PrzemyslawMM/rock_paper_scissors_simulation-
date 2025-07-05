import random

class Simulation_Chamber:
  rock = [100]
  paper = [100]
  scissors = [100]
  
  def draw(self):
    return 0
  
  def fight_choose(self, sim_rock, sim_paper, sim_scissors):
    fight = []
    if sim_rock > 0 and sim_paper > 0 and sim_scissors > 0:
      allowed = [0,1,2]
      fight = [random.choice(allowed), random.choice(allowed)]
      
    if sim_rock == 0 and sim_paper > 0 and sim_scissors > 0:
      allowed = [1,2]
      fight = [random.choice(allowed), random.choice(allowed)]
      
    if sim_rock > 0 and sim_paper == 0 and sim_scissors > 0:
      allowed = [0,2]
      fight = [random.choice(allowed), random.choice(allowed)]
      
    if sim_rock > 0 and sim_paper > 0 and sim_scissors == 0:
      allowed = [0,1]
      fight = [random.choice(allowed), random.choice(allowed)]

    if sim_rock > 0 and sim_paper == 0 and sim_scissors == 0:
      fight = [0, 0]
      
    if sim_rock == 0 and sim_paper > 0 and sim_scissors == 0:
      fight = [1, 1]
      
    if sim_rock == 0 and sim_paper == 0 and sim_scissors > 0:
      fight = [3, 3]
    return fight

  def simulation_day(self):
    sim_rock = self.rock[-1] #0
    sim_paper = self.paper[-1] #1
    sim_scissors = self.scissors[-1] #2

    end_rock = sim_rock
    end_paper = sim_paper
    end_scissors = sim_scissors

    for i in range(sim_rock+sim_paper+sim_scissors):
      if sim_rock+sim_paper+sim_scissors == 0:
        break
      fight = self.fight_choose(sim_rock, sim_paper, sim_scissors)

      match fight[0]:
        case 0:
          match fight[1]:
            case 0:
              if sim_rock == 1:
                # end_rock += 1
                sim_rock -= 1
              else:
                end_rock += self.draw()
                sim_rock -= 2
            case 1:
              end_rock -= 1
              end_paper += 1
              sim_rock -= 1
              sim_paper -= 1
            case 2:
              end_rock += 1
              end_scissors -= 1
              sim_rock -= 1
              sim_scissors -= 1
        case 1:
          match fight[1]:
            case 0:
              end_rock -= 1
              end_paper += 1
              sim_rock -= 1
              sim_paper -= 1
            case 1:
              if sim_paper == 1:
                # end_paper += 1
                sim_paper -= 1
              else:
                end_paper += self.draw()
                sim_paper -= 2
            case 2:
              end_scissors += 1
              end_paper -= 1
              sim_scissors -= 1
              sim_paper -= 1
        case 2:
          match fight[1]:
            case 0:
              end_scissors -= 1
              end_rock += 1
              sim_scissors -= 1
              sim_rock -= 1
            case 1:
              end_scissors += 1
              end_paper -= 1
              sim_scissors -= 1
              sim_paper -= 1
            case 2:
              if sim_scissors == 1:
                # end_scissors += 1
                sim_scissors -= 1
              else:
                end_scissors += self.draw()
                sim_scissors -= 2
    
    self.rock.append(end_rock)
    self.paper.append(end_paper)
    self.scissors.append(end_scissors)