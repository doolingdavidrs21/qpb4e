#!/usr/bin/env bash
set -u
echo "Hello $1, from $0"

echo "You can list numbers and text like this:"

for n in 1 2 3 four
do
   echo "Number $n"
done

for n in {1..5}
do
    echo "Number $n"
done

echo "Or use the output of another command:"
for f in $(ls)
do
    echo $f
done