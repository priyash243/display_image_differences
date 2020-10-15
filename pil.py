from Pil import Image,ImageChops
img1=Image.open('img1.jpg')
img2=Image.open('ima2.jpg)
diff=ImageChops.difference(img1,img2)
print(diff.getbox()) #shows difference in no. of  pixels
if diff.getbox():
  diff.show() #shows actual diff in images
