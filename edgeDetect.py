from PIL import Image
ImageURL="./lenna.png"
shrinkfactor=4
detectfactor=20
image1=Image.open(ImageURL).convert('L')
rst=Image.open(ImageURL).convert('L')
w=image1.size[0]
h=image1.size[1]
shrinkImage=image1.resize((int(w/shrinkfactor),int(h/shrinkfactor)), Image.ANTIALIAS)
largeImage=shrinkImage.resize((w,h),Image.ANTIALIAS)
pix=image1.load()
pixrst=rst.load()
pixl=largeImage.load()
image1.show()
largeImage.show()
for x in range(0,w):
    for y in range(0,h):
        g=pix[x,y]
        lg=pixl[x,y]
        diff=abs(g-lg)
        pixrst[x,y]=0
        if diff>detectfactor:
            pixrst[x, y] = 255
rst.save("edge.png","png")
