import numpy as np
from GA.Initializer import Heuristic_Initializer
from GA.Selector import Roulette_Selector
from Task_Initializer import Task
from Evaluator import Evaluator
from copy import deepcopy

task = Task()
init = Heuristic_Initializer()
pop = init.initialize_pop(task,100)

evaluator = Evaluator()
pop = evaluator.evaluate(pop,task)

selector = Roulette_Selector()
parents = selector.select(pop,50)

fitnesses_parents = []
for pa in parents:
    for p in pa:
        fitnesses_parents.append(p['fitness'])

fitnesses_pop = [p['fitness'] for p in pop]
print(np.mean(fitnesses_parents),np.mean(fitnesses_pop))
assert np.mean(fitnesses_parents) < np.mean(fitnesses_pop)
assert len(parents) == 25



