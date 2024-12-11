#!/usr/bin/python3
search_results = []

def get_average_length(taxonomy, gene, howmany=10): #define our function with a default value for howmany
    from Bio import Entrez, SeqIO #import the processes we need
    import os, subprocess
    Entrez.email = "e.g.cragg@sms.ed.ac.uk"
    Entrez_api_key = "5150280144c8068543fe3ccb82f021fa1c08"
    search_term = taxonomy + " " + gene + " complete" #define search term
    search_output = open(search_term.replace(" ","_")+"_outputs.txt","w")
    mysearch = Entrez.esearch(db="protein", term=search_term, retmax=howmany)
    result = Entrez.read(mysearch)
    loopcounter = total_length = 0
    #extract info from the results
    for accession in result["IdList"]:
        loopcounter += 1
        gb_file = Entrez.efetch(db="protein",id=accession,rettype="gb")
        record = SeqIO.read(gb_file, "genbank")
        total_length = total_length +len(record.seq)
        search_results.append([[search_term,record.id,record.description,len(record.seq),record.seq]])
        print(record.id+"\t"+record.description+"\t"+str(len(record.seq))+"\t"+record.seq[0:50]+"...")
        search_output.write(record.id+"\t"+record.description+"\t"+str(len(record.seq))+"\t"+str(record.seq)+"\n")
    mean_length = int(total_length/loopcounter)
    return print(("\nThe mean length was "+str(mean_length)+" amino acids.\n"))
    close(search_output)

get_average_length("Arthropoda","ATP6")
