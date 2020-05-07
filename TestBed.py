import cv2

img = cv2.imread('./Data/TryImage.jpg')
grap = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

canny_lthreshold = 150
canny_hthreshold = 250
edges = cv2.Canny(grap,canny_lthreshold,canny_hthreshold)
