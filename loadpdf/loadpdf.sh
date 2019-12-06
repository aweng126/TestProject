#!/bin/bash
#  download pdf file by this shell script, all the file will download to files/ 
#  paper1206.txt row format like this id title link
#  "$1" is the paramater from the shell.  execute this file can by this way
#  ./loadpdf paper1206.txt
cat "$1" | while read line
do
    id=$(echo $line | awk '{print $1}');
    title=$(echo $line | awk '{print $2}');
    pdfurl=$(echo $line | awk '{print $3}');

    curl  -o files/"$title".pdf "$pdfurl"
    # echo $line
done 