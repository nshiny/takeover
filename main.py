# TODO: Parameter to force certain bots into the matches.
# TODO: Select bots without replacement when there are enough.


import os
import random
import sys

sys.path.append("bots")
from game import Match


def get_bots(path):
    names = [x[:-3] for x in os.listdir(path) if x[-3:] == ".py"]
    names.remove("__init__")

    return [__import__(x) for x in names]


def main(argv):
    bots = get_bots("bots")
    match = Match([random.choice(bots) for x in range(6)])
    match.repeat(1)

            
if __name__ == "__main__":
    sys.exit(main(sys.argv))
