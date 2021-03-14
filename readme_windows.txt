This directory already contains the resulting files from the python scripts.
They can be obtained by following the following process:

- Open cmd.exe and run 'docker build -t 2imp25-assignment2 .'
- Next, run 'docker run -it --rm -v "%cd%/out:/out/" 2imp25-assignment2'

Lines of code stored in lines.csv:
- Open another cmd in the root folder and run 'docker ps' to see the container id.
- Then copy lines.csv from container to host using 'docker cp <containerId>:/usr/jquery-data/lines.csv .'

Similarity between all versions stored in similarities.csv:
- Inside bash, run 'python compute_code_clones.py'
- Wait for approximately 50 minutes for completion
- Open another cmd in the root folder and run 'docker ps' to see the container id.
- Run 'docker cp <containerId>:/usr/jquery-data/similarities.csv .'

All created figures are stored in the root folder in SE_Assignment_2/
Manually run 'python bar_chart.py' in cmd to create the bar charts "barchart.png" and "filesbarchart.png".
Manually run 'python heat_map.py' in cmd to create the heatmap "heatmap.png".
