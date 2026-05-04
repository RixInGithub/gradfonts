from PIL import Image
from sys import argv
if len(argv)<2: raise Exception
name = argv[1]
with open("alpha.txt")as aIO:a=[b for b in [[b.rstrip("\n").split("=")[0],b[3]] for b in(aIO).readlines()] if not b[1].isspace()]
temp = Image.open(name+"Temp.png").convert("RGBA")
new = Image.new("RGBA",(temp.width*len(a),temp.height))
y = 0
while y<temp.height:
	count = 0
	while count < len(a):
		x = 0
		while x < temp.width:
			new.putpixel(((count*temp.width)+x,y),temp.getpixel((x,y)))
			x += 1
		count += 1
	y += 1
new.save(name+"Ext.png")
with open("toWrite.txt","w") as wIO: wIO.write("".join([b[1] for b in a]))