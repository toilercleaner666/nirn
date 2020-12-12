#!/bin/sh
for i in {1..4272}
do
	cat ${i}-${i}.txt
	cat TEMPLATE.txt > ${i}-${i}.txt
done
#for i in {1..4272}
#do
#	sed -i "s/ - /${i}-${i}/" ${i}-${i}.txt
#done
