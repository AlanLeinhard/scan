import cv2
import pytesseract
import PIL

def tesseract(a):


    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    # img = cv2.imread('D:\hackaton\save_0.png')
    img = a
    # img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    config = r'--oem 3 --psm 6'

    data = pytesseract.image_to_data(img, config=config, lang='rus+eng')
    text = pytesseract.image_to_string(img, config=config, lang='rus')
    print(text)

    for i,el in enumerate(data.splitlines()):
        if i == 0:
            continue

        el = el.split()

        
        text = pytesseract.image_to_string(img, config=config, lang='rus')
        if(el == 'Щетневу'):            
            x, y, w, h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
            cv2.rectangle(img, (x,y), (w+x, h+y), (0,255,0), 2)



        # try:
        # x, y, w, h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
        # cv2.rectangle(img, (x,y), (w+x, h+y), (0,255,0), 2)
        # cv2.putText(img, el[11], (x,y), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 1)
        # except IndexError: 
        #     print("Операция была пропущена")

    cv2.imwrite('save.png',img)
    cv2.imshow('Result', img)
    cv2.waitKey(0)





    
    # arrs = [a]

    # for arr in arrs:

    #     pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    #     # img = cv2.imread('D:\hackaton\save_0.png')
    #     img = arr
    #     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #     config = r'--oem 3 --psm 6'

    #     data = pytesseract.image_to_data(img, config=config, lang='rus+eng')
    #     text = pytesseract.image_to_string(img, config=config, lang='rus')
    #     print(text)

    #     for i,el in enumerate(data.splitlines()):
    #         if i == 0:
    #             continue

    #         el = el.split()
    #         try:
    #             x, y, w, h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
    #             cv2.rectangle(img, (x,y), (w+x, h+y), (0,0,255), -1)
    #             cv2.putText(img, el[11], (x,y), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 1)
    #         except IndexError: 
    #             print("Операция была пропущена")

    #     cv2.imshow('Result', img)
    #     cv2.waitKey(0)
