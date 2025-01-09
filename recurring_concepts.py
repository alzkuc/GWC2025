#This Python script accesses the previously created concept_frequency.py file and extracts concepts that appear in at least 15, 16, or all 17 out of 17 datasets, then prints them.import pandas as pd 

import pandas as pd 
file_path = 'PATH/TO/ConceptFrequency.tsv'
df = pd.read_csv (file_path, sep='\t')

concepts_15lists=set(df[df['FREQUENCY (MAX. 17)'] >= 15]['CONCEPTICON GLOSS'].tolist())
concepts_16lists=set(df[df['FREQUENCY (MAX. 17)'] >= 16]['CONCEPTICON GLOSS'].tolist())
concepts_17lists=set(df[df['FREQUENCY (MAX. 17)'] == 17]['CONCEPTICON GLOSS'].tolist())

print((len)(concepts_15lists)) #number of recurring concepts in at least 15 out of 17 datasets
print(concepts_15lists) #prints concepts that appear in at least 15 out of 17 datasets
print(concepts_16lists) #prints concepts that appear in at least 16 out of 17 datasets
print(concepts_17lists) #prints concepts that appear in all 17 out of 17 datasets