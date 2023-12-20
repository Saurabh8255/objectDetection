import subprocess
import os
from models.common import DetectMultiBackend

def perform_object_detection(weights_path, img_size, confidence, source_path, hide_labels=True, save_crop=True, save_txt=True):
    command = f"python {os.path.join(os.getcwd(), 'detect.py')} \
                --weights {weights_path} \
                --img {img_size} \
                --conf {confidence} \
                --source {source_path} \
                {'--hide-labels' if hide_labels else ''} \
                {'--save-crop' if save_crop else ''} \
                {'--save-txt' if save_txt else ''}"

    subprocess.run(command, shell=True)

def main():
    # Set your desired parameters
    weights_path = os.path.abspath(r"F:\\Celestial\saurabh_enviroment\saurabh_venv/best.pt")
    img_size = 507
    confidence = 0.25
    source_path = os.path.abspath(r"F:\\Celestial\saurabh_enviroment\saurabh_venv/pdf_images")

    # Call the YOLOv5 detection function
    perform_object_detection(weights_path, img_size, confidence, source_path)

if __name__ == "__main__":
    main()
