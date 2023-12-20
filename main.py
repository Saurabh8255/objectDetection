from pdf_to_images import convert_pdf_to_images
# from ocr import perform_ocr
from detection import perform_object_detection
from rename_images import extract_texts_and_rename_images

def main():
    # Convert PDF to images
    pdf_file_path = r'F:\Celestial\saurabh_enviroment\saurabh_venv/BD.pdf'
    output_images_folder = r'F:\Celestial\saurabh_enviroment\saurabh_venv/pdf_images'
    converted_images = convert_pdf_to_images(pdf_file_path, output_images_folder)

    # # OCR, Object Detection, and Text Extraction
    # for page_number, image_path in converted_images:
    #     # OCR
    #     image_path = '/content/drive/MyDrive/yolov5/runs/detect/exp2/crops/fig/0032.jpg'
    #     ocr_result = perform_ocr(image_path)

    #     print(f"OCR Result for Page {page_number}: {ocr_result}")

    #     # Object Detection
    # weights_path = '/content/drive/MyDrive/yolov5/runs/train/exp13/weights/best.pt'
    # img_size = 507
    # confidence_threshold = 0.25
    # source_folder = '/content/drive/MyDrive/image_text_extraction_project/pdf_images'
    # hide_labels = True
    # save_crop = True
    # save_txt = True
    # perform_object_detection(weights_path, img_size, confidence_threshold, source_folder, hide_labels, save_crop, save_txt)

    #     # Text Extraction and Image Renaming
    #     # Example usage in main.py:
    
    print("hello world")

    !python /content/drive/MyDrive/yolov5/detect.py --weights /content/drive/MyDrive/yolov5/runs/train/exp13/weights/best.pt --img 507 --conf 0.25 --source /content/drive/MyDrive/image_text_extraction_project/pdf_images --hide-labels --save-crop --save-txt

    imaged_path = '/content/drive/MyDrive/yolov5/runs/detect/exp7/0196.png'
    labels_path = '/content/drive/MyDrive/yolov5/runs/detect/exp7/labels/0196.txt'
    output_folder = '/content/drive/MyDrive/yolov5/runs/detect/exp7/crops/object'
    extract_texts_and_rename_images(imaged_path, labels_path, output_folder)



if __name__ == "__main__":
    main()
