import cv2
import pytesseract

def perform_ocr(image_path):
    """
    Perform OCR on an image using Tesseract.

    Parameters:
    - image_path (str): Path to the image.

    Returns:
    - str: Extracted text from the image.
    """
    # Set the Tesseract executable path (optional, adjust as needed)
    pytesseract.pytesseract.tesseract_cmd = r'F:\Celestial\saurabh_enviroment\saurabh_venv\Scripts\pytesseract.exe'

    # Initialize the output text as an empty string
    output_text = ''

    # Gaussian blur filter parameters
    gaussian_blur_kernel = (1, 1)
    gaussian_blur_sigma = 0.8

    # Image binarization parameters
    binarization_threshold = 80  # Adjust the threshold as needed

    # Load the image
    img = cv2.imread(image_path)

    # Image preprocessing - Method 1
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Grayscale conversion
    img1 = cv2.convertScaleAbs(img1, alpha=1.5, beta=50)  # Enhance contrast and brightness
    blurred1 = cv2.GaussianBlur(img1, gaussian_blur_kernel, gaussian_blur_sigma)
    img1 = cv2.addWeighted(img1, 1, blurred1, -0.3, 0)
    img1 = cv2.resize(img1, None, fx=1, fy=1, interpolation=cv2.INTER_CUBIC)  # Resize
    img1 = cv2.GaussianBlur(img1, gaussian_blur_kernel, gaussian_blur_sigma)
    _, img1 = cv2.threshold(img1, binarization_threshold, 255, cv2.THRESH_BINARY)
    extracted_text1 = pytesseract.image_to_string(img1)

    # Image preprocessing - Method 2
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Grayscale conversion
    img2 = cv2.resize(img2, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)  # Resize
    _, img2 = cv2.threshold(img2, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # Thresholding
    img2 = cv2.GaussianBlur(img2, gaussian_blur_kernel, gaussian_blur_sigma)
    _, img2 = cv2.threshold(img2, binarization_threshold, 255, cv2.THRESH_BINARY)
    extracted_text2 = pytesseract.image_to_string(img2)

    # Choose the result with non-empty text
    if extracted_text1.strip():
        output_text = extracted_text1
    else:
        output_text = extracted_text2

    # Append the image file name as a header
    output_text += f"Image File: {image_path}\n"

    return output_text
#example uses
image_path = 'F:\Celestial\saurabh_enviroment\saurabh_venv\Test1.pdf'
ocr_result = perform_ocr(image_path)