# Initial 

import glob
import os
allpies = glob.glob("*.py")

for py in allpies:
	thepie = open(py, "r")
	rottenpie = open("%s.rotten" % py, "w")

	mold = "# This pie has molded \n"
	rottenpie.write(mold)

	for line in thepie.readlines():
		rottenpie.write(line)

	thepie.close()
	rottenpie.close()

	os.remove(py)
	os.rename("%s.rotten" % py, py)



