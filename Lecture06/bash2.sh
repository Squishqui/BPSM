#!/usr/bin/bash
# clear the outputs from the last run of this script
rm -f *.exercise.out
# state your variables and reset variables and counters from the last run
# remove the headers which tell you the what each tab delimited field is
inputfile=/home/s2760053/Exercises/Lecture06/blastoutput2.out
goodlines=$(grep -o '^[^#]*' ${inputfile} | wc -l | cut -d ' ' -f1)
unset IFS
unset dataline
shortHSP=0;
hspcounter=0;
# we may receive multiple lines of code form a BLASTs
echo -e "We have ${goodlines} data lines for processing"
# initialise a bash array for multiple HSPs
dupS_acc=()
# choose how you want to sort the HSP scores
group1cut=150
group2cut=250
group3cut=351
outfile1="HSPscore.${group1cut}.exercise.out"
outfile2="HSPscore.${group2cut}.exercise.out"
outfile3="HSPscore.${group3cut}.exercise.out"
outfile4="HSPscore.morethan.${group3cut},exercise.out"
# remove any existing versions of those out files, using rm does not remove the variables
# we would need to use unset to remove the variables
rm -f ${outfile1}${outfile2}${outfile3}${outfile4}
#read the whole line as a variable
while IFS=$'\t' read -r  wholeline;
do
       # echo "Line is "$wholeline""
#  if the first character of the whole line one does not equal #
  if test ${wholeline:0:1} != "#"
  then
          dataline=$((dataline+1))
	  echo -e "line is ${dataline}"
         #split the lines into the fields that we want
         # here we are splitting wholeline into the fields that we want!
         read Q_acc S_acc pc_identity alignment_length mismatches gap_opens Q_start Q_end S_start S_end evalue bitscore <<< ${wholeline}
         bitscore=$(printf "%.0f\n" "$bitscore")
	 # send the subject accessions for all HSPs to a file
         echo -e "${dataline}\t${Q_acc}\t${S_acc}" >> Subject_accessions.exercise.out
	 # send the alignment lengths and percent ID for all HSPs to a file
         echo -e "${dataline}\t${alignment_length}\t${pc_identity}" >> al_leng_pcID.exercise.out
	 # show the HSPs with more than 20 mismatches (-gt means greater than)
	 #if [ "$mismatches" -gt 20 ] && [ "$alignment_length" -lt 100 ]
         #then
         #      echo -e "${dataline}\thas more than 20 mismatches:\t ${mismatches} \n \
		#	and is shorter than 100 amino acids ${alignment_length}"
         #fi
	 #show the first 20 HSPs that have fewer than 20 mismatches
	 #if (( mismatches < 20))
	 #then
	#	 hspcounter=$((hspcounter+1))
	#	 if (( hspcounter <= 20 ))
	#	 then
	#		 hsp_array+=("$wholeline}")
	#		 echo -e "${dataline}\t${wholeline}" >> Fewer_than_20.exercise.out
	#	 fi
	# fi
	# List the top 10 highest HSPs
	#if (( dataline <= 10 ))
	#then
	#	echo -e "${dataline}\t${wholeline}" >> Top10.HSPs.exercise.out
	#fi
	#if [[ ${S_acc} == *"AEI"* ]];
	#then
	#	echo -e "${dataline}\t${S_acc} contains AEI: \n \
	#		Subject starts at ${S_start},\n \
	#	       	Query starts at ${Q_start}" >> AEIinSubAcc.starts.exercise.out
	#fi
	if test ${S_acc} == ${pre_acc}  
 	then
 		dupecount=$((dupecount+1))
 		if [[ dupecount -eq 1 ]]; then
 		dupS_acc=${S_acc}
 		fi
 		if [[ $dupS_acc == *${S_acc}* ]]; then
 			echo -e "${dataline} has $dupecount repeats"
  		else
  			dupS_acc="${dupS_acc} ${S_acc}"
 		fi
	fi
	pre_acc=${S_acc}
  fi
done < ${inputfile}
