#!/usr/bin/python3
import re

#accessions list:
accessions = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']

#create dictionary of each of the search keys with blank values
output_dict = {
        "contains the number 5:": [],
        "contains d or e:": [],
        "contains de:": [],
        "contains d something e:": [],
        "contains d and e:": [],
        "starts with x or y:": [],
        "starts with x or y and ends with e:": [],
        "contains 3 numbers in any order:": [],
        "contains 3 different numbers:": [],
        "contains 3 or more numbers in a row:": [],
        "ends with d, followed by a, r, or p:": []
        }

#for each accession, run each search and add them to the correct dictionary key
for acc in accessions:
    if re.search(r'5', acc):
        output_dict["contains the number 5:"].append(acc)
    if re.search(r'd|e', acc): #| means or
        output_dict["contains d or e:"].append(acc)
    if re.search(r'de',acc):
        output_dict["contains de:"].append(acc)
    if re.search(r'd.*e', acc): #. means something, * means any number of somethings
        output_dict["contains d something e:"].append(acc)
    if re.search(r'd', acc) and re.search(r'e', acc):
        output_dict["contains d and e:"].append(acc)
    if re.search(r'^[xy]', acc): #^ for starts with, [xy] for either x or y
        output_dict["starts with x or y:"].append(acc)
    if re.search(r'^[xy]', acc) and re.search(r'e$', acc): #$ for ends with
        output_dict["starts with x or y and ends with e:"].append(acc)
    if len(re.findall(r'\d',acc))==3:
        output_dict["contains 3 numbers in any order:"].append(acc)
    #find all numbers in the accession and put them in a non-redundant list
    numbers = set(re.findall(r'[1234567890]', acc))
    #if the length of that list is 3 or more, add acc to the dictionary
    if len(numbers) >= 3:
        output_dict["contains 3 different numbers:"].append(acc)
    if re.search(r'[1234567890]{3,}',acc): #{3,} 3 or more instances
        output_dict["contains 3 or more numbers in a row:"].append(acc)
    if re.search(r'd[arp]$', acc):
        output_dict["ends with d, followed by a, r, or p:"].append(acc)

for keys,values in output_dict.items():
    print(keys)
    print(values)
