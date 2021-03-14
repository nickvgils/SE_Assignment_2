import csv
import itertools
import json
import os
from distutils.version import LooseVersion
from sys import version

rootdir = "/usr/jquery-data"
outpath = "output.json"
csvpath = "similarities.csv"

# Param versions is expected to be a tuple of two versions
def getSimilarity(versions):
    # Stores the output of JsInspect inside a JSON file and then re-uses it
    command = f'jsinspect -I -L -r json --ignore "sizzle|intro.js$|outro.js$|Test.js$" {" ".join([os.path.join(rootdir, v, "src") for v in versions])} > {outpath}'
    print(f'Executing {command}')
    os.system(command)
    with open(outpath, 'r') as out:
        similarities = json.load(out, strict=False)
        return similarities

# Param versions is expected to be a tuple of two versions
# Returns the total number of similar lines
def compareVersions(versions):
    print(versions)
    # Avoids comparing to same or older versions
    if LooseVersion(versions[0]) >= LooseVersion(versions[1]):
        return 0
    similarities = getSimilarity(versions)
    similarity_ranges = {}
    similar_lines = 0
    # Similar lines are stored per file in a set
    for clone in similarities:
        for instance in clone["instances"]:
            if instance["path"] in similarity_ranges:
                similarity_ranges[instance["path"]].update(range(instance["lines"][0], instance["lines"][1] + 1))
            else:
                similarity_ranges[instance["path"]] = set(range(instance["lines"][0], instance["lines"][1] + 1))

    for file, rg in similarity_ranges.items():
        similar_lines += len(rg)
    return similar_lines

with os.scandir(rootdir) as root:
    versions = sorted([ver.name for ver in root if ver.is_dir()], key=LooseVersion)
    # Cartesian product to retrieve all possible pairs
    version_pairs = itertools.product(versions, versions)
    similarities = {}
    for version in versions:
        similarities[version] = {}
    for pair in version_pairs:
        similarities[pair[0]][pair[1]] = compareVersions(pair)

    with open(csvpath, 'w+') as result:
        writer = csv.writer(result, delimiter=',', quotechar='\"')
        fields = ["version"] + versions
        writer.writerow(fields)
        for version in versions:
            writer.writerow([version] + [similarities[version][x] for x in versions])