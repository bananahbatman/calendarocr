import cv2
from pytesseract import image_to_string
import re
"""
links: https://www.freecodecamp.org/news/getting-started-with-tesseract-part-ii-f7f9a0899b3f/\\

greyscale, gaussian, otsu's threshold
"""

def process_image(filename, greyscale=0, read=0, blur=0, threshold=0):
    """
    Returns an image processed into a string using preprocessing methods specified
    by the defined parameters.

    parameters:
        filename: name of file in str
        greyscale: boolean value
        read: whether to read/display the file or not
        blur: 1 (averaging), 2 (gaussian), 3 (median), 4 (bilateral filtering)
        threshold: 1 (simple), 2 (adaptive), 3 (otsu's)
    """

    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image', 600,600)

    if greyscale:
        img = cv2.imread(filename, 0) #the 0 converts the image greyscale
    else:
        img = cv2.imread(filename)

    if blur == 1:
        img = cv2.blur(img,(5,5))
    elif blur == 2:
        img = cv2.GaussianBlur(img, (5, 5), 0)
    elif blur == 3:
        img = cv2.medianBlur(img, 3)
    elif blur == 4:
        img = cv.bilateralFilter(img,9,75,75)

    if threshold == 1:
        ret, img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
    elif threshold == 2:
        img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
    elif threshold == 3:
        img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    if read:
        cv2.imshow("image", img) #display image in 600x600
        cv2.waitKey(0) #wait until next key is pressed to exit viewing

    # Adding custom options
    custom_config = '--oem 3 --psm 6'

    return image_to_string(img, config=custom_config)
