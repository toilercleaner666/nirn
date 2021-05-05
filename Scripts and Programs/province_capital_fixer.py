# Author - Sol_InvictusXLII
#
# Script purpose: Use a csv to extract trade good information to the history/provinces files, while
# 	Keeping the old information in those files the same
# 
# Using the file:
# First, you will need a csv. This has columns in the following order:
#	0. Province ID
#	1. Province Name
#	2. Trade Good
# This .csv should also have a header row (important, otherwise the first row is skipped).
# You can copy-paste the first 2 columns from definition.csv. Look at /data/ValenwoodDevReligion.csv for an example
# Now, make a backup of your history/provinces directory.
# After creating the .csv file, place it in /data and run the script. Input the csv file name when prompted, next
# 	input the directory name in /out that you want to save it to (use a unique name)
# It will generate the new files in /out/... , and delete the old files in history/provinces
# Simply copy and paste the new files over.

import os
import argparse
from tkinter import messagebox

histdir = "../NirnUniversalis/history/provinces"
# Backup reminder alert
messagebox.showinfo("Alert", "Please make a backup of history/provinces before running this script. Dont scream at Sol if the script bugs and you forgot to do this. Especially make sure to do this if you edited the script in any way.")

infile = open("../NirnUniversalis/map/definition.csv")
provinces = [l.split(';') for l in infile.readlines()]

# Output
print("Enter the directory name to save the files in (in /out)")
direct = input()

# Create /out if it doesnt exist locally
if not os.path.exists('out'):
	os.makedirs('out')

# Create a folder for your new directory
if not os.path.exists('out/' + direct):
	os.makedirs('out/' + direct)

# 0: number, 1: name, 2: trade giid
# Add any other province based items (culture, trade goods, etc) that you wish to add to the script in the csv
# Make sure to set up input flags if you want to edit these in.

# Iterate over every province in the csv
for prov in provinces[1:]:
	# Old and new province file names
	infilename = histdir + "/" + prov[0] + "-" + prov[0] + ".txt"
	outfilename = "out/" + direct + "/" + prov[0] + "-" + prov[4] + ".txt"

	# Old province file object (initialized to empty string, this will get replaced and wont cause errors)
	pfile = ""
	try:
		pfile = open(infilename, "r")
	except:
		# If it isnt of form XXX-XXX.txt, try XXX-something.txt
		dirls = [f for f in os.listdir(histdir) if f.startswith(prov[0] + "-")]
		if len(dirls) == 1:
			infilename = histdir + "/" + dirls[0]
			pfile = open(infilename, "r")
		else:
			# If neither file name works, skip it and print and error
			print("something wrong with file for province number " + prov[0])
			continue

	# List of lines for old and new files
	oldlines = pfile.readlines()
	newlines = []

	for line in oldlines:
		if line.startswith("capital = "):
			# Set capital name to province name.
			# It will be very rare that the 2 are different.
			newlines.append("capital = \"" + prov[4] + "\"")

		else:
			newlines.append(line)

	# Write to output file
	with open(outfilename, "w") as outfile:
		outfile.write(''.join(newlines))
	pfile.close()
	os.remove(infilename)

#Alert
messagebox.showinfo("Alert", "File generated in /out/" + direct + ".\nThe old files have been deleted already, just move the new files over")