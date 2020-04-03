# Determine sex from Bam file
Determine sex in Homo sapiens sample from bam file using a simple python script.

## Usage:
```
python determineSexFromBam.py file_name_1.bam file_name_2.bam [...]
```

## Component required:
1. [Samtools](http://www.htslib.org/) 
2. [Pandas](https://pandas.pydata.org/) 

## Installation component required:
```
conda install -c bioconda samtools
pip install pandas
```

## Output:

|	Sample	|	Sex	|
| ---  | ---  |
|	190106	|	MALE	|
|	191093	|	MALE	|
|	193012	|	FEMALE	|
|	182151	|	FEMALE	|
|	190169	|	MALE	|
|	190210	|	FEMALE	|

## Licence

This software is under 
GNU General Public License version 3
