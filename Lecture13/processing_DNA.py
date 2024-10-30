#!/usr/bin/python3

#convert file into a list
#with open('/localdisk/home/s2760053/Exercises/Lecture13/input.txt') as f:
#    lines = f.read().splitlines()
#    for e in lines :
#        cleaned_lines = {e}.replace('ATTCGATTATAAGC','')
#        print(cleaned_lines)

#open a file for writing clean sequences into
clean_seq = open('clean_sequences.txt','w+')

#open input.txt and replace first 14 bases with nothing
dna_seq = open('input.txt').read().replace('ATTCGATTATAAGC','').split()

#Iterate through the DNA sequences and insert clean sequences into the file
for cleans in dna_seq:
    clean_seq.write(cleans + '\n')
    print(len(cleans))

#remove the first 14 base pairs if they are the same as the sequence given

#for eachline in input.txt :
#    if {eachline}.startswith('ATTCGATTATAAGC'):

