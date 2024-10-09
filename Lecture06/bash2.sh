cut -d$'\t' -f 2,3,4,5 blastoutput2.out |
       	sort -n -t$'\t' -k4,4 |
       	awk 'BEGIN{FS="\t"}{if($4 >= 20 && $3 <= 100){print $0}}'
