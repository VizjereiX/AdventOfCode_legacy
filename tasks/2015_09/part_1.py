from typing import DefaultDict
import itertools

logger = None



def run(filename):
    distances = DefaultDict(dict)

    with open(filename, "r") as f:
        data = f.read()
        for line in data.splitlines():
            line = line.strip()
            cities, distance = line.split(" = ")
            c1, c2 = cities.split(" to ")
            distances[c1][c2] = int(distance)
            distances[c2][c1] = int(distance)


        minDist = int(1e100)
        for perm in itertools.permutations(distances.keys()):
            total_distance = 0
            for i in range(len(perm) - 1):
                total_distance += distances[perm[i]][perm[i + 1]]
            if total_distance < minDist:
                minDist = total_distance

    return str(minDist)