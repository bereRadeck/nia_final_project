from GA.Initializer import Heuristic_Initializer, Random_Initializer
from Task_Initializer import Task
from copy import deepcopy
import numpy as np

task = Task()


init = Heuristic_Initializer()

pop = init.initialize_pop(task)

i = np.random.choice(range(len(pop)))
ind = pop[i]

customer_count = 0
customers = []
for route in ind['solution'].values():
    customer_count+=len(route)
    customers.append(route)

customers_flattend = [c for sublist in customers for c in sublist]
assert customer_count == len(task.demands)
assert len(np.unique(customers_flattend)) == len(task.demands)

init = Random_Initializer()
pop = init.initialize_pop(task)

i = np.random.choice(range(len(pop)))
ind = pop[i]

customer_count = 0
customers = []
for route in ind['solution'].values():
    customer_count+=len(route)
    customers.append(route)

customers_flattend = [c for sublist in customers for c in sublist]

assert len(np.unique(customers_flattend)) == len(task.demands)
assert customer_count == len(task.demands)