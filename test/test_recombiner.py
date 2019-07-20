import numpy as np
from GA.Initializer import Heuristic_Initializer
from GA.Selector import Roulette_Selector
from GA.Recombiner import Recombiner
from Task_Initializer import Task
from Evaluator import Evaluator
from copy import deepcopy

task = Task()
init = Heuristic_Initializer()
pop = init.initialize_pop(task, 100)

evaluator = Evaluator()
pop = evaluator.evaluate(pop, task)

selector = Roulette_Selector()
parents = selector.select(pop, 5)

recombiner = Recombiner()

offspring = recombiner.recombine(parents)
ind = np.random.choice(offspring)

customers_num = 0
for route in ind['solution'].values():
    customers_num += len(route)

customers = [customer for route in ind['solution'].values() for customer in route]

assert len(customers) == len(np.unique(customers))

print(customers_num, len(task.demands))
assert customers_num == len(task.demands)

task = {'capacities': [20, 40, 100], 'demands': [10, 10, 10, 10, 10, 10, 10, 10]}

child = {'solution': {}}

child['solution'][2] = [0, 1, 2]
child['solution'][1] = [3, 4, 5]
child['solution'][0] = [6, 7]

child = recombiner.fill_big_capacities(child, task)
print()
