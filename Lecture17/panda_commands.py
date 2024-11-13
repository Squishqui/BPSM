#!/usr/bin/python3
import os, sys, subprocess
import numpy as np
import pandas as pd

#create a dataframe of the data and index it with the organism names/accessions
df = pd.read_csv('eukaryotes.txt', sep="\t", na_values=['-'])
df.index=df.apply(lambda x: "{} ({})".format(x['#Organism/Name'],x['BioSample Accession']),axis=1)

#How many fungal species have genomes bigger than 100Mb?
big_fungi = df[(df['Group']=='Fungi')&(df['Size (Mb)']>100)]
print("There are", big_fungi.shape, "funal species with genomes larger than 100Mb")

#How many genomes of each major group (plants, animals, fungi, and protists) have been sequenced, and how many unique organisms?
for Group in ['Plants', 'Animals', 'Fungi', 'Protists']:
    count = len(df[df['Group'] == Group])
    count_unique = len(set(df[df['Group'] == Group]['#Organism/Name']))
    print("{} genomes for {} ({} unique)".format(count, Group, count_unique))

#Which Heliconius species genomes have been sequenced, and how many scaffolds is each assembly in?
hel = df[df.apply(lambda x : x['#Organism/Name'].startswith('Heliconius'), axis=1)]
hel[ ['#Organism/Name', 'Scaffolds'] ]
print(hel)

#Which center has sequenced the most plant genomes?
most_plants = df[df['Group'] == 'Plants']['Center'].value_counts().head(1)
print(most_plants,"has sequenced the most plant genomes")

#Which center has sequenced the most insect genomes?
most_insects = df[df['SubGroup'] == 'Insects']['Center'].value_counts().head(1)
print(most_insects,"has sequenced the most insect genomes")

#Add a column giving the number of proteins per gene
df['Proteins per gene'] = df['Proteins']/df['Genes']
print(df[df['Proteins per gene']>=1.1][['#Organism/Name','Group','Proteins per gene']].head())
