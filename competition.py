from concurrent.futures import ProcessPoolExecutor
from itertools import chain

import os
import random
import sys
import time


sys.path.append("bots")
from game import Match

# Excluded bots are those that don't try to win, or that are broken
# in a way that breaks the competition.
EXCLUDED = ["duke_or_die_bot", "ultimateCHEATERBOT_obf", "sable_secret_bot"]

NUM_PLAYERS = 6


def match_worker(bots, iterations):
    sys.path.append("bots")
    match = Match([__import__(x) for x in bots])
    winners = match.repeat(iterations)

    return [[(x, w == x) for x in bots] for w in winners]


def parallel_execute(threads, groups, iterations):
    results = []
    
    if len(groups) == 1:
        return [match_worker(groups[0], iterations)]
    else:
        futures = []
        with ProcessPoolExecutor(max_workers=threads) as executor:             
            for group in groups:
                futures.append(executor.submit(
                    match_worker, group, iterations))

    return [x.result() for x in futures]

def rate_skill(names, results):
    from trueskill import Rating, rate, setup
    MU = 1000
    setup(MU, MU / 3, MU * 5, MU / 5000)
    
    started = time.clock()
    ratings = {x : Rating() for x in names}
    for entry in results:
        adjusted = rate([(ratings[x[0]],) for x in entry],
                        [(int(not x[1]),) for x in entry])
        for index, rating in enumerate(adjusted):
            ratings[entry[index][0]] = rating[0]

    print("Completed rankings in", str(int(time.clock() - started)), "seconds")
    print("")

    descending = sorted(ratings.items(), key=lambda x:x[1], reverse=True)
    for name, rating in descending:
        print(name)
        print("   ", "Mu: %.0f" % rating.mu)
        print("   ", "Sigma: %.0f" % rating.sigma)
        print("")

def compete(names, matches, iterations, ratings, threads):
    groups = [random.sample(names, NUM_PLAYERS) for x in range(matches)]
    
    started = time.clock()
    results = parallel_execute(threads, groups, iterations)
    results = list(chain.from_iterable(results))

    # TrueSkill weights later results more heavily to account for skill
    # changing over time. That doesn't happen across matches here,
    # but there can be considerable variance between matches. Minimize
    # that effect by interleaving all the match results.
    results = list(chain.from_iterable(zip(results)))
    
    print("Completed matches in", str(int(time.clock() - started)), "seconds")
    print("")

    if len(groups) == 1:  
        for index, name in enumerate(groups[0]):
            print(name + "@" + str(index))
        print("")

    # Remove any bots that didn't play to avoid singularities.
    names = set(chain.from_iterable(groups))

    totals = []
    for name in names:
        wins = sum(sum(1 for y in x if y[0] == name and y[1])
                   for x in results)
        played = sum(sum(1 for y in x if y[0] == name)
                   for x in results)
        totals.append((name, wins, played))

    for name, wins, played in sorted(
        totals, key=lambda x: x[1] / x[2], reverse=True):
        print(name)
        print("   ", "Wins:", wins)
        print("   ", "Played:", played)
        print("   ", "Rate: %.4f" % (wins / played))
        print("")

    if ratings:
        rate_skill(names, results)
        

def main(argv):
    threads = 5
    matches = 50
    iterations = 10000
    ratings = True
    
    names = [x[:-3] for x in os.listdir("bots") if x[-3:] == ".py"]
    names.remove("__init__")
    names = [x for x in names if x not in EXCLUDED]

    compete(names, matches, iterations, ratings, threads)
    

if __name__ == "__main__":
    sys.exit(main(sys.argv))
