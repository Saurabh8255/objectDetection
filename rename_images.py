from PIL import Image, ImageDraw
from IPython.display import display
import pytesseract
import cv2
import numpy as np
import os

def process_box(box, img_width, img_height):
    label, x_center, y_center, width, height = box

    abs_width = int(width * img_width)
    abs_height = int(height * img_height)

    x = int(x_center * img_width - abs_width / 2)
    y = int(y_center * img_height - abs_height / 2)

    return x, y, abs_width, abs_height

def extract_texts_and_rename_images(imaged_path, labels_path, output_folder):
    image = Image.open(image_path)

    with open(labels_path, 'r') as file:
        box_coordinates = [list(map(float, line.split())) for line in file]

    img_width, img_height = image.size

    extracted_texts = []

    for box_values in box_coordinates:
        label, _, _, _, _ = box_values
        x, y, abs_width, abs_height = process_box(box_values, img_width, img_height)

        mask = Image.new('L', image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.rectangle([x, y, x + abs_width, y + abs_height], fill=255)

        image.paste((255, 255, 255), mask=mask)

    display(image)

    for i, box_values in enumerate(box_coordinates):
        label, _, _, _, _ = box_values
        x, y, abs_width, abs_height = process_box(box_values, img_width, img_height)

        region_of_interest = image.crop((x, y, x + abs_width, y + abs_height))
        img_cv2 = cv2.cvtColor(np.array(region_of_interest), cv2.COLOR_RGB2BGR)

        gaussian_blur_kernel = (3, 7)
        gaussian_blur_sigma = 1.2
        binarization_threshold = 80

        img1 = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2GRAY)
        img1 = cv2.convertScaleAbs(img1, alpha=1.5, beta=50)
        blurred1 = cv2.GaussianBlur(img1, gaussian_blur_kernel, gaussian_blur_sigma)
        img1 = cv2.addWeighted(img1, 1, blurred1, -0.3, 0)
        img1 = cv2.resize(img1, None, fx=1, fy=1, interpolation=cv2.INTER_CUBIC)
        img1 = cv2.GaussianBlur(img1, gaussian_blur_kernel, gaussian_blur_sigma)
        _, img1 = cv2.threshold(img1, binarization_threshold, 255, cv2.THRESH_BINARY)
        extracted_text1 = pytesseract.image_to_string(img1).strip()
        if extracted_text1:
            extracted_texts.append(extracted_text1)

        img2 = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2GRAY)
        img2 = cv2.resize(img2, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        _, img2 = cv2.threshold(img2, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        img2 = cv2.GaussianBlur(img2, gaussian_blur_kernel, gaussian_blur_sigma)
        _, img2 = cv2.threshold(img2, binarization_threshold, 255, cv2.THRESH_BINARY)
        extracted_text2 = pytesseract.image_to_string(img2).strip()
        if extracted_text2:
            extracted_texts.append(extracted_text2)

    print("Extracted Texts:", extracted_texts)

    for img, extracted_text in zip(os.listdir(output_folder), extracted_texts):
        old_path = os.path.join(output_folder, img)
        new_path = os.path.join(output_folder, extracted_text + '.jpg')
        os.rename(old_path, new_path)

# # Example usage:
# imaged_path = '/content/drive/MyDrive/yolov5/runs/detect/exp7/0196.png'
# labels_path = '/content/drive/MyDrive/yolov5/runs/detect/exp7/labels/0196.txt'
# output_folder = '/content/drive/MyDrive/yolov5/runs/detect/exp7/crops/object'
# extract_texts_and_rename_images(imaged_path, labels_path, output_folder)
