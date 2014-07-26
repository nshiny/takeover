import os
import random
import sys

from game import log
from competition import compete, EXCLUDED


def select_bots(num_players, required, excluded, names):
    available = [x for x in names if x not in excluded]
    
    if len(required) >= num_players:
        return random.sample(required, num_players)

    needed = num_players - len(required)
    
    if len(available) - len(set(required)) < needed:
        return required + [random.choice(available) for x in range(needed)]
    
    return required + random.sample(set(available) - set(required), needed)


def main(argv):
    iterations = 10
    required = ["turtle_bot"]
    excluded = EXCLUDED
    num_players = 6

    # Note that there's no output when running more than one match
    log.verbose = True
    
    names = [x[:-3] for x in os.listdir("bots") if x[-3:] == ".py"]
    names.remove("__init__")
    
    bots = select_bots(num_players, required, excluded, names)

    compete(bots, 1, iterations, False, 1)

            
if __name__ == "__main__":
    sys.exit(main(sys.argv))
