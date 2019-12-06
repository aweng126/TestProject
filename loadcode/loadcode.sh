#!/bin/bash

FOLD="codes/"

cat "$1" | while read line
do
    name=$(echo $line | awk '{print $1}');
    codeurl=$(echo $line | awk '{print $2}')
    # echo $codeurl

    if [ ! -d "$FOLD$name" ]; then
        mkdir $FOLD$name
        echo "build success"
    fi
    # echo $FOLD$name
    git clone  $codeurl  $FOLD$name 
done
