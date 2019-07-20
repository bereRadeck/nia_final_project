
import numpy as np
from copy import deepcopy
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
LOG = logging.getLogger(__name__)


class Evaluator:

    def evaluate(self, pop, task):
        """
        evaluates each individual of a population and return the population with updated fitness scores
        :param pop:
        :param task:
        :return:
        """
        this_task = deepcopy(task)
        this_pop = deepcopy(pop)
        values = []
        for individual in this_pop:
            fitness = self._evaluate_individual(individual,this_task)
            individual['fitness'] = fitness
            values.append(fitness)

        # LOG.info('Fitness: Mean= {} \t Min={} \t Max={}'.format(np.mean(values),
        # np.min(values),np.max(values)))
        return this_pop

    @staticmethod
    def _evaluate_individual(individual, task):
        """
        evaluates and individual solution by determining the rout distance of each car, multiplying
        it with the cars transportation costs and summing it up
        :param individual: a single solution to the vrp
        :param task: the vrp
        :return: a fitness score (the smaller the better)
        """
        fitness = 0
        for car, route in individual['solution'].items():
            i = np.append(0, route)
            j = np.append(route, 0)

            dist_sum = np.sum(task.distance_matrix[i, j])
            cost = dist_sum*task.transportation_costs[car]
            fitness += cost

        return fitness
