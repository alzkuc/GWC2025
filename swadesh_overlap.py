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
path = 'PATH/TO/Conceptlists'
common_concepts_dict = {}
for file_name in file_paths:
    df = pd.read_csv(path + file_name, sep='\t')
    dataset_concepts = df['CONCEPTICON_GLOSS'].tolist()
    
    #Finds common concepts between swadeshnouns and each dataset
    common_concepts = set(swadeshnouns) & set(dataset_concepts)
    
    #Stores sorted list of common concepts in the dictionary
    common_concepts_dict[file_name] = sorted(common_concepts)

    #Prints the common concepts and the count
    print(f"Common concepts found in {file_name}: {common_concepts_dict[file_name]}")
    print(f"Number of common concepts in {file_name}: {len(common_concepts_dict[file_name])}")