# Author - Sol_InvictusXLII
#
# Script purpose: Generate prov_names_l_english.yml file
# This is the localization file for province names, and is how provinces are named in game
# 
# Using the file:
# 1. Run the file with python command
# 2. The output file will be generated in /out directory
# 3. Save the file in UTF-8 BOM encoding
# 4. Copy the file from /out and place it in the correct directory (this is not done by the script so you can check that the output is correct)
#
# If the file does not work and provinces revert to base game names, you did not save it in the correct encoding.

import os
from tkinter import messagebox

# Open definition to read from
f = open("../NirnUniversalis/map/definition.csv", "r")

# Split the csv along semicolons
prov = [g.split(';') for g in f.readlines()]

# Initialize the output content
output = "l_english:\n"

# Build the output in .yml format
for line in prov[1:]:
	output += " PROV" + line[0] + ": \"" + line[4] + "\"\n"

# Create the out directory if it doesnt exist
if not os.path.exists('out'):
	os.makedirs('out')

# Write the output to file
f = open("out/prov_names_l_english.yml", "w")
f.write(output)

messagebox.showinfo("Alert", "File generated in /out.\nRemember to change the file encoding to UTF-8 BOM")