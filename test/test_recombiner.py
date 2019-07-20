import numpy as np
from GA.Initializer import Heuristic_Initializer
from GA.Selector import Roulette_Selector
from GA.Recombiner import Recombiner
from Task_Initializer import Task
from Evaluator import Evaluator
from copy import deepcopy

task = Task()
init = Heuristic_Initializer()
pop = init.initialize_pop(task,100)

evaluator = Evaluator()
pop = evaluator.evaluate(pop,task)

selector = Roulette_Selector()
parents = selector.select(pop,5)

recombiner = Recombiner()

offspring = recombiner.recombine(parents)
ind = np.random.choice(offspring)

customers_num = 0
for route in ind['solution'].values():
    customers_num+=len(route)

customers = [customer for route in ind['solution'].values() for customer in route]

assert len(customers) == len(np.unique(customers))

print(customers_num,len(task.demands))
assert customers_num == len(task.demands)


