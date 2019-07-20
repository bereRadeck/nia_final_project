import logging
import sys
import numpy as np
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
LOG = logging.getLogger(__name__)
class Replacer:

    def __init__(self):
        pass

    def replace(self, pop, offspring):

        fitnesses = [p['fitness'] for p in pop]
        pop = [x for x, _ in sorted(zip(pop,fitnesses), reverse=True,key=lambda pair: pair[1])]
        l = len(offspring)

        new_pop = np.append(offspring,pop[l:])
        assert len(new_pop) == len(pop)
        fitnesses_after = [p['fitness'] for p in pop]
        if np.min(fitnesses) != np.min(fitnesses_after):
            LOG.info('WARNING: Minimum is replaced')
        return new_pop
