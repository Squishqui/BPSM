#!/usr/bin/python3
import os, sys
import numpy as np
import matplotlib.pyplot as plt

#open the file, remove all new line syntax, put bases in upper case
ecoli = open("ecoli.txt").read().replace('\n', '').upper()

#what is the total length of the genome?
length = len(ecoli)

#what window size are we using?
window = 1000

#What are the regions we are testing?
regions=[50000,100000,length]

for region in regions:
    print("processing the region from 0 to", region)
    at = [] # initiate the list
    for start in range(region-window):
        win = ecoli[start:start+window]
        at.append((win.count('A')+win.count('T'))/window)
    #plot the list
    plt.figure(figsize=(20,10))
    plt.plot(at, label="AT content", linewidth=3,color="purple")
    plt.ylabel('Fraction of bases')
    plt.xlabel('Position on genome')
    plt.title("AT content, 1kb windows of the E.coli genome")
    plt.legend()
    plt.savefig("Chart_Exercise_1_"+str(region)+".png",transparent=True)
    plt.show()
