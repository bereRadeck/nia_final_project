import numpy as np
from GA.Initializer import Heuristic_Initializer
from Task_Initializer import Task
from Evaluator import Evaluator
from copy import deepcopy


task = Task()


init = Heuristic_Initializer()

pop = init.initialize_pop(task)

evaluator = Evaluator()
pop = evaluator.evaluate(pop,task)

for p in pop:
    print(p['fitness'])