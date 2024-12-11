#!/usr/bin/python3
search_results = []

def get_average_length2(taxonomy, gene, startat=0,howmany=100):
    from Bio import Entrez, SeqIO
    Entrez.email = "e.g.cragg@sms.ed.ac.uk"
    Entrez.api_key= "5150280144c8068543fe3ccb82f021fa1c08"
    search_term = taxonomy + " " + gene + " complete"
    search_output = open(search_term.replace(" ","_")+"_outputs.txt","w")
    mysearch = Entrez.esearch(db="protein", term=search_term, retstart = startat, retmax=howmany)
    result = Entrez.read(mysearch)
    print("Search done,", result['Count'],"found, starting retrieval of",howmany,"starting at",startat)
    loopcounter = poorseqs = total_length = 0
    for accession in result['IdList']:
      loopcounter += 1
      genbank = Entrez.efetch(db="protein",id=accession,rettype="gb")
      print('\r' + 'Retrieving sequence ' + str(loopcounter+startat), end="")
      record = SeqIO.read(genbank, "genbank")
      Xaa = str(record.seq).count("X")
      if Xaa > 5 :
         print(" Seq",loopcounter+startat,"contains",Xaa,"unknown amino acids:",int(100*Xaa/len(record.seq)), "percent of total!")
         poorseqs += 1
      else :
         total_length =  total_length + len(record.seq)
         search_results.append([search_term,record.id,record.description,len(record.seq),record.seq])
         # print(record.id+"\t"+record.description+"\t"+str(len(record.seq))+"\t"+record.seq[0:50]+"...")
         search_output.write(record.id+"\t"+record.description+"\t"+str(len(record.seq))+"\t"+str(record.seq)+"\n")
    goodseqs=loopcounter-poorseqs
    mean_length = int(total_length/goodseqs)
    return print(("\nThe mean length of the "+str(goodseqs)+" high quality seqs was "+str(mean_length)+" amino acids.\n"))
    close(search_output)

get_average_length2("Box taurus","cytochrome c oxidase subunit I (mitochondrion)",1,3000)
