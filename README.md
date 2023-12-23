# Determine sex from Bam file
Determine sex in Homo sapiens sample from sorted bam file fastly using a simple python script.

Dec 2023 - new version
### Key Changes:
- **Error Handling**: Added more detailed error handling and messages.
- **Parameterization of Filters**: Users can now pass a comma-separated list of filters as a second argument. If no filters are provided, a default list is used.
- **Flexibility in Reference Genome**: The script now handles different chromosome naming conventions by checking if chromosome names are numeric for autosomes and looking for 'Y' in the chromosome name for Y chromosome reads.
- **Sex Determination Using X/Y Coverage Ratio**: The `calculate_sex` function now calculates the sum of reads for the X chromosome and the Y chromosome separately. It then computes the ratio of X to Y coverage. If this ratio is greater than 4, it classifies the sample as female; otherwise, it classifies it as male.
- **Handling Zero Y Reads**: To avoid division by zero, if the Y reads are zero, the function automatically classifies the sample as female.

## Usage:
```
python determineSexFromBam.py [bam_file] [optional: filters]
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

Sr Bioinfo Scientist
Adriano De Marino, PhD 

Contact: <adriano.demarino@gmail.com>
