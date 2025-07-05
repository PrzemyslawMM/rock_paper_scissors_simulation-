from Simulation_Chamber import Simulation_Chamber
import matplotlib.pyplot as plt

simulation = Simulation_Chamber()

k = 1000
for i in range(k):
  simulation.simulation_day()

x = [i for i in range(0, k+1)]
plt.plot(x, simulation.rock, c="grey", linewidth=1, label="ROCK")
plt.plot(x, simulation.paper, c="blue", linewidth=1, label="PAPER")
plt.plot(x, simulation.scissors, c="black", linewidth=1, label="SCISSORS")
plt.legend(bbox_to_anchor=(1,1))
plt.show()

# simulation = Simulation_Chamber()

# k = 100
# for i in range(k):
#   simulation.simulation_day()

# print(simulation.rock) 
# print(simulation.paper) 
# print(simulation.scissors)