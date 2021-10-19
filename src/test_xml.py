from imutils.paths import list_files
from imutils.paths import list_images
from bs4 import BeautifulSoup
import cv2

xml_paths = "dataset\\output\\xml"
image_paths = "dataset\\output\\images"

xml_paths = list(list_files(xml_paths))
image_paths = list(list_images(image_paths))

for xml_path in xml_paths:
    contents = open(xml_path).read() # đọc toàn bộ file
    soup = BeautifulSoup(contents,"xml")
    image_path = soup.find("path")
    # print(image_path)
    image = cv2.imread(image_path.text)
    object_ = soup.find_all("object")
    for obj in object_:
        bbox = soup.find_all("bndbox")
        for bounding_box in bbox:
            xmin = int(bounding_box.find("xmin").text)
            ymin = int(bounding_box.find("ymin").text)
            xmax = int(bounding_box.find("xmax").text)
            ymax = int(bounding_box.find("ymax").text)
            cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 255), 2)
    cv2.imshow("res",image)
    cv2.waitKey(0)