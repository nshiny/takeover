# TODO: Parameter to force certain bots into the matches.
# TODO: Select bots without replacement when there are enough.


import os
import random
import sys

sys.path.append("bots")
from game import Match, log


def get_bots(path):
    names = [x[:-3] for x in os.listdir(path) if x[-3:] == ".py"]
    names.remove("__init__")

    return [__import__(x) for x in names]


def select_bots(required, bots):
    named = {x.__name__ : x for x in bots}
    required = [named[x] for x in required]
    
    if len(required) >= 6:
        return random.sample(required, 6)

    needed = 6 - len(required)
    
    if len(bots) - len(set(required)) < needed:
        return required + [random.choice(bots) for x in range(needed)]
    
    return required + random.sample(set(bots) - set(required), needed)


def main(argv):
    iterations = 1
    verbose = True
    required = ["turtle_bot"]
    
    log.verbose = verbose
    bots = get_bots("bots")
    
    match = Match(select_bots(required, bots))
    match.repeat(iterations)

            
if __name__ == "__main__":
    sys.exit(main(sys.argv))
