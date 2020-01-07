f = open("prov_names.txt", "w")
s = open("definition.csv", "r")
f.write("l_english:\n")
i = 0
for t in s:
	t = t.split(";")
	f.write(" PROV" + str(i) + ": \"" + t[4] + "\"\n")
	i = i + 1
f.close()