# Determine sex from Bam file
Determine sex in Homo sapiens sample from sorted bam file fastly using a simple python script.

## Usage:
```
python determineSexFromBam.py file_name_1.bam file_name_2.bam [...] file_name_n.bam
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

[MIT LICENCE](https://github.com/adrianodemarino/Determine_sex_from_bam/blob/master/LICENSE.md)

## Author info

Adriano De Marino, MS, PhD student

Contact: <adriano.demarino@gmail.com>
