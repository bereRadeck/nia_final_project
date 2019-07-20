import numpy as np
from collections import defaultdict
from GA.Initializer import Heuristic_Initializer, Random_Initializer
from GA.Selector import Roulette_Selector
from GA.Recombiner import Recombiner
from GA.Mutator import Route_Mutator
from GA.Replacer import Replacer
from Task_Initializer import Task
from Evaluator import Evaluator
from Genetic_Alrorithm import Genetic_Alrorithm
from ACO_SORTER import ACO_Sorter


from ACO.ACO_Initializer import ACO_Initializer
from ACO.ACO_SolutionGenerator import SolutionGenerator
from ACO.ACO_Evaporator import Evaporator
from ACO.ACO_Intensificator import Intensificator
from ACO.ACO_Main import ACO

aco_initializer = ACO_Initializer()
aco_solutiongenerator = SolutionGenerator()
aco_evaporator = Evaporator()
aco_intensificator = Intensificator()



initializer = Heuristic_Initializer()
#initializer = Random_Initializer()
selector = Roulette_Selector()
recombiner = Recombiner()
mutator = Route_Mutator()
replacer = Replacer()
task = Task()
evaluator = Evaluator()

aco_iterations = 5
aco_sorter = ACO_Sorter(aco_initializer,
                        aco_solutiongenerator,
                        aco_evaporator,
                        aco_intensificator,
                        task.distance_matrix,
                        aco_iterations)
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
                       iterations=iterations,
                       aco_sorter = aco_sorter,
                       aco_sort_step=1,
                       sort_with_aco=False,
                       refill_cars=True)

#ga.run()

results = defaultdict(list)
"""
pop_sizes = [20, 100, 100, 1000]  # ,10000]

offspring_percentages = [0.1, 0.2, 0.5]
for pop_size in pop_sizes:
    for off_p in offspring_percentages:
        offspring_size = off_p * pop_size
        ga = Genetic_Alrorithm(initializer=initializer,
                               selector=selector,
                               recombiner=recombiner,
                               mutator=mutator,
                               replacer=replacer,
                               evaluator=evaluator,
                               popSize=pop_size,
                               nrOffspring=offspring_size,
                               task=task,
                               mutate_prop=mutate_prop,
                               iterations=iterations,
                               aco_sorter=aco_sorter,
                               aco_sort_step=1,
                               sort_with_aco=False)

        solutions = ga.run(logging=False)
        min_score = np.min(list(solutions.values())[0])
        max_score = np.max(list(solutions.values())[0])
        mean_score = np.mean(list(solutions.values())[0])
        results['pop_size'].append(pop_size)
        results['offspring_size'].append(offspring_size)
        results['max'].append(max_score)
        results['min'].append(min_score)
        results['mean'].append(mean_score)"""
