#!/usr/bin/python3
count=0

#open the file and read them into variables
genomic_dna = open('genomic_dna2.txt').read().upper()
len_dna = len(genomic_dna)
exons = open('exons.txt').read().rsplit()
#print(genomic_dna, exons)
#print(exons)

#create and open coding_sequences.fasta and call it coding
with open('coding_sequences.fasta','w+') as coding:
    coding.write('>Lecture13_exercise2_codingseq\n') #header for info on the file
    for exon in exons : #for each line in exons (which is one sequence per line)
        count += 1
        startexon = int(exon.split(',')[0])-1 #split the line by comma, and have start exon be the first number
        endexon = int(exon.split(',')[1]) #split the line by comma, and have end exon be the last number
        exonwanted = genomic_dna[startexon :endexon] #splice the sequence
        coding.write(exonwanted) #write this coding sequence into our file
        regionsummary = 'Exon'+str(count)+' '+str(exon)+' runs from index position '+str(startexon)+' upto but not including '+str(endexon)+ '.' #add a summary for the coding sequence
        print(regionsummary,'\n\t',exonwanted) #print details to the screen
