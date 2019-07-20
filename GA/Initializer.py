import numpy as np
from copy import deepcopy
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
LOG = logging.getLogger(__name__)
LOG.propagate = False


class Random_Initializer:

    def initialize_pop(self, task, pop_size=10):
        np.random.seed(0)
        customer_indices = np.arange(len(task.demands)) + 1
        car_indices = np.arange(len(task.capacities))
        pop = []
        for i in range(pop_size):
            # LOG.info('Create Individual Number: {}'.format(i+1))
            individual = self._create_individual_random(customer_indices,
                                                        car_indices,
                                                        task.demands,
                                                        task.capacities,)
            pop.append(individual)

        return pop

    def _create_individual_random(self, customer_indices, car_indices, demands, capacities):
        """
        creates random individuals by choosing cars randomly car and filling them up with
        randomly chosen customer demands until its full
        :param customer_indices: the customers
        :param car_indices: the cars
        :param demands: the customer demands
        :param capacities: the car capacities
        :return: and randomly created solution: a dict containing the car-customer assignments and the fitness
        """
        left_customers_indices = deepcopy(customer_indices)
        left_car_indices = deepcopy(car_indices)
        solution = dict()

        # while not all customers are served
        while len(left_customers_indices) >= 1:

            # choose a car and delete it from the list
            car = np.random.choice(left_car_indices)
            i = np.where(left_car_indices == car)
            left_car_indices = np.delete(left_car_indices, i)
            capacity = capacities[car]
            # LOG.info('Car with {} capacity is chosen'.format(capacity))

            # choose a new customer randomly
            # next_customer = np.random.choice(left_customers_indices)
            # next_demand = demands[next_customer - 1]
            next_demand = 0
            route = []

            # while there is enough room in the car for the next customer
            # and at least one customer is left
            while (capacity - next_demand > 0) & (len(left_customers_indices) > 0):
                # LOG.info('Next Customer: {} with demand {}, {} left customers'.format(next_customer,
                # next_demand,len(left_customers_indices)))
                next_customer = np.random.choice(left_customers_indices)
                next_demand = demands[next_customer - 1]

                # append the next customer to the car-route
                capacity -= next_demand
                route.append(next_customer)

                # delete it from the leftover customers
                i = np.argwhere(left_customers_indices == next_customer)
                left_customers_indices = np.delete(left_customers_indices, i)

                # get the next customer
                # next_customer = np.random.choice(left_customers_indices)
                # next_demand = demands[next_customer - 1]

            solution[car] = route

        individual = dict()
        individual['solution'] = solution
        # initial fitness is zero, will be changed by initial evaluation
        individual['fitness'] = 0

        return individual


class Heuristic_Initializer:

    def initialize_pop(self, task, pop_size=10):
        np.random.seed(0)
        customer_indices = np.arange(len(task.demands))+1
        car_indices = np.arange(len(task.capacities))
        pop = []
        for i in range(pop_size):
            # LOG.info('Create Individual Number: {}'.format(i+1))
            individual = self._create_individual(customer_indices,
                                                 car_indices,
                                                 task.demands,
                                                 task.capacities,
                                                 task.customer_matrix)
            pop.append(individual)

        return pop

    def _create_individual(self, customer_indices, car_indices, demands, capacities, customer_matrix):
        """
        creates solutions using a heuristic: close customers should be next to each other in a car-route
        :param customer_indices: customers
        :param car_indices: cars
        :param demands: customer demands of task
        :param capacities: car capacities of task
        :param customer_matrix: the distance matrix that only contains the needed customers
        :return:
        """
        customer_matrix = deepcopy(customer_matrix)
        left_customers_indices = deepcopy(customer_indices)
        left_car_indices = deepcopy(car_indices)

        solution = dict()

        # while not all customers are served
        while len(left_customers_indices) > 0:

            # choose a car and delete it fromm the list
            car = np.random.choice(left_car_indices)
            i = np.where(left_car_indices == car)
            left_car_indices = np.delete(left_car_indices, i)
            capacity = capacities[car]
            # LOG.info('Car with {} capacity is chosen'.format(capacity))

            next_customer = np.random.choice(left_customers_indices)
            next_demand = demands[next_customer-1]

            route = []

            # while there is enough room in the car for the next customer
            # and at least one customer is left
            while (capacity-next_demand > 0) & (len(left_customers_indices) > 0):
                # LOG.info('Next Customer: {} with demand {}, {} left customers'.format(next_customer, next_demand,
                # len(left_customers_indices)))
                # append the next customer to the car-route
                capacity -= next_demand
                route.append(next_customer)

                # delete it from the leftover customers
                i = np.argwhere(left_customers_indices == next_customer)
                left_customers_indices = np.delete(left_customers_indices, i)
                # and make the distance to it infinite
                customer_matrix[next_customer, :] = 1000000

                # get the next customer
                next_customer = self._get_closest_customer(next_customer,customer_matrix)
                next_demand = demands[next_customer-1]
            LOG.info('Car {} got route {}'.format(car, str(route)))
            solution[car] = route

        individual = dict()
        individual['solution'] = solution
        # initial fitness is zero, will be changed by initial evaluation
        individual['fitness'] = 0

        return individual

    def _get_closest_customer(self,customer, customer_matrix):
        """
        returns the next clostest customer to a given customer
        :param customer: distance matrix
        :param customer_matrix: customer
        :return: next clostest customer
        """

        return customer_matrix[:, customer].argmin()



