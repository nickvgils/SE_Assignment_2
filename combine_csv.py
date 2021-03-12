import os
import glob
import pandas as pd
path = r'C:\Users\sword\Documents\GitHub\SE_Assignment_2\out\jquery-data'                    # use your path
all_files = glob.glob(os.path.join(path, "*.csv"))     # advisable to use os.path.join as this makes concatenation OS independent
combined = pd.DataFrame(columns=('version', 'files', 'blank', 'comment', 'code'))

# Version 1.2.1 < 1.10.1
def get_order(file):
    filename = os.path.basename(file)
    filename = filename[:-4]
    return [int(_) for _ in filename.split(".")]

sorted_files = sorted(all_files, key=get_order)

for file in sorted_files:
    df = pd.read_csv(file)
    df_sum = df.tail(1).to_numpy()
    filename = os.path.basename(file)
    version = filename[:-4]
    combined = combined.append({'version' : version, 'files' : df_sum[0][0], 'blank' : df_sum[0][2], 'comment' : df_sum[0][3], 'code' : df_sum[0][4]}, ignore_index=True)

combined.to_csv(r'C:\Users\sword\Documents\GitHub\SE_Assignment_2\lines.csv', index=False)