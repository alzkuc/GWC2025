#This Python script accesses the previously created concept_frequency.py file and extracts concepts that appear in at least 15, 16, or all 17 out of 17 datasets, then prints them.import pandas as pd 

from csvw.dsv import UnicodeDictReader
from pathlib import Path

def get_list(data, freq):
    return [row["CONCEPTICON_GLOSS"] for row in data if int(row["FREQUENCY"]) >= freq]

with UnicodeDictReader(Path(__file__).parent / "concept-frequency.tsv",
                       delimiter="\t") as reader:
    data = [row for row in reader]

list_15 = get_list(data, 15)
list_16 = get_list(data, 16)
list_17 = get_list(data, 17)

for a, b in zip([15, 16, 17], [list_15, list_16, list_17]):
    print("# {0} lists ({1} concepts".format(a, len(b)))
    for c in b:
        print("* " + c)
    print("")

