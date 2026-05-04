from urllib.request import urlopen
from sys import stdout as io

with urlopen("https://www.unicode.org/Public/MAPPINGS/VENDORS/ADOBE/stdenc.txt") as adobeIO:
	print("#include <stdint.h>")
	io.write("uint16_t uni2ase[][2] = {")
	notFirst = False
	for l in adobeIO.readlines():
		if l[0]==b"#"[0]: continue
		io.write("%s{0x%s,0x%s}" % tuple([","if(notFirst)else""]+l.decode().split("\t")[:2]))
		notFirst = True
	print("};")