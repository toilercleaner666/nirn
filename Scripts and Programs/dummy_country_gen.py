# Author - Sol_InvictusXLII
#
# Script purpose: use country_tags.txt file to generate dummy files for missing countries in common and history
# Files are generated in out/dummy_countries

import os
import re

# Edit these if you have a different directory structure
histdir = "../NirnUniversalis/history/countries/"
ctdir = "../NirnUniversalis/common/country_tags/"
ccdir = "../NirnUniversalis/common/countries/"
ctfile = "nirn_tags.txt"

# Excluded countries and tags. Edit this if you need dummies for the below tags, or if you want to manually exclude any other tags
hexc = ["REBELS", "PIRATES", "NATIVES"]		# excluded country names
cexc = ["REB", "PIR", "NAT"]				# excluded country tags

# Check if files are correct in script
if not os.path.exists(histdir):
	print("History files cant be found. Please change the directory in the script to suit your filestructure")
	exit()
if not os.path.exists(ctdir):
	print("Country tags files cant be found. Please change the directory in the script to suit your filestructure")
	exit()
if not os.path.exists(ccdir):
	print("Country files cant be found. Please change the directory in the script to suit your filestructure")
	exit()
if not os.path.exists(ctdir + ctfile):
	print("Country tags file has incorrect name or cant be found. Please change the filename in the script to suit your filestructure")
	exit()

# Create /out and subdirs
if not os.path.exists("out/dummy_countries/history/countries"):
	os.makedirs("out/dummy_countries/history/countries")
if not os.path.exists("out/dummy_countries/common/countries"):
	os.makedirs("out/dummy_countries/common/countries")

# Directory lists -> files that already exist
hlist = [item[0:3].upper() for item in os.listdir(path=histdir)]
clist = [item.replace(".txt", "").upper() for item in os.listdir(path=ccdir)]

# Build dummy files
with open(ctdir + ctfile) as ct_file:
	for line in ct_file.readlines():
		if re.match("[A-Za-z][A-Za-z][A-Za-z]\s*=\s*\"", line):
			# Extract TAG, countryname into sp[0], sp[1]
			sp = re.split("\s*=\s*\"countries/", line)
			sp[1] = sp[1].split(".txt")[0]
			sp[0] = sp[0].upper()

			# Missing history/countries file -> generate dummy at "{TAG} - {Country}.txt"
			if sp[0] not in hlist and sp[0] not in cexc:
				hist_dummy = f"# {sp[0]} - {sp[1]}\n\ngovernment = monarchy\ngovernment_rank = 1\nmercantilism = 0.0\nprimary_culture = heartlander\nadd_government_reform = feudalism_reform\nreligion = eight_divines_rel\ntechnology_group = western\ncapital = 1"
				fname = f"{sp[0]} - {sp[1]}.txt"
				with open("out/dummy_countries/history/countries/" + fname, "w+") as f:
					f.write(hist_dummy)
			
			# Missing common/countries file -> generate dummy at "{Country}.txt"
			if sp[1].upper() not in clist and sp[1].upper() not in hexc:
				country_dummy = f"#Country Name: {sp[1]} ({sp[0]})" + "\n\ngraphical_culture = westerngfx\ncolor = { 93  160  163 }\n\nhistorical_idea_groups = { }\nhistorical_units = { }\nmonarch_names = { PLACEHOLDER }\nleader_names = { PLACEHOLDER }\nship_names = { PLACEHOLDER }\narmy_names = { PLACEHOLDER }"
				fname = f"{sp[1]}.txt"
				with open("out/dummy_countries/common/countries/" + fname, "w+") as f:
					f.write(country_dummy)

print("\n--------------------------------------------------------\n| Files generated in \"/out/dummy_countries/\"           |\n| Please check the files before copying them over      |\n| When ready, copy the history, common folders to root |\n| If it asks to replace any files, select no           |\n| (Tell Sol if it does, that's a bug)                  |\n--------------------------------------------------------")