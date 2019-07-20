import numpy as np

class Route_Mutator:

    def mutate(self, pop, prop=0.1):

        for p in pop:
            p['solution'] = self._mutate_individual(p, prop)

        return pop

    @staticmethod
    def _mutate_individual(individual, prop):
        new_solution = dict()
        # go though each car-customer assignment of a solution
        for car, route in individual['solution'].items():
            # swap two random chooses customers of a route with mutate probability
            if np.random.uniform(0, 1) < prop:
                if len(route) >= 2:
                    i = np.random.choice(range(len(route)-1), replace=False)
                    tmp = route[i]
                    route[i] = route[i+1]
                    route[i+1] = tmp

            new_solution[car]=route

        return new_solution


