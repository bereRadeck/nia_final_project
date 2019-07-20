import numpy as np
from os.path import join
from copy import deepcopy


class Task:

    def __init__(self, PATH = 'problem'):
        """
        hold all the infomration about a VRP
        :param PATH:
        """
        self.capacities = parsefile(join(PATH, "capacity.txt"))
        self.distance_matrix = parsefile(join(PATH, "distance.txt"))
        self.transportation_costs = parsefile(join(PATH, "transportation_cost.txt"))
        self.demands = parsefile(join(PATH, "demand.txt"))
        self.num_customers = len(self.demands)
        self.num_cars = len(self.capacities)
        self.customer_matrix = deepcopy(self.distance_matrix)
        self.customer_matrix[0,:] = 1000000
        self.customer_matrix[:,0] = 1000000


def parsefile(filename):
    with open(filename) as filereader:
        file_array = []
        for line in filereader:
            line = line.split(' ')
            line = [int(value) for value in line if value != '' and value != "\n"]

            file_array.append(line)
    if len(file_array) == 1:
        file_array = file_array[0]
    file_array = np.asarray(file_array)

    return file_array


def read_task(PATH):
    capacities = parsefile(join(PATH, "capacity.txt"))
    distance_matrix = parsefile(join(PATH," distance.txt"))
    transportation_costs = parsefile(join(PATH, "transportation_cost.txt"))
    demands = parsefile(join(PATH, "demand.txt"))

    """
    print(len(distance_matrix))
    print(len(distance_matrix[0]))
    print(len(capacities))
    print(len(transportation_costs))
    print(len(demands))
    """
    return distance_matrix, capacities, transportation_costs, demands