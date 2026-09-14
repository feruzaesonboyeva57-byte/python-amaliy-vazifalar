#!/bin/bash
# Bingo Number Generator
echo -e "\n~~ Bingo Number Generator ~~\n"
NUMBER=$(( RANDOM % 75 + 1 ))
if [[ $NUMBER -le 15 ]]
then
  echo "The next number is B:$NUMBER"
elif [[ $NUMBER -le 30 ]]
then
  echo "The next number is I:$NUMBER"
elif [[ $NUMBER -le 45 ]]
then
  echo "The next number is N:$NUMBER"
elif [[ $NUMBER -le 60 ]]
then
  echo "The next number is G:$NUMBER"
else
  echo "The next number is O:$NUMBER"
fi
