from PIL import Image
import matplotlib.pyplot as plt
import math

def histograma(im : Image):
    (w, h) = im.size
    values = [0] * 256
    valor : int
    for j in range(0, h):
        for i in range(0, w):
            valor = im.getpixel((i, j))
            values[valor] += 1
    plt.plot(values)
    plt.show()

def binario(limiar : int, im : Image):
    (w, h) = im.size
    out = Image.new('1', (w, h))
    valor : int
    for j in range(0, h):
        for i in range(0, w):
            valor = im.getpixel((i, j))
            if valor <= limiar:
                out.putpixel((i, j), 0)
            else:
                out.putpixel((i, j), 1)
    plt.imshow(out)
    plt.show()

def logaritmica(limiar, im : Image):
    (w, h) = im.size
    out = Image.new('P', (w, h))
    valor : int
    for j in range(0, h):
        for i in range(0, w):
            valor = im.getpixel((i, j))
            valor = math.log(1 + ((math.e ** limiar) -1)) * valor
            out.putpixel((i, j), int(valor))
    plt.imshow(out)
    plt.show()

def invert(im : Image):
    (w, h) = im.size
    out = Image.new('P', (w, h))
    valor : int
    for j in range(0, h):
        for i in range(0, w):
            valor = im.getpixel((i, j))
            valor = abs(valor - 255)
            out.putpixel((i, j), valor)
    plt.imshow(out)
    plt.show()

if __name__ == "__main__":
    limiar = 1
    imagem = Image.open("/home/udesc/Documentos/cameraman.png").convert('L')
    # histograma(imagem)
    # binario(limiar, imagem)
    # logaritmica(limiar, image m)
    # invert(imagem)
