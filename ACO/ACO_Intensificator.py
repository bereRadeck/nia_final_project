
class Intensificator:

    def __init__(self,delta=1):
        self.delta = delta

    def intensify(self,pheromone_matrix,solutions):
        best_solution = solutions[0]

        for i in range(len(best_solution)-1):
            origin = best_solution[i]
            destination = best_solution[i+1]
            pheromone_matrix[origin, destination] = pheromone_matrix[origin, destination] + self.delta

        return pheromone_matrix
