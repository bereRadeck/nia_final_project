import numpy as np
from copy import deepcopy

class Recombiner:


    def recombine(self,parents):
        offspring = []
        for p in parents:
            child1, child2 = self._recombine_individual(p[0],p[1])
            offspring.append(child1)
            offspring.append(child2)

        return offspring



    def _recombine_individual(self,parent1,parent2):
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
            new_solution2 = self._delete_customers(parent2['solution'],route1)
            # append the new route
            new_solution2[car1] = route1
            parent2['solution'] = new_solution2

        parent2_cars = np.array(list(parent2['solution'].keys()))
        mask2 = np.isin(parent2_cars, parent1_cars)
        cars_to_choose_fom_parent2 = parent2_cars[~ mask2]
        if len(cars_to_choose_fom_parent2) > 0:
            car2 = np.random.choice(cars_to_choose_fom_parent2)
            route2 = parent2['solution'][car2]
            new_solution1 = self._delete_customers(parent1['solution'],route2)
            new_solution1[car2] = route2
            parent1['solution'] = new_solution1


        return parent1, parent2

    def _delete_customers(self,solution,customers):
        old_customers = [c for route in solution.values() for c in route]
        o = len(old_customers)
        count = len(customers)

        new_solution = dict()

        for car,route in solution.items():
            for customer in customers:
                if np.isin(customer,route):
                    i = np.argwhere(route==customer)
                    route = np.delete(route,i)

                    i = np.argwhere(customers == customer)
                    customers = np.delete(customers, i)
            if len(route) > 0:
                new_solution[car]=route

        new_customers = [c for route in new_solution.values() for c in route]

        n = len(new_customers)

        #assert len(np.unique(old_customers)) > len(np.unique(new_customers))
        assert len(np.unique(old_customers)) - len(np.unique(new_customers)) == count

        return new_solution