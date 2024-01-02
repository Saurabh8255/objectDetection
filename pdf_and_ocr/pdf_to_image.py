# import os
# import fitz  # PyMuPDF

# def converting_pdf_into_image():
#     # Path to the PDF file
#     pdf_file = 'pdf_and_ocr\\Upload PDF Here\\M5.pdf'

#     # Create a folder to store the images
#     output_folder = 'pdf_and_ocr\\PDF converted to IMAGES'
#     os.makedirs(output_folder, exist_ok=True)

#     # Open the PDF file
#     pdf_document = fitz.open(pdf_file)

#     # Iterate through the pages and convert to images
#     images = []
#     for i in range(pdf_document.page_count):
#         page = pdf_document.load_page(i)
#         image = page.get_pixmap()
#         images.append((i, image))  # Store the page number along with the image

#     # Save the images to the 'images' folder
#     for i, (page_number, image) in enumerate(images):
#         # Pad the number with leading zeros and save the image
#         image.save(os.path.join(output_folder, f'{i:04d}.png'), "png")
#     pdf_document.close()





import os
import fitz  # PyMuPDF
import shutil
def converting_pdf_into_image():
    recent = "pdf_and_ocr\\Recently PDF converted to IMAGES\\"
    aa = 0
    bb = []
    # Path to the PDF file
    pdf_folder = 'pdf_and_ocr\\Upload PDF Here'
    xxxx = sorted( os.listdir(pdf_folder))

    implementation_done_pdf = len(os.listdir("pdf_and_ocr\\Executed PDF"))
    cc = len(os.listdir("pdf_and_ocr\Executed PDF"))
    # for i in os.listdir(pdf_folder):
    #     print(i)
    # Create a folder to store the images
    for i in range(len(xxxx)):

        aa = aa + 1
        pdf_file = pdf_folder+"\\"+ xxxx[i]
        output_folder = 'pdf_and_ocr\\PDF converted to IMAGES'
        os.makedirs(output_folder, exist_ok=True)

        # Open the PDF file
        pdf_document = fitz.open(pdf_file)

        # Iterate through the pages and convert to images
        images = []
        for j in range(pdf_document.page_count):
            page = pdf_document.load_page(j)
            image = page.get_pixmap()
            images.append((j, image))  # Store the page number along with the image
            bb.append(j)
        # Save the images to the 'images' folder
        for k, (page_number, image) in enumerate(images):
            # Pad the number with leading zeros and save the image
            image.save(recent + f"pdf{implementation_done_pdf}_page{k}.png" , "png") 
            image.save(os.path.join(output_folder,  f"pdf{implementation_done_pdf}_page{k}.png"  ), "png") 
        # xyz = xyz + 1
        # pdf_document.close()
        # if xyz == implementation_done_pdf:
        #     break   
        implementation_done_pdf = implementation_done_pdf + 1
    for j in range(len(xxxx)):
        shutil.copy( pdf_folder + "\\" + xxxx[j] ,"pdf_and_ocr\\Executed PDF")
    return aa,bb,cc











# converting_pdf_into_image()

#PAGES SAVED :   pdf{i}_page{k}.png






