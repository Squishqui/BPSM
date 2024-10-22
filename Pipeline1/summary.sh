#!/usr/bin/bash

# Ask for the directory with all the fastqc data 
echo "Hello, where are the fast1c.zip folders stored?"
read directory
echo "Reading data in ${directory}"
output_file="${directory}/qcsummary.txt"
> qcsummary.txt

# Change to the directory
cd "${directory}" || { echo "Failed to access ${directory}"; exit 1; }

for folder in *_fastqc
do
	echo "Processing ${folder}"
	#unzip ${folder}
	folder_name="${folder}"
	cd ${folder_name} || { echo "Failed to enter ${folder_name}"; exit 1; }
	count=$(awk 'BEGIN{FS="\t"; fail=0}
	($1 == "FAIL") {fail++} END {print fail}' summary.txt)
	if [[ ${count} -ge 2 ]]; then
		echo "${folder} failed the QC test" >> "$output_file"
	else
		echo "${folder} passed the QC test" >> "$output_file"
	fi
cd ..
done
