"""
This Python script generates a .tsv file that lists concept sets from our concept lists. For each concept, the script records the number of datasets where the concept appears and identifies the datasets where the concept is missing.
"""

from pathlib import Path

from pyconcepticon import Concepticon
from csvw.dsv import UnicodeWriter

from collections import defaultdict

# list of concepts to be queried
conceptlists = [
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

concepticon = Concepticon("concepticon-data") # stores the data

# Initialize a defaultdict to hold the gloss data
gloss_data = defaultdict(list)

# Populate gloss_data with counts
for conceptlist in conceptlists:
    cl = concepticon.conceptlists[conceptlist]
    for concept in cl.concepts.values():
        if concept.concepticon_gloss:
            gloss_data[concept.concepticon_gloss].append(conceptlist)

# Create a set of all lists for checking missing concepts
all_lists = set(conceptlists)
output_data = []

# For each gloss, determine which lists it's present in and which it’s missing from:
for gloss, values in gloss_data.items():
    present_lists = set(values)  # Lists where present
    present_count = len(present_lists)       # Frequency
    missing_lists = all_lists - present_lists # Lists where absent
    
    if present_count < len(all_lists):  # Only include missing lists if not all are present
        missing_list_info = "; ".join(sorted(missing_lists)) 
    else:
        missing_list_info = "None"  
    
    output_data.append([gloss, present_count, "; ".join(sorted(present_lists)), missing_list_info])

path = Path(__file__).parent / "concept-frequency.tsv"

with UnicodeWriter(path, delimiter='\t') as writer:
    writer.writerow(['CONCEPTICON_GLOSS', 'FREQUENCY', 'PRESENT', 'ABSENT'])
    for row in sorted(output_data, key=lambda x: x[1], reverse=True):
        writer.writerow(row)

print("Data have been written to file {0}.".format(path))

