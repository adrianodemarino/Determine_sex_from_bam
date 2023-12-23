import os,sys
import pandas as pd
 
'''
  +--------------------------------------------------------+
  |             Determine Sex in Homo Sapiens              |
  +--------------------------------------------------------+
  |  Author:   Adriano De Marino                           |
  |  Date:     April 2020 v1, Dec 2023 v2                  |
  |  Contact:  adriano.demarino@gmail.com                  |
  |  Version:  2.0.0                                       |
  +--------------------------------------------------------+
'''

# Usage: python determineSexFromBam.py [bam_file] [optional: filters]

def calculate_sex(df):
    try:
        x_reads = df.loc[df['chromosome'].str.contains('X', case=False), 'reads'].sum()
        y_reads = df.loc[df['chromosome'].str.contains('Y', case=False), 'reads'].sum()

        if y_reads == 0:  # Avoid division by zero
            return 'FEMALE'

        ratio = x_reads / y_reads
        return 'FEMALE' if ratio > 4 else 'MALE'
    except Exception as e:
        print("Error in calculating sex:", e)
        sys.exit(1)

def main():
    for file in sys.argv[1:]:
        basename = os.path.basename(file).replace(".bam", "")
        filters = sys.argv[2].split(',') if len(sys.argv) > 2 else ["Un", "random", "alt", "GL", "NC", "hs", "*", "fix", "M"]

        grep_command = ' | '.join([f'grep -v "{f}"' for f in filters])
        bash_command = f'samtools idxstats {file} | {grep_command} | sort -V | cut -f 1,3 > /tmp/{basename}.sex'

        try:
            os.system(bash_command)
            df = pd.read_csv(f"/tmp/{basename}.sex", sep="\t", names=["chromosome", "reads"])
        except Exception as e:
            print(f"Error processing {file}: {e}")
            continue

        sex = calculate_sex(df)
        print(f"{basename}\t{sex}")

if __name__ == "__main__":
    main()
