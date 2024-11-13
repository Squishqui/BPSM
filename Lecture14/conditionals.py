#!/usr/bin/python3

data = open("./data.csv")


for geneline in data:
    #splitting the line into a list of elements delimited by ","
    gene_info = geneline.split(",")
    #define each element in the list
    species = gene_info[0].lower()
    sequence = gene_info[1].upper()
    A_T_count = sequence.count("A") + sequence.count("T")
    seq_length = int(len(sequence))
    gene_name = gene_info[2].upper()
    expression = int(gene_info[3])
    #Al evaluated AT content in this section using
    #atcontent = (sequence.count('A')+sequence.count('T'))/seq_length
    #atstatus = low #this is the default value before the "if" functions
    #if (atcontent >=0.45 and atcontent <= 0.65):
        #atstatus = "medium"
    #if (atcontent>0.65):
        #atstatus = "high"
    #print(species, "has the sequence", sequence, "with gene name", gene_name)
    if "melanogaster" in species:
        print(gene_name, "is melanogaster")
    elif "simulans" in species:
        print(gene_name, "is simulans")
    #fail lines are included as a check to see that the code was working, they can be commented out once you are sure it is running correctly
    #else:
        #print("Question 1 (FAIL): "+ species + " " + gene_name)
    if seq_length >= 90 and seq_length <= 110:
        print(gene_name, "has between 90 and 110 bases")
    if ((A_T_count/seq_length) < 0.5) and expression > 200 :
        print(gene_name, "has less than 50% AT content and has an expression level of greater than 200")
    if (gene_name.startswith("K") or gene_name.startswith("H")) and "melanogaster" not in species:
        print(gene_name, "is not D melanogaster and starts with k or h")
    if ((A_T_count/seq_length) > 0.65):
        print(gene_name, "has a high AT content")
    elif ((A_T_count/seq_length) < 0.45):
        print(gene_name, "has a low AT content")
    else:
        print(gene_name, "has a medium AT conent")
