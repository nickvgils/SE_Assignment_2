import csv
import os
import sys
import numpy as np
from matplotlib import pyplot as plt

def create_barchart(data, pngpath):
    fig, axes = plt.subplots()
    plt.sca(axes)
    # Draw barchart
    axes.bar(versions, data)
    # Set the tick labels as versions
    plt.xticks([i for i in range(len(versions))], versions, rotation=90, fontsize=4)
    fig.set_size_inches(7, 5)
    # Save image
    plt.savefig(pngpath, dpi=1000)

if __name__ == "__main__":
    with open(os.path.join(sys.path[0], "lines.csv"), mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader) # Skips headers row
        data = [row for row in csv_reader]
        versions = [i[0] for i in data]
        sizes = [i[1:] for i in data]
        loc = [int(x[1]) + int(x[2]) + int(x[3]) for x in sizes]

        create_barchart(np.array(loc), os.path.join(sys.path[0], "barchart.png"))
