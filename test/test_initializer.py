from GA.Initializer import Heuristic_Initializer
from Task_Initializer import Task
from copy import deepcopy
import numpy as np

task = Task()


init = Heuristic_Initializer()

pop = init.initialize_pop(task)

ind = pop[-1]

customers = 0
for route in ind['solution'].values():
    customers+=len(route)

assert customers == len(task.demands)