"""
This Python script accesses the previously created concept_frequency.py file and extracts concepts that appear in at least 15, 16, or all 17 out of 17 datasets, then prints them.
"""

from csvw.dsv import UnicodeDictReader
from pathlib import Path
from wordcloud import WordCloud
from matplotlib import pyplot as plt

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

word_frequencies = {
        row["CONCEPTICON_GLOSS"]: int(row["FREQUENCY"]) for row in data}



wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='Oranges').generate_from_frequencies(word_frequencies)

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig("wordcloud.pdf")
