from concurrent.futures import ProcessPoolExecutor
from collections import Counter

import os
import random
import sys
import time

sys.path.append("bots")
from game import Match, log


def worker(bots, iterations):
    sys.path.append("bots")
    match = Match([__import__(x) for x in bots])
    return match.repeat(iterations)


def parallel(bots, threads, matches, iterations):
    final = Counter()
 
    if matches == 1:
        print("one")
        final.update(worker(bots, iterations))
    else:
        futures = []
        with ProcessPoolExecutor(max_workers=threads) as executor:             
            for x in range(matches):
                futures.append(executor.submit(
                    worker, bots, iterations))

        for result in futures:
            final.update(result.result())
        
    print("")
    for key in sorted(final):
        print(key, "%.4f" % (final[key] / (matches * iterations)),
              "(" + str(final[key]) + ")")
        

def select_bots(num_players, required, excluded, names):
    available = [x for x in names if x not in excluded]
    
    if len(required) >= num_players:
        return random.sample(required, num_players)

    needed = num_players - len(required)
    
    if len(names) - len(set(required)) < needed:
        return required + [random.choice(names) for x in range(needed)]
    
    return required + random.sample(set(names) - set(required), needed)


def main(argv):
    threads = 6
    matches = 6
    iterations = 10000
    required = []
    excluded = ["duke_or_die_bot"]
    num_players = 6

    # Note that there's no output when running more than one match
    log.verbose = False
    
    names = [x[:-3] for x in os.listdir("bots") if x[-3:] == ".py"]
    names.remove("__init__")
    
    bots = select_bots(num_players, required, excluded, names)
    started = time.clock()
    parallel(bots, threads, matches, iterations)

    print("")
    print("Completed in", str(int(time.clock() - started)), "seconds")

            
if __name__ == "__main__":
    sys.exit(main(sys.argv))
