import csv
import numpy as np
import os
import sys
from matplotlib import pyplot as plt
from matplotlib import colors
from distutils.version import LooseVersion

linespath = os.path.join(sys.path[0], "lines.csv")
similarpath = os.path.join(sys.path[0], "similarities.csv")
coveragepath = os.path.join(sys.path[0], "coverage.csv")
loc = []
similarities = []
versions = []

# Get lines of code count
with open(linespath, mode='r') as loc_file:
    loc_reader = csv.reader(loc_file)
    next(loc_reader)
    data = [row for row in loc_reader]
    versions = [i[0] for i in data]
    sizes = [i[1:] for i in data]
    loc = [int(x[1]) + int(x[2]) + int(x[3]) for x in sizes]

# Get similarities
with open(similarpath, mode='r') as sim_file:
    sim_reader = csv.reader(sim_file)
    next(sim_reader)
    similarities = [row[1:] for row in sim_reader]

coverage = [[
    float(y) / (loc[i] + loc[j]) for j, y in enumerate(x)
] for i, x in enumerate(similarities)]
with open(os.path.join(sys.path[0], "coverage.csv"), 'w+') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='\"')
    fields = ["version"] + versions
    writer.writerow(fields)
    for i, x in enumerate(versions):
        writer.writerow([x] + coverage[i])

# Create the heatmap
cmap = {
    'red': [
        [0.0, 1.0, 1.0],
        [0.25, 0.0, 0.0],
        [0.5, 0.0, 0.0],
        [0.75, 1.0, 1.0],
        [1.0, 1.0, 1.0]
    ],
    'green' : [
        [0.0, 1.0, 1.0],
        [0.25, 1.0, 1.0],
        [0.5, 1.0, 1.0],
        [0.75, 1.0, 1.0],
        [1.0, 0.0, 0.0]
    ],
    'blue': [
        [0.0, 1.0, 1.0],
        [0.25, 1.0, 1.0],
        [0.5, 0.0, 0.0],
        [0.75, 0.0, 0.0],
        [1.0, 0.0, 0.0]
    ]
}
colormap = colors.LinearSegmentedColormap('heatcolormap', segmentdata=cmap, N=256)
fig, axes = plt.subplots(nrows=2, gridspec_kw={'height_ratios': [60, 1]})
plt.sca(axes[0])
# Coordinates range from zero to the cumulative sum of the lines of code
coords = np.cumsum(np.append([0], np.array(loc)))
mesh_x, mesh_y = np.meshgrid(coords, -coords)
axes[0].pcolormesh(mesh_x, mesh_y, np.array(coverage).transpose(), cmap=colormap)
# Put label in middle of the cells
label_coords = np.array([(x + coords[i+1])/2 for i, x in enumerate(coords) if i < len(coords) - 1])
# Filter coordinates for new versions
version_coords = [coords[i] for i, x in enumerate(versions) if x.count(".") <= 1 or (LooseVersion(x) >= LooseVersion('1.8') and x[-2:] == ".0")]
axes[0].tick_params(length=0)
plt.xticks(label_coords, versions, rotation=90, fontsize=3)
plt.yticks(-label_coords, versions, rotation=0, fontsize=3)
# Plot lines that give clear visualization of version seperation
plt.hlines(-np.array(version_coords), min(coords), max(coords), linewidth=1)
plt.hlines(-coords, min(coords), max(coords), linewidth=0.2)
plt.vlines(np.array(version_coords), -min(coords), -max(coords), linewidth=1)
plt.vlines(coords, -min(coords), -max(coords), linewidth=0.2)

# Subplot for gradient scale
gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))
plt.sca(axes[1])
axes[1].imshow(gradient, aspect='auto', cmap=colormap)
axes[1].tick_params(length=0)
plt.xticks([0, 255], [0, 1])
plt.yticks([])
fig.tight_layout()
fig.set_size_inches(7, 8)

plt.savefig(os.path.join(sys.path[0], "heatmap.png"), dpi=1000)