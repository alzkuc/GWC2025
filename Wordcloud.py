#This Python script generates a word cloud from words appearing in 15, 16, and all 17 of the tested datasets, with sizes corresponding to their frequency.
#Note: This script makes use of the file ConceptFrequency.tsv - this can either be downloaded from the same repository, or generated using previous scripts.

import pandas as pd 
file_path = 'PATH/TO/ConceptFrequency.tsv'
try: 
    df = pd.read_csv (file_path, sep='\t')
    filtered_df = df[df['list_count'] >= 15]
    glossandcount = filtered_df['concepticon_gloss'].tolist()
    print(glossandcount)
    print((len)(glossandcount))
except Exception as e:
    print('error processing: {e}')


concepts_15lists=set(df[df['FREQUENCY (MAX. 17)'] >= 15]['CONCEPTICON GLOSS'].tolist())
concepts_16lists=set(df[df['FREQUENCY (MAX. 17)'] >= 16]['CONCEPTICON GLOSS'].tolist())
concepts_17lists=set(df[df['FREQUENCY (MAX. 17)'] == 17]['CONCEPTICON GLOSS'].tolist())
print(concepts_15lists)
print(concepts_16lists)
print(concepts_17lists)

from wordcloud import WordCloud
import matplotlib.pyplot as plt

word_frequencies = {
    "NOSE": 1, "SOCK": 1, "ANT": 2, "PEAR": 1, "SNAIL": 2, "RHINOCEROS": 2, "BALL": 1, "SPECTACLES": 1,
    "POT": 1, "OWL": 1, "SQUIRREL": 1, "HORSE": 1, "FLAG": 1, "DUCK": 1, "GUITAR": 1, "APPLE": 2,
    "AIRPLANE": 2, "COW": 1, "GLOVE": 1, "CAT": 1, "SHEARS": 1, "LION": 1, "TURTLE": 1, "TIGER": 1,
    "TREE": 1, "BED": 3, "SPIDER": 1, "EAR": 1, "SAW": 2, "TABLE": 2, "MOUNTAIN": 1, "BANANA": 1,
    "TRAIN": 1, "GRAPE": 1, "ELEPHANT": 1, "CAMEL": 2, "HAMMER": 1, "BUTTERFLY": 2, "EYE": 1,
    "FINGER": 1, "HOUSE": 2, "GUN": 1
}

wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='Oranges').generate_from_frequencies(word_frequencies)

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
