import os
import fitz  # PyMuPDF

def convert_pdf_to_images(pdf_file, output_folder):
    """
    Convert each page of a PDF file into images and save them to the specified folder.

    Parameters:
    - pdf_file (str): Path to the PDF file.
    - output_folder (str): Path to the folder where images will be saved.

    Returns:
    - List of tuples: Each tuple contains the page number and corresponding image.
    """
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Open the PDF file
    pdf_document = fitz.open(pdf_file)

    # Iterate through the pages and convert to images
    images = []
    for i in range(pdf_document.page_count):
        page = pdf_document.load_page(i)
        image = page.get_pixmap()
        images.append((i, image))  # Store the page number along with the image

    # Save the images to the specified folder
    for i, (page_number, image) in enumerate(images):
        # Pad the number with leading zeros and save the image
        image.save(os.path.join(output_folder, f'{i:04d}.png'), "png")

    # Close the PDF document
    pdf_document.close()

    return images


# #Example uses
pdf_file_path = r'F:\Celestial\saurabh_enviroment\saurabh_venv/BD.pdf'
output_images_folder = r'F:\Celestial\saurabh_enviroment\saurabh_venv/pdf_images'
converted_images = convert_pdf_to_images(pdf_file_path, output_images_folder)
