"""
This Python script calculates and presents the overlap of concepts within the 17 datasets with Swadesh 1955. 
Note: For this script, one must first download and save the Swadesh_POStagged.tsv file (Under: Additional Data).
"""

from pyconcepticon import Concepticon

concepticon = Concepticon("concepticon-data")

swadesh = concepticon.conceptlists["Swadesh-1952-200"].concepts
nouns = []
for concept in swadesh.values():
    if concepticon.conceptsets[concept.concepticon_id].ontological_category == "Person/Thing":
        nouns += [concept.concepticon_gloss]

#Specific comparison: which Swadesh concepts and how many are present in which dataset
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

common_concepts = {}

for conceptlist in conceptlists:
    concepts = [concept.concepticon_gloss for concept in
                concepticon.conceptlists[conceptlist].concepts.values() if
                concept.concepticon_gloss in nouns]
    common_concepts[conceptlist] = sorted(concepts)

for cl, concepts in common_concepts.items():
    print('# Conceptlist {0} has {1} common concepts'.format(cl, len(concepts)))
    for concept in concepts:
        print('* ' + concept)
    print("")
