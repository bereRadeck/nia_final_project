import numpy as np

class Roulette_Selector:

    def select(self, pop, offspring_size):
        """
        selects parents based on fitness
        :param pop: population
        :param offspring_size: size of offspring
        :return: parents for recombiner
        """
        parents = []
        if offspring_size%2 == 0:
            parents_number = int(offspring_size/2)
        else:
            parents_number = int((offspring_size-1)/2)

        for i in range(parents_number):
            fitness = np.array([individual['fitness'] for individual in pop])
            fitness = 1/ fitness
            probs = fitness/fitness.sum()
            p1,p2 = np.random.choice(pop,size=2,replace=False,p=probs)
            parents.append((p1,p2))

        return parents
