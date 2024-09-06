import pytesseract
import cv2
import PIL.Image
# copy paste directory to the images

#default configuration for the image processing: use 1
myconfig = r"--psm 1 --oem 3"
#6 is good for kda

#what file will be processed and turned into text
myIMG = #saved image links go here
text = pytesseract.image_to_string(PIL.Image.open(myIMG), config=myconfig)
print(text)

list = text.split()
num = 0;
ssh = 0;
cs = 0;
for x in list:
    if(x == "super"):
        list[num] = list[num] + "." + list[num + 1] + "." + list[num + 2]
        list.pop(num + 1)
        list.pop(num + 1)
    if(x == "Chad"):
        list[num] = list[num] + " " + list[num + 1]
        list.pop(num + 1)
    num = num + 1
    print(x)
 
print(list)
