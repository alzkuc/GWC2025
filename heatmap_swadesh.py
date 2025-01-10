import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

base_directory = 'PATH/TO/conceptlists'
common_concepts_dict = {}
for file_name in file_paths:
    
    df = pd.read_csv(base_directory + file_name, sep='\t')
    
    dataset_concepts = df['CONCEPTICON_GLOSS'].tolist()
    
    common_concepts = set(swadeshnouns) & set(dataset_concepts)
    
    common_concepts_dict[file_name] = sorted(common_concepts)

heatmap_data = pd.DataFrame(0, index=file_paths, columns=swadeshnouns)
for dataset, nouns in common_concepts_dict.items():
    for noun in nouns:
        heatmap_data.at[dataset, noun] = 1

from matplotlib.colors import ListedColormap
plt.figure(figsize=(15, 9)) 
cmap = ListedColormap(['#fca663', '#de5b12'])
heatmap = sns.heatmap(heatmap_data, cmap=cmap, cbar=True, linewidths=0.5, vmin=0.0, vmax=1.0, square=True,  cbar_kws={"orientation": "vertical", "shrink": 0.25})
colorbar = heatmap.collections[0].colorbar
colorbar.set_ticks([0, 1])
colorbar.set_ticklabels(['Absent', 'Present']) 

print((len)(swadeshnouns))
plt.title('')
plt.xlabel('')
plt.ylabel('')

plt.tight_layout()
plt.show()

