from concurrent.futures import ProcessPoolExecutor
from itertools import chain

import argparse
import json
import os
import random
import sys
import time


sys.path.append("bots")
from game import Match

# Excluded bots are those that don't try to win, or that are broken
# in a way that breaks the competition.
EXCLUDED = ["duke_or_die_bot", "ultimateCHEATERBOT_obf"]

NUM_PLAYERS = 6


def match_worker(bots, iterations):
    sys.path.append("bots")
    match = Match([__import__(x) for x in bots])
    winners = match.repeat(iterations)

    return [[(x, w == x) for x in bots] for w in winners]


def parallel_execute(parallel, groups, iterations):
    results = []
    
    if len(groups) == 1:
        return [match_worker(groups[0], iterations)]
    else:
        futures = []
        with ProcessPoolExecutor(max_workers=parallel) as executor:             
            for group in groups:
                futures.append(executor.submit(
                    match_worker, group, iterations))

    return [x.result() for x in futures]

def rate_skill(names, results, metrics):
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
    for index, (name, rating) in enumerate(descending):
        metrics[name]["Rank"] = index
        metrics[name]["Mu"] = "%.0f" % rating.mu
        metrics[name]["Sigma"] = "%.0f" % rating.sigma

        
def compete(names, matches, iterations, ratings, parallel):
    groups = [random.sample(names, NUM_PLAYERS) for x in range(matches)]
    
    started = time.clock()
    results = parallel_execute(parallel, groups, iterations)
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

    metrics = {x : {} for x in names}
    for name, wins, played in sorted(
        totals, key=lambda x: x[1] / x[2], reverse=True):

        rate = "%.4f" % (wins / played)

        metrics[name]["Wins"] = wins
        metrics[name]["Played"] = played
        metrics[name]["Rate"] = rate

        print(name)
        print("   ", "Wins:", wins)
        print("   ", "Played:", played)
        print("   ", "Rate:", rate)
        print("")
        
    if ratings:
        rate_skill(names, results, metrics)

    return metrics
        

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--parallel", type=int, default=5,
                        help="number of parallel processes")
    parser.add_argument("-m", "--matches", type=int, default=50,
                        help="number of matches in the competition")
    parser.add_argument("-i", "--iterations", type=int, default=10000,
                        help="number of iterations in a match")
    parser.add_argument("-s", "--skip-ratings", action="store_true",
                        help="skip ratings generation")
    parser.add_argument("-j", "--json-file", default=None,
                        help="path to file for json results output")
    args = parser.parse_args(argv)
    
    names = [x[:-3] for x in os.listdir("bots") if x[-3:] == ".py"]
    names.remove("__init__")
    names = [x for x in names if x not in EXCLUDED]

    metrics = compete(names, args.matches, args.iterations,
                      not args.skip_ratings, args.parallel)
    
    if args.json_file is not None:
        with open(args.json_file, "w") as file:
            file.write(json.dumps(metrics, indent=4))    

    metrics = sorted(metrics.items(), key=lambda x: x[1]["Rank"])
    for name, entry in metrics:
        print("")
        print(name)
        for key, value in entry.items():
            print("   ", key, value)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
