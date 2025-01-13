# Data and Code Accompanying the Study "Everybody Likes to Sleep: A Computer-Assisted Comparison of Object Naming Data from 30 Languages"

Data and code presented here accompany the following study:

>  Kučerová, Alžběta and List, Johann-Mattis (2025): Everybody Likes to Sleep: A Computer-Assisted Comparison of Object Naming Data from 30 Languages. Proceedings of the Global WordNet Conference 2025. 

## Installation

Download the Concepticon repository and checkout version 3.3.0. With Make and git installed, you can just type:

```
$ make download
```

Otherwise, using GIT, you can also directly type:

```
$ git clone https://github.com/concepticon/concepticon-data.git
$ cd concepticon-data
$ git checkout v3.3.0
```

To install the packages, type:

```
$ pip install -r requirements.txt
```

## Analysis

Concept counts can be done with the script `concept_frequency.py`:

```
$ python concept_frequency.py
```

Results will be written to file `concept-frequency.tsv`.

Then, type:

```
$ python swadesh_overlap.py
```

This will create output printed to the terminal and also create a barplot (`swadesh-barcharts.pdf`) and a heatmap (`swadesh-heatmap.pdf`).

To create the wordcloud shown in the study, type.

```
$ python recurring_concepts.py
```.

This will create the file `wordcloud.pdf`.

