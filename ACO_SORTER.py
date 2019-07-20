
from ACO.ACO_Main import ACO
from copy import deepcopy
import numpy as np
import logging
import sys
import numpy as np
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
LOG = logging.getLogger(__name__)

class ACO_Sorter:

    def __init__(self,aco_initializer,
                 aco_solutiongenerator,
                 aco_evaporator,
                 aco_intensificator,
                 distance_matrix,
                 aco_iterations):

        self.ACO = ACO(deepcopy(distance_matrix),
                       aco_initializer,
                       aco_solutiongenerator,
                       aco_evaporator,
                       aco_intensificator,
                       aco_iterations,True)


    def sort_routes(self,pop):
        for i,p in enumerate(pop):

            for key, route in p['solution'].items():

                if len(route) > 2:
                    #LOG.info('Old route: {}'.format(str(route)))
                    new_route_indices = self.ACO.run(route)
                    #LOG.info('New indices route: {}'.format(str(new_route_indices)))

                    assert len(new_route_indices) == len(route)
                    #LOG.info('New Route: {}'.format(str(np.array(route)[new_route_indices])))
                    p['solution'][key] = np.array(route)[new_route_indices]


        return pop

    def sort_singe_route(self, route):

        new_route_indices = self.ACO.run(route)
        assert len(new_route_indices) == len(route)
        new_route = np.array(route)[new_route_indices]
        return new_route

