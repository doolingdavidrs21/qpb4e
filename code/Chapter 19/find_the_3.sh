#!/usr/bin/env bash
for i in {1..10}
do
    if test $i -eq 3
    then
        echo "I found the 3!"
    else
        echo "Not looking for the $i"
    fi
done
