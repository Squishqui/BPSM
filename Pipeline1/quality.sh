#!/usr/bin/bash

#Ask for the directory with all the data in
echo "Hello, where are the fq.gz files stored?"
read directory
echo "reading data in ${directory}"
cd ${directory} || { echo "Failed to access ${directory}"; exit 1; }

#list the files in the directory
files_list=$(ls ${directory})

#run fastqc on all files in the current folder
for file in *fq.gz
do
	echo "Processing $file"
	gunzip $file
	fastqc -o "${directory}" -t 5 "${file%.gz}"
done

