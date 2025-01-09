#This Python script generates a .tsv file that lists concept sets from our concept lists. For each concept, the script records the number of datasets where the concept appears and identifies the datasets where the concept is missing.

import os
import pandas as pd
from collections import defaultdict

#Define the path to the folder, where you stored the datasets from our OSF Project
folder_path = 'PATH/TO/conceptlists'
conceptlistIDs = [
    'Hwang-2021-60',
    'Snodgrass-1980-260',
    'MorenoMartinez-2012-360',
    "Tsaparina-2011-260",
    "Dunabeitia-2018-750",
    "vanDort-2007-50",
    "Nishimoto-2005-359",
    "Boukadi-2015-348",
    "Shao-2016-327",
    "Bangalore-2022-180",
    "Zhong-2024-1286",
    "Raman-2013-260",
    "Dimitropoulou-2009-260",
    "Rogic-2013-346",
    "Liu-2011-435",
    "Ramanujan-2019-158",
    "Dunabeitia-2022-500"
]

#Initialize a defaultdict to hold the gloss data
gloss_data = defaultdict(list)

#Populate gloss_data with counts
for file_name in conceptlistIDs:
    file_path = os.path.join(folder_path, f"{file_name}.tsv")
    try:
        df = pd.read_csv(file_path, sep='\t')
        
        if 'CONCEPTICON_GLOSS' in df.columns:
            gloss_counts = df['CONCEPTICON_GLOSS'].value_counts()
            
            for gloss, count in gloss_counts.items():
                gloss_data[gloss].append(file_name)
        else:
            print(f"'CONCEPTICON_GLOSS' not found in {file_name}")
    except Exception as e:
        print(f"Error reading {file_name}: {e}")

#Create a set of all lists for checking missing concepts
all_lists = set(conceptlistIDs)
output_data = []

#For each gloss, determine which lists it's present in and which it’s missing from:
for gloss in gloss_data.keys():
    present_lists = set(gloss_data[gloss])  #Lists where present
    present_count = len(present_lists)       #Frequency
    missing_lists = all_lists - present_lists #Lists where absent
    
    if present_count < len(all_lists):  #Only include missing lists if not all are present
        missing_list_info = "; ".join(missing_lists) 
    else:
        missing_list_info = "None"  
    
    output_data.append([gloss, present_count, "; ".join(present_lists), missing_list_info])

output_df = pd.DataFrame(output_data, columns=['CONCEPTICON GLOSS', 'FREQUENCY (MAX. 17)', 'PRESENT IN:', 'ABSENT IN:'])
output_path = os.path.join(folder_path, 'ConceptFrequency.tsv')
output_df.to_csv(output_path, sep='\t', index=False)

print(f"Your file has been saved to {output_path}")

