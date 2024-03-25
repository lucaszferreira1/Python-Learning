from PIL import Image
import matplotlib.pyplot as plt

def blend(im1, im2, alpha):
    (imw, imh) = im1.size
    im3 = Image.new(im1.mode, (imw, imh))
    for h in range(0, imh):
        for w in range(0, imw):
            pix = im1.getpixel((w, h))
            pix *= (1 - alpha)
            pix += alpha * im2.getpixel((w, h))
            im3.putpixel((w, h), int(pix))
    return im3

if __name__ == "__main__":
    im1 = Image.open("Imagens para testes/MorrisHolidayMetallic/MorrisHolidayMetallic5873_gray.png")
    im2 = Image.open("Imagens para testes/MorrisHolidayMetallic/MorrisHolidayMetallic5874_gray.png")
    
    im3 = blend(im1, im2, 1)

    plt.imshow(im3, cmap='gray')
    plt.show()