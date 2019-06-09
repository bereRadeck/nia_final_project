import numpy as np
from GA.Initializer import Heuristic_Initializer
from GA.Selector import Roulette_Selector
from GA.Recombiner import Recombiner
from GA.Mutator import Route_Mutator
from GA.Replacer import Replacer
from Task_Initializer import Task
from Evaluator import Evaluator
from Genetic_Alrorithm import Genetic_Alrorithm

initializer = Heuristic_Initializer()
selector = Roulette_Selector()
recombiner = Recombiner()
mutator = Route_Mutator()
replacer = Replacer()
task = Task()
evaluator = Evaluator()

pop_size = 10
offspring_size = 5
mutate_prop = 0.2
iterations = 20

ga = Genetic_Alrorithm(initializer=initializer,
                       selector=selector,
                       recombiner=recombiner,
                       mutator=mutator,
                       replacer=replacer,
                       evaluator=evaluator,
                       popSize=pop_size,
                       nrOffspring = offspring_size,
                       task=task,
                       mutate_prop=mutate_prop,
                       iterations=iterations)

ga.run()




