


class Evaporator:

    def __init__(self,rho=0.5):
        self.rho = rho

    def evaporate(self,pheromone_matrix):
        pheromone_matrix = (1-self.rho) * pheromone_matrix

        return pheromone_matrix


