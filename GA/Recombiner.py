import numpy as np
from copy import deepcopy
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
LOG = logging.getLogger(__name__)
LOG.propagate = False
class Recombiner:


    def recombine(self,parents):
        offspring = []
        for p in parents:
            child1, child2 = self._recombine_individual(p[0],p[1])
            offspring.append(child1)
            offspring.append(child2)

        return offspring



    def _recombine_individual(self,parent1,parent2):
        """
        chooses a car from each parent that is yet not used in the other one and put's it into each other solution,
        while deleting the corresponding customers from the other routes
        :param parent1:
        :param parent2:
        :return:
        """
        #"""
        # get all the cars that are listed in each solution
        parent1_cars = np.array(list(parent1['solution'].keys()))
        parent2_cars = np.array(list(parent2['solution'].keys()))

        # determine which cars from parent1 are also in parent2, and the other way around
        mask1 = np.isin(parent1_cars,parent2_cars)


        # determine which of the cars of parent1 are not in parent2 and the other way around
        cars_to_choose_fom_parent1 = parent1_cars[~ mask1]


        # if there is at least one car in parent1 that it not in parent2
        if len(cars_to_choose_fom_parent1) > 0:
            # choose one of these cars
            car1 = np.random.choice(cars_to_choose_fom_parent1)
            # get it's route
            route1 = parent1['solution'][car1]

            # delete the route customers from the old solution of parent2
            old_solution = deepcopy(parent2['solution'])
            #LOG.info('Customers from Route1: {}'.format(str(route1)))
            new_solution2 = self._delete_customers(old_solution,route1)
            # append the new route
            new_solution2[car1] = route1
            parent2['solution'] = new_solution2

        parent2_cars = np.array(list(parent2['solution'].keys()))
        mask2 = np.isin(parent2_cars, parent1_cars)
        cars_to_choose_fom_parent2 = parent2_cars[~ mask2]
        if len(cars_to_choose_fom_parent2) > 0:
            car2 = np.random.choice(cars_to_choose_fom_parent2)
            route2 = parent2['solution'][car2]
            old_solution = deepcopy(parent1['solution'])
            #LOG.info('Customers from Route2: {}'.format(str(route2)))
            new_solution1 = self._delete_customers(old_solution,route2)
            new_solution1[car2] = route2
            parent1['solution'] = new_solution1


        return parent1, parent2

    def fill_big_capacities(self, child, task, aco_sorter):
        demands = {}
        free_spaces = {}

        for car, route in child['solution'].items():
            capacity = task.capacities[car]
            demand = 0
            for customer in route:
                demand += task.demands[customer-1]
            free_spaces[car] = capacity-demand
            demands[car] = capacity

        free_space_cars = []
        free_space_list = []
        for car, free_space in sorted(free_spaces.items(), key=lambda item: item[1]):
            free_space_cars.append(car)
            free_space_list.append(free_space)

        demand_cars = []
        demands_list = []
        for car, demand in sorted(demands.items(), key=lambda item: item[1]):
            demand_cars.append(car)
            demands_list.append(demand)

        if free_space_list[-1] >= demands_list[0]:
            a = list(child['solution'][free_space_cars[-1]])
            b = list(child['solution'][demand_cars[0]])
            route = a+b
            new_route = aco_sorter.sort_singe_route(route)
            child['solution'][free_space_cars[-1]] = new_route

            child['solution'].pop(demand_cars[0])

        return child

    def fill_free_capacities_in_offspring(self, offspring, task, aco_sorter):
        new_offspring = []
        for child in offspring:
            child = self.fill_big_capacities(child, task, aco_sorter)
            new_offspring.append(child)
        return new_offspring












        pass


    def _delete_customers(self,solution,customers):
        """
        d
        :param solution:
        :param customers:
        :return:
        """
        old_customers = [c for route in solution.values() for c in route]
        o = len(old_customers)
        count = len(customers)

        new_solution = dict()

        for car,route in solution.items():
            for customer in customers:
                #assert isinstance(customer, int)
                if np.isin(customer,route):
                    i = np.argwhere(route==customer)
                    route = np.delete(route,i)

                    i = np.argwhere(customers == customer)
                    customers = np.delete(customers, i)
            if len(route) > 0:
                new_solution[car]=route

        new_customers = [c for route in new_solution.values() for c in route]

        n = len(new_customers)

        assert len(np.unique(old_customers)) - len(np.unique(new_customers)) == count

        return new_solution