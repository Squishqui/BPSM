#!/usr/bin/python3
#Sequence contains 2 exons with an intron in between
sequence = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

#take the coordinates from question 4 and extract the exons
exon1 = sequence[0:63]
intron = sequence[63:90]
exon2 = sequence[90:len(sequence)]

#combine the exons together into the coding sequence alone
coding = exon1 + exon2

#work out the percentage of the original sequence that is coding
coding_percentage = (len(coding)/len(sequence)) *100
print("The coding sequence makes up", str(int(coding_percentage)), "% (rounded) of the original sequence")

#convert intron to lowercase
intron_lower = intron.lower()

#combine the 3 sequences and print
new_sequence = exon1 + intron_lower + exon2
print(new_sequence)
