import glob
import os

# Get all pies
allpies = glob.glob("*.py")

for py in allpies:
	# Open the pie
	thepie = open(py, "r")

	# Open a rotten pie
	rottenpie = open("%s.rotten" % py, "w")
	# Write our mold to the rotten pie
	rottenpie.write("# This pie has molded \n")

	# Read the original pie and write all lines to the rotten pie
	for line in thepie.readlines():
		rottenpie.write(line)

	# Close these two pies
	thepie.close()
	rottenpie.close()

	# Delete the original
	os.remove(py)
	# Make the rotten pie look like the original...
	os.rename("%s.rotten" % py, py)



