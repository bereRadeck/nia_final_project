from Task_Initializer import Task
from copy import deepcopy
import numpy as np

task = Task()
dist = deepcopy(task.distance_matrix)

assert task.customer_matrix[3,46] == dist[3,46]
assert task.customer_matrix.shape == dist.shape


