#!/usr/bin/python

#dictionary to convert codons into amino acids
gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

#Sequence of interest
sequence = "ATGTTCGGTCTCGAGACTTAGGCTC"

#split the sequence into open reading frames, starting at the 1st, 2nd, and 3rd base
def frames(sequence):
    len_sequence = len(sequence)
    window1 = list(range(0,len_sequence,3))
    window2 = list(range(1,len_sequence,3))
    window3 = list(range(2,len_sequence,3))
    return window1,window2,window3

#convert sequences into amino acids
def convert(sequence,start_positions):
    orf = []
    for item in start_positions:
        temp_seq = sequence[item:item+3]
        if len(temp_seq) == 3: #ensure only complete codons are processed
            orf.append(temp_seq)

    print("The codons in this ORF are",orf)

    aminoacids = []
    keys = gencode.keys()
    for codon in orf:
        if codon in keys:
            value = gencode[codon]
            aminoacids.append(value)
    #print(aminoacids)
    return aminoacids

#create reverse complement of the sequence
def reverse(seq):
    reverse = seq[::-1]
    v1 = reverse.replace("A","t")
    v2 = v1.replace("T","a")
    v3 = v2.replace("C","g")
    v4 = v3.replace("G","c")
    final = v4.upper()
    return final

#these 3 open reading frames are given as 3 lists of starting values
win1, win2, win3 = frames(sequence)

#give amino acid sequence for each open reading frame
orf1 = convert(sequence,win1)
print("Open reading frame 1 has the amino acid sequence: " + " ".join(orf1))

orf2 = convert(sequence,win2)
print("Open reading frame 2 has the amino acid sequence: " + " ".join(orf2))

orf3 = convert(sequence,win3)
print("Open reading frame 3 has the amino acid sequence: " + " ".join(orf3))

#give reverse complement sequence
rev_seq = reverse(sequence)
print("The reverse complement of the sequence is", rev_seq)

#find open reading frames for the reverse sequence
win4, win5, win6 = frames(rev_seq)

#give amino acid sequence for each of the reverse open reading frames
orf4 = convert(rev_seq,win4)
print("Open reading frame 4 has the amino acid sequence: " + " ".join(orf4))

orf5 = convert(rev_seq,win5)
print("Open reading frame 5 has the amino acid sequence: " + " ".join(orf5))

orf6 = convert(rev_seq,win6)
print("Open reading frame 6 has the amino acid sequence: " + " ".join(orf6))

