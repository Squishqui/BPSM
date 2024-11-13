#!/usr/bin/python3

#our sequence
dna="ATGCGCGCGATATAGCAT"

#length of our sequence
len_dna=int(len(dna))

#what kmer size do we want to use?
possible_kmer_sizes = list(range(2,len_dna-1))
minimum_kmer = 3

k=2 # kmer size
n=2 # more than this number found
offset=1

#make list of all the possible starting positions for the first window
starting_positions = list(range(0,len_dna,offset))
created_segments = []
#print(starting_positions)

#separate sequence into kmers
for seg_start in starting_positions:
    if (seg_start+k)<len_dna+1:
        tempseq = dna[seg_start :seg_start+k].upper()
        created_segments = created_segments + [tempseq]
        print(tempseq)
        #print(created_segments)

#create set of non-redundant options that we need to search through for iterations
options = (set(created_segments))
#print(options)

for seq in options:
    count = created_segments.count(seq)
    if count > n:
        print(seq, "occurs ", count, "times")
