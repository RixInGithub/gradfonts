from PIL import Image
from functools import reduce

def hexify(data, w):
	if w%8 != 0: raise Exception("idiot")
	w//=4 # this algo calculates nybbles rather than full bytes
	out = []
	tmp = ["", []]
	for px in data:
		if len(tmp[1])<4:
			tmp[1] += [px]
		if len(tmp[1])==4:
			if len(tmp[0])<w:
				tmp[0]+=hex(reduce(lambda a,b: (a<<1)|b, tmp[1], 0))[2:].upper()
			if len(tmp[0])==w:
				out += [tmp[0]+""]
				tmp[0] = ""
			tmp[1] = []
	return "\n".join(out)

if __name__=="__main__":
	img = Image.open(input("img: ")).convert("1")
	print(hexify([a==0 for a in img.getdata()], img.width))