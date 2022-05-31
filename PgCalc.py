#opencv
import imghdr
import cv2
import pytesseract
import pyautogui
import tkinter as tk 
from tkinter import ttk


def pangyaProgram():
    imgPangya = pyautogui.screenshot(region=(0,25,158,380))
    imgPangya.save("PangyaImgs\\imagemPangya.png")
    print("FotoSalve")

    pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
    img = cv2.imread("PangyaImgs\\imagemPangya.png")

    resultado = pytesseract.image_to_string(img)

    with open('PangyaTxt\\PangyaValues.txt','w') as arquivoLido:
        for valor in resultado:
            arquivoLido.write(str(valor))



# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Button Demo')

# exit button
exit_button = ttk.Button(
    root,
    text='RODAR',
    command=lambda: pangyaProgram()
)

exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()



        





