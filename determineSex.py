import os,sys
import pandas as pd

for file in sys.argv[1:]:
	
	basename = file.replace(".bam","")
	
	bashCommand = 'samtools idxstats {file} | \
	grep -v "Un" | \
	grep -v "random" | \
	grep -v "alt" | \
	grep -v "*" | \
	grep -v "M" | \
	sort -V | \
	cut -f 1,3 > /tmp/{out}.sex'.format(file=file,out=basename)

	try:
		os.system(bashCommand)
		df = pd.read_csv("/tmp/{file}.sex".format(file=basename),sep="\t",header=None) 
	except Exception as e:
		"Are you using sorted bam file ?"
		exit()
	
	autosom = int(df.loc[0:21,1].mean()) 

	if df.loc[22,1]/autosom <= 0.5: 
		print(basename,"\t","MALE",sep="") 
	else: 
		print(basename,"\t","FEMALE",sep="")

exit()
