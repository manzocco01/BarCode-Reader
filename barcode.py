import cv2 as cv
from pyzbar import pyzbar
from tqdm import tqdm

numeri = []     #creazione vettore dove inserire il risultato della scansione


for i in tqdm(range(1,9375)):

    collegamento = (f"C:/Users/liamm/Desktop/Barcode_World/{i}.png")   #directory dei codici a barre
    image = cv.imread(collegamento)                                    #caricamneto dell'immagine
    numeri.append(pyzbar.decode(image)[0][0].decode("utf-8"))          #scansione



for x in numeri:
        print(x, end="")















