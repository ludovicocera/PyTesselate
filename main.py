import math
import tkinter
from io import BytesIO
from PIL import Image
from tkinter import filedialog

root = tkinter.Tk()
root.withdraw()

path = filedialog.askopenfilename()

im = Image.open(path)

macroPixelHeight = int(input("Number of vertical boxes: "))
macroPixelSize = math.floor(im.size[1] / (macroPixelHeight * 2))
macroPixelWidth = math.floor(macroPixelHeight * im.size[0] / im.size[1])

newIm = Image.new('RGB', (macroPixelWidth * macroPixelSize,
                          macroPixelHeight * macroPixelSize))

for i in range(0, macroPixelHeight):
    for j in range(0, macroPixelWidth):
        cropX = j * macroPixelSize * 2 + macroPixelSize
        cropY = i * macroPixelSize * 2 + macroPixelSize
        box = im.crop(
            (cropX, cropY, cropX + macroPixelSize, cropY + macroPixelSize))
        newIm.paste(box, (j * macroPixelSize, i * macroPixelSize))

newIm.show()
