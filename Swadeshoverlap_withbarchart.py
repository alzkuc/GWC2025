#This Python script calculates and presents the overlap of concepts within the 17 datasets with Swadesh 1955. 
#Note: For this script, one must first download and save the Swadesh_POStagged.tsv file (Under: Additional Data).

import pandas as pd

file_path = 'PATH/TO/Swadesh_POStagged.tsv'
df= pd.read_csv (file_path, sep='\t')
swadeshnouns = (df[df['POS_Tag'] == "NOUN"]['CONCEPTICON_GLOSS'].tolist()) #all Swadesh nouns saved into a variable
print((len)(swadeshnouns)) #the amount of nouns in Swadesh 1955
print((swadeshnouns)) #the nouns

#Specific comparison: which Swadesh concepts and how many are present in which dataset
file_paths = [
    'Hwang-2021-60.tsv',
    'Snodgrass-1980-260.tsv',
    'MorenoMartinez-2012-360.tsv',
    'Tsaparina-2011-260.tsv',
    'Dunabeitia-2018-750.tsv',
    'vanDort-2007-50.tsv',
    'Nishimoto-2005-359.tsv',
    'Boukadi-2015-348.tsv',
    'Shao-2016-327.tsv',
    'Bangalore-2022-180.tsv',
    'Zhong-2024-1286.tsv',
    'Raman-2013-260.tsv',
    'Dimitropoulou-2009-260.tsv',
    'Rogic-2013-346.tsv',
    'Liu-2011-435.tsv',
    'Ramanujan-2019-158.tsv',
    'Dunabeitia-2022-500.tsv'
]
path = 'PATH/TO/conceptlists/'
common_concepts_dict = {}
for file_name in file_paths:
    df = pd.read_csv(path + file_name, sep='\t')
    dataset_concepts = df['CONCEPTICON_GLOSS'].tolist()
    common_concepts = set(swadeshnouns) & set(dataset_concepts)
    common_concepts_dict[file_name] = sorted(common_concepts)

import matplotlib.pyplot as plt
import numpy as np

common_counts = [len(common_concepts_dict[file_name]) for file_name in file_paths]
dataset_names = file_paths  

sorted_data = sorted(zip(common_counts, dataset_names), key=lambda x: x[0], reverse=True)
sorted_counts, sorted_names = zip(*sorted_data)
norm = plt.Normalize(min(sorted_counts), max(sorted_counts))
cmap = plt.cm.Oranges
plt.figure(figsize=(10, 6))
bars = plt.bar(sorted_names, sorted_counts, color=cmap(norm(sorted_counts)))

for bar, count in zip(bars, sorted_counts):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),                  #Height
        str(count),                        #Displaying the count
        ha='center',                       
        va='bottom',                       
        fontsize=10                        
    )

#plt.ylabel('Number of Concepts shared with Swadesh')
#plt.xlabel('Dataset Name')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


