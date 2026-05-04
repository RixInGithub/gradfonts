from PIL import Image
from hexifier import *

def main(argv):
	if len(argv)<2: raise Exception
	name = argv[1]
	img = Image.open(name+".png").convert("RGB")
	with open("alpha.txt")as aIO:a=[b for b in [[b.rstrip("\n").split("=")[0],b[3]] for b in(aIO).readlines()] if not b[1].isspace()]
	w = img.width//len(a)
	h = img.height
	bbx = [w,h,0,0]
	print("STARTFONT 2.1")
	print("FONT", argv[1])
	print("SIZE", max(w,h), 96, 96)
	print("FONTBOUNDINGBOX", *bbx)
	print("CHARS", len(a)+1)
	print("STARTPROPERTIES 2")
	print("CHARSET_REGISTRY \"Adobe\"")
	print("CHARSET_ENCODING \"Standard\"")
	print("ENDPROPERTIES")
	fontIdx = 0
	for b in a:
		print("STARTCHAR", "char"+b[0])
		print("ENCODING", int(b[0],16))
		print("DWIDTH", w, 0)
		print("BBX", *bbx)
		print("BITMAP")
		print(hexify([max(a)==0 for a in img.crop((fontIdx*w,0,(fontIdx+1)*w,h)).getdata()],w))
		print("ENDCHAR")
		fontIdx += 1
	print("STARTCHAR space")
	print("ENCODING 32")
	print("DWIDTH", w, 0)
	print("BBX", *bbx)
	print("BITMAP")
	print("\n".join(["0"*(w//4) for a in range(h)]))
	print("ENDCHAR")
	print("ENDFONT")

main(__import__("sys").argv)