from pdf_and_ocr.pdf_to_image import converting_pdf_into_image
from subprocess import call
import subprocess
import numpy as np 
import os
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import shutil
import pandas as pd
import matplotlib.pyplot as plt 
# import xml.etree.ElementTree as ET
import pytesseract
import string

"""
from yolo.runs.train.exp.x.weights import best.pt
Give all path from this folder
"""

num_pdf , num_images_list , All_total_pdf = converting_pdf_into_image()
command = [
    "python","yolo\\detect.py",
    "--weights", "yolo\\runs\\train\\exp13\\weights\\best.pt",
    "--img", "682",
    "--conf", "0.25",
    "--source", "pdf_and_ocr\\Recently PDF converted to IMAGES",
    "--save-txt","--hide-labels","--save-crop"
]
# command = [
#     "python","yolo\\detect.py",
#     "--weights", "yolo\\runs\\train\\exp\\x\\weights\\best.pt",
#     "--img", "682",
#     "--conf", "0.25",
#     "--source", "pdf_and_ocr\\Recently PDF converted to IMAGES",
#     "--save-txt","--hide-labels","--save-crop"
# ]
# subprocess.run(command)

# def delete_images_from_recent():
#     pass

def Getting_path():
    images_path = "yolo\\runs\\detect\\exp"
    num = 1
    tt = True
    while tt:
        num = num + 1
        if os.path.exists(images_path + f"{num}") and os.path.isdir(images_path + f"{num}"):
            pass
        else:
            # print(f"The folder at {images_path + str(num) } does not exist.")
            break
            # break
    get_images = images_path + str(num-1)
    labels_path = get_images + f"\\labels"
    return get_images , labels_path
## Extracted_image_and_dimensions_path = Separation()
images , labels = Getting_path()



# def Get_Dig_Info():






def Saving_images():
    # xxx = len(os.listdir("pdf_and_ocr\Executed PDF"))

    global num_pdf , num_images_list,images , labels , All_total_pdf
    text = labels
    # num_pdf  = 2
    # num_images_list = [0,1,2,3,4,5,6,7,8,9,10,0,1,2,3,4,5,6,7,8,9,10]
    # images = "yolo\\runs\\detect\\exp14"
    # text = "yolo\\runs\\detect\\exp14\\labels"
    # filter_img = ""
    result_digram = "RESULT DIGRAMS"
    result_digram_updated = "Result Digram Updated"
    result_text = "RESULT TEXT"
    all_labels_file_list = os.listdir(text)
    sec_sum = 0
    # arrrr1 = []

    sec_while = True
    for i in range(num_pdf):
        sec_while = True
        while sec_while:
            dig_fetching = cv2.imread(images + "\\" + f"pdf{i}_page{num_images_list[sec_sum]}.png",cv2.THRESH_BINARY )

            # print(images + "\\" + f"pdf{i}_page{num_images_list[sec_sum]}")
            check_file = text + "\\" + f"pdf{i}_page{num_images_list[sec_sum]}.txt"

            if f"pdf{i}_page{num_images_list[sec_sum]}.txt" not in all_labels_file_list:
                shutil.copy( images + "\\" + f"pdf{i}_page{num_images_list[sec_sum]}.png" , "Filtered_Images" )

            # if f"pdf{i}_page{num_images_list[sec_sum]}.txt" in all_labels_file_list :
# ==------------------------------------------------------------------------------------

            if f"pdf{i}_page{num_images_list[sec_sum]}.txt" in all_labels_file_list:
                repeat_digrams=0
                arrrr1 = []           
                filee = open(check_file , 'r')
                # with open(check_file , 'r') as filee:
                lines = filee.readlines()
                counting_images = 0

                for line in lines:
                    data = line.split()
                    if int(data[0]) == 1:   ### 1 means only digram
                        x_center, y_center, width, height = map(float, data[1:])
                        x1 = int((x_center - width / 2) * dig_fetching.shape[1])
                        y1 = int((y_center - height / 2) * dig_fetching.shape[0])
                        x2 = int((x_center + width / 2) * dig_fetching.shape[1])
                        y2 = int((y_center + height / 2) * dig_fetching.shape[0])
    
                        arrrr1.append(list(dig_fetching[y1:y2,x1:x2] ))
                        if repeat_digrams == 0:
                            van_d = cv2.imread(images +"\\"+ f"pdf{i}_page{num_images_list[sec_sum]}.png" , cv2.THRESH_BINARY)                    

                        if f"pdf{i}_page{num_images_list[sec_sum]}.txt" in all_labels_file_list:
                            for iii in range(y1,y2):
                                for jjj in range(x1,x2):
                                    van_d[iii][jjj] = 255

                Image.fromarray(van_d).save("Filtered_Images" +"\\"+f"pdf{i}_page{num_images_list[sec_sum]}.png")

                # for ip in range(len(arrrr1)):
                #     plt.imshow( arrrr1[ip] , cmap="gray")
                #     plt.show()

                tt = ""
                for line in lines:
                    data = line.split()
                    if int(data[0]) == 0:   ### 1 means only digram
                        x_center, y_center, width, height = map(float, data[1:])
                        x1 = int((x_center - width / 2) * dig_fetching.shape[1])
                        y1 = int((y_center - height / 2) * dig_fetching.shape[0])
                        x2 = int((x_center + width / 2) * dig_fetching.shape[1])
                        y2 = int((y_center + height / 2) * dig_fetching.shape[0])
                        print(x1,x2,y1,y2)
                        ocr_dig = van_d[y1:y2,x1:x2]
                        tt = pytesseract.image_to_string(ocr_dig)

                        if len(tt) == 0:
                            tt = "NONE"

                        tt = tt.replace(" " , "AAA")
                        for aabb in range(len(tt)):
                            if tt[aabb].isalpha() :
                                pass
                            else:
                                tt = tt.replace(tt[aabb]  , " ") 
                        tt = tt.replace(" "  , "") 
                        tt = tt.replace(" "  , "") 

                        tt = tt.replace("AAA" , " ")                        
                        saving_only_digrams = np.array(arrrr1[counting_images])
                        print(tt)
                        lll = Image.fromarray(saving_only_digrams)
                        lll.save(result_digram_updated +"\\"+f"pdf{i}_page{num_images_list[sec_sum]}_{counting_images}{tt[0:49]}.png")


                        # plt.imshow(saving_only_digrams , cmap = "gray")
                        # plt.show()

                        # print(result_digram_updated +"\\"+f"pdf{i}_page{num_images_list[sec_sum]}_{counting_images}_{tt}.png")
                        # Image.fromarray(saving_only_digrams).save(result_digram_updated +"\\"+f"pdf{i}_page{num_images_list[sec_sum]}_{counting_images}.png")
                        # cv2.imshow()
                        
                        # counting_images = counting_images + 1

























                    # if int(data[0]) == 0:   ### 1 means digram with fig_name
                    #     pass

# ======================================================

            #     filee.close()
            # counting_images = 0
            # if f"pdf{i}_page{num_images_list[sec_sum]}.txt" in all_labels_file_list:            
            #     filee = open(check_file , 'r')
            #     lines = filee.readlines()
            #     for line in lines:
            #         data = line.split()
            #         if int(data[0]) == 0:   ### 1 means only digram
            #             print("Executed")
            #             x_center, y_center, width, height = map(float, data[1:])
            #             x1 = int((x_center - width / 2) * dig_fetching.shape[1])
            #             y1 = int((y_center - height / 2) * dig_fetching.shape[0])
            #             x2 = int((x_center + width / 2) * dig_fetching.shape[1])
            #             y2 = int((y_center + height / 2) * dig_fetching.shape[0])
            #         else:
            #             continue
            #         ocr_dig = van_d[y1:y2,x1:x2]
            #         text = pytesseract.image_to_string(ocr_dig)

            #         saving_only_digrams = np.array(arrrr1[counting_images])
            #         Image.fromarray(saving_only_digrams).save(result_digram_updated +"\\"+f"pdf{i}_page{num_images_list[sec_sum]}_{counting_images}_{text}.png" )
            #         if int(data[0]) == 0:
            #             counting_images = counting_images + 1



                # filee.close()

                # pytesseract.tesseract_cmd = 'pdf and ocr\\text2image.exe'
                # counting_images = 0
                # text = ""
                # for line1 in lines:
                #     lines = filee.readlines()
                #     data = line1.split()
                #     if int(data[0]) == 0:
                #         x_center, y_center, width, height = map(float, data[1:])
                #         x1 = int((x_center - width / 2) * dig_fetching.shape[1])
                #         y1 = int((y_center - height / 2) * dig_fetching.shape[0])
                #         x2 = int((x_center + width / 2) * dig_fetching.shape[1])
                #         y2 = int((y_center + height / 2) * dig_fetching.shape[0])
                #     else:
                #         continue
                #     ocr_dig = van_d[y1:y2,x1:x2]
                #     text = pytesseract.image_to_string(ocr_dig)

                #     saving_only_digrams = np.array(arrrr1[counting_images])
                #     Image.fromarray(saving_only_digrams).save(result_digram_updated +"\\"+f"pdf{i}_page{num_images_list[sec_sum]}_{counting_images}_{text}.png" )
                #     if int(data[0]) == 0:
                #         counting_images = counting_images + 1



            if sec_sum + 1 == len(num_images_list):
                break 
            if num_images_list[sec_sum] > num_images_list[sec_sum + 1]:
                sec_while = False
            sec_sum = sec_sum + 1
        All_total_pdf = All_total_pdf + 1

Saving_images()


# def Implementing_OCR():
#     global num_pdf , num_images_list,images , labels  ,All_total_pdf  
#     # num_pdf  = 2
#     # num_images_list = [0,1,2,3,4,5,6,7,8,9,10,0,1,2,3,4,5,6,7,8,9,10]
#     # images = "yolo\\runs\\detect\\exp17"
#     # text = "yolo\\runs\\detect\\exp17\\labels"
#     text = labels
#     result_digram = "RESULT DIGRAMS"
#     result_text = "RESULT TEXT"
#     filtered_images = "Filtered_Images"
#     list_of_filtered_images = os.listdir(result_digram)

#     sec_sum = 0   
#     pytesseract.tesseract_cmd = 'pdf and ocr\\text2image.exe'
#     for i in range(num_pdf):
#         ff = result_text +"\\"+ f"Text_Of_pdf_{i}.txt"
#         f = open(ff ,"w")
#         sec_while = True
#         while sec_while:
#             if os.path.exists(filtered_images + "\\" +  f"pdf{i}_page{num_images_list[sec_sum]}.png"):
#                 img =  filtered_images + "\\" +  f"pdf{i}_page{num_images_list[sec_sum]}.png" 
#                 x = cv2.imread(img  , cv2.THRESH_BINARY)
#                 x = cv2.resize(x , (2000,2000))

#                 # for ii in range(2000):
#                 #         for jj in range(2000):
#                 #             if x[ii][jj] > 200:
#                 #                 x[ii][jj] = 255
#                 #             if x[ii][jj] < 100:
#                 #                 x[ii][jj] = 0
#                 text = pytesseract.image_to_string(x)
#                 text = text.replace("\n" , "")
#                 # print(f"{num_images_list[sec_sum]} IMPLEMENTED")
#                 f.write(text)
#                 f.write(str(f"\n\n\n==========  PAGE {num_images_list[sec_sum]} ===========\n\n\n"))
#             if sec_sum + 1 == len(num_images_list):
#                 break 
#             if num_images_list[sec_sum] > num_images_list[sec_sum + 1]:
#                 sec_while = False
#             sec_sum = sec_sum + 1
#         All_total_pdf = All_total_pdf + 1
#         # f.close()

# Implementing_OCR()


