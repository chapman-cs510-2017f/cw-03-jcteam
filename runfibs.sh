#Cynthia Parks, Julie Gardner-Hoag
#2303535, 2299636
#cparks@chapman.edu, gardnerh@chapman.edu
#CS 510 Computing for Scientists
#CW 3


#!bin/bash

#checking for backup file
if [-f fibs.csv.bak]
   	then
	echo "Backup already exists."
	exit 1	     
fi

if [-f fibs.csv]
	then
	mv fibs.csv fibs.csv.bak
	echo "Created a backup file"
fi

for i in {1...10000}
	do
	touch "fibs.csv"
	echo -n "$(./fib.py $i)," >> fibs.csv
done
