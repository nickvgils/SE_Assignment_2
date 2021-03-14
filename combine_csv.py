import os
import glob
import pandas as pd
command = f'for d in * ; do (echo "$d" && cloc --include-lang=JavaScript --csv --out=$d.csv --match-d=\'src\' $d); done'
print(f'Executing {command}')
os.system(command)
all_files = glob.glob('./*.csv')
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

combined.to_csv('lines.csv', index=False)