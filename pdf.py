from re import A
from pdf2image import convert_from_path
from imgtxt import tesseract
import cv2
import os


# title = input("Pdf files name: ")


def menu():
    global quality
    # print("""
    #     Image format: 
    #     1. Very High Resolution - 700 dpi
    #     2. High Resolution - 500 dpi
    #     3. Medium Resolution - 300 dpi
    #     4. Low Resolution - 100 dpi
    #     5. Very Low Resolution - 50 dpi
    #     """)
    while True:
        # choice = input('Choose One: ')
        quality = 1080 #if choice == '1' else 500 if choice == '2' else 300 if choice == '3' else 100 if choice == '4' else 50 if choice == '5' else "Wrong choice"
        program()
        print('Have a Nice Code')
        quit()


def program():
    j = -1
    for file_name in os.listdir("./folder"):
        if file_name.endswith(".pdf"):
            # if it's a txt file, print its name (or do whatever you want)
            # print(file_name)
            j += 1
            images = convert_from_path("./folder/"+file_name, quality)
            for i, image in enumerate(images):
                image.save(f'./dataset/data/save_{j}_{i}.jpeg')
                data_file =open("./output/test_images.txt",'a')
                data_file.write(f'save_{j}_{i}.jpeg\n')
                data_file.close()
                # a = cv2.imread(f'save_{i}.png')
                # tesseract(a)


    # tesseract(images)


if __name__ == '__main__':
    menu()