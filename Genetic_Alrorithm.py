import logging
import sys
import numpy as np
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
LOG = logging.getLogger(__name__)

class Genetic_Alrorithm:

    def __init__(self, initializer, selector, recombiner, mutator, replacer, evaluator,
                  popSize, nrOffspring,task, mutate_prop, iterations,aco_sorter,aco_sort_step,sort_with_aco=False):
        if nrOffspring > popSize:
            LOG.info('Warning: Size of Offspring should be smaller than size of pop')
        self.initializer = initializer
        self.selector = selector
        self.recombiner = recombiner
        self.mutator = mutator
        self.replacer = replacer
        self.evaluator = evaluator
        self.mutate_prop = mutate_prop
        self.task = task
        self.iterations = iterations
        self.popSize = popSize
        self.nrOffspring = nrOffspring
        self.aco_sorter = aco_sorter
        self.aco_sort_step = aco_sort_step
        self.sort_with_aco = sort_with_aco



    def run(self,logging=True):
        solutions = dict()



        LOG.info('Intitialize population with size {}'.format(self.popSize))
        self.pop = self.initializer.initialize_pop(self.task, self.popSize)
        LOG.info('Evaluate Population')

        self.pop = self.evaluator.evaluate(self.pop,self.task)
        fitness = [p['fitness'] for p in self.pop]
        LOG.info('Initial Fitness:\t\t\t Mean= {}\tMin={}\tMax={}'.format(round(np.mean(fitness),2),
                                                                          np.min(fitness),
                                                                        np.max(fitness)))

        if self.sort_with_aco == True:
            self.pop = self.aco_sorter.sort_routes(self.pop)
            self.pop = self.evaluator.evaluate(self.pop,self.task)
            fitness = [p['fitness'] for p in self.pop]
            LOG.info('Initial Fitness after ACO Sorting:\t Mean= {}\tMin={}\tMax={}'.format(round(np.mean(fitness), 2),
                                                                              np.min(fitness),
                                                                              np.max(fitness)))

        LOG.info('Start genetic algorithm with {} iterations'.format(self.iterations))
        solutions[0] = fitness
        for i in range(self.iterations):

            LOG.info('\n\nIteration {}'.format(i))

            # select parents based on their  fitness
            parents = self.selector.select(pop=self.pop,offspring_size=self.nrOffspring)

            # create offspring from parents
            offspring = self.recombiner.recombine(parents)

            # mutate the offspring
            offspring = self.mutator.mutate(offspring,self.mutate_prop)

            if (self.sort_with_aco == True) & (i%self.aco_sort_step == 0):
                offspring = self.aco_sorter.sort_routes(offspring)


            # evaluate the fitness of the offspring
            offspring = self.evaluator.evaluate(offspring,self.task)

            fitness_off = [p['fitness'] for p in offspring]
            LOG.info('Offspring Fitness:\t\t Mean= {}\tMin={}\tMax={}'.format(round(np.mean(fitness_off),2),
                                                                        np.min(fitness_off),
                                                                          np.max(fitness_off)))

            # replace old weak individuals of pop with offspring
            self.pop = self.replacer.replace(self.pop,offspring)

            new_fitness = [p['fitness'] for p in self.pop]
            LOG.info('New Fitness:\t\t\t\t Mean= {}\tMin={}\tMax={}'.format(round(np.mean(new_fitness),2),np.min(new_fitness),np.max(new_fitness)))


            solutions[i+1] = new_fitness

        return solutions






