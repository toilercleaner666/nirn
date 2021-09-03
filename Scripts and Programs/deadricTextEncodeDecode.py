import string
deadric = ['à', 'á', 'â', 'ã', 'ä', 'å', 'æ', 'ç', 'è', 'é', 'ê', 'ë', 'ì', 'í', 'î', 'ï', 'ð', 'ñ', 'ò', 'ó', 'ô', 'õ', 'ö', 'û', 'ø', 'ù']
empireChar = 'ú'

def encode(text):
	out = text
	out = out.replace("$$EMPIRECHAR$$", empireChar)
	for i in range(26):
		out = out.replace(string.ascii_uppercase[i], string.ascii_lowercase[i])
	for i in range(26):
		out = out.replace(string.ascii_lowercase[i], deadric[i])
	return out

def decode(text):
	out = text
	out = out.replace(empireChar, "$$EMPIRECHAR$$")
	for i in range(26):
		out = out.replace(deadric[i], string.ascii_lowercase[i])
	return out

while True:
	print("\n(e)ncode, (d)ecode, or (q)uit")
	mode = input()
	if mode == "quit" or mode == 'q':
		exit()
	elif mode == "encode" or mode == 'e':
		print("Enter text to encode. For Empire Character, use $$EMPIRECHAR$$")
		t = input()
		print("\nEncoded Text: " + encode(t))
	elif mode == "decode" or mode == 'd':
		print("Enter text to decode")
		t = input()
		print("\nDecoded Text: " + decode(t))
	else:
		print("Please enter encode, decode, or quit")