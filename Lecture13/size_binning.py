#!/usr/bin/python3
import os, shutil, subprocess

folder_path = "/localdisk/home/s2760053/Lecture13"
bin_sizes = list(range(100,1000,100))
print(bin_sizes)
for item in bin_sizes:
    item2=int(item)+99
    dir_name = str(item)+"_"+str(item2)+"_binsize"
    #print(dir_name)
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

sequence_number = 0
dna_sequences = open("xac.dna")
#print(dna_sequences)
for eachline in dna_sequences.readlines():
    dna = eachline.rstrip('/n')
    length = len(dna)
    print("Found a DNA sequence with length",length)
    for bin_lower in bin_sizes:
        bin_upper = bin_lower+99
        if length >= bin_lower and length<= bin_upper:
            print("bin is "+ str(bin_lower)+" to "+str(bin_upper))
            output_path = str(bin_lower)+"_"+str(bin_upper)+"_binsize"+"/"+str(sequence_number)+".dna"
            output = open(output_path,"w")
            output.write(dna)
            output.close()
            sequence_number +=1

