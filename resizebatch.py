"""
This is to resize a batch of images from their original size to (100X100)
"""
import cv2
import glob # this is a built-in library to retrieve path recursively

image_list =glob.glob("*.jpg")

for item in image_list:
    img = cv2.imread(item, 0)
    resized_image = cv2.resize(img,(100,100))
    cv2.imshow("window",resized_image)
    cv2.waitKey(2000) # waiting for 2 seconds
    cv2.imwrite("re_"+item, resized_image)
    cv2.destroyAllWindows()
    