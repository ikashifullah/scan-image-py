import cv2
import pytesseract
from pprint import pprint

img = cv2.imread("./images/table.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)

_, threshold = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

data = pytesseract.image_to_string(threshold)

text_data = data.split("\n")
all_text = ''

for text in text_data:
    # use this to filter the data, like which fields you want out
    # if ["From Date", "To Date", "Transferred To", "etc", "etc"] in line:
    pprint(text)
    all_text += text + "\n"

# save it in a file for future use
with open("text.txt", "w") as f:
    f.write(str(all_text))