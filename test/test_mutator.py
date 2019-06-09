import numpy as np
from GA.Initializer import Heuristic_Initializer
from GA.Selector import Roulette_Selector
from GA.Recombiner import Recombiner
from GA.Mutator import Route_Mutator
from Task_Initializer import Task
from Evaluator import Evaluator
from copy import deepcopy

task = Task()
init = Heuristic_Initializer()
pop = init.initialize_pop(task,10)

evaluator = Evaluator()
pop = evaluator.evaluate(pop,task)

ind = np.random.choice(pop)
customers_before = [customer for route in ind['solution'].values() for customer in route]
assert len(customers_before) == len(np.unique(customers_before))

mutator = Route_Mutator()
pop = mutator.mutate(pop,0.8)

ind = np.random.choice(pop)

customers_num = 0
for route in ind['solution'].values():
    customers_num+=len(route)

customers = [customer for route in ind['solution'].values() for customer in route]



print(len(customers),len(np.unique(customers)))
assert len(customers) == len(np.unique(customers))

print(customers_num,len(task.demands))
assert customers_num == len(task.demands)