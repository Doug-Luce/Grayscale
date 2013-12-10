#Team #GreyScale
#Douglas
#Barak
#Jonathan

#Grayscale working now with PIL
#Grayscale before and after working, code on line 39, 42 ,26, 27
from PIL import Image, ImageTk
from graphics import GraphWin
from tkinter import filedialog # Will be used to open the file from the user
import tkinter
import os

# Global variables for radio buttons----
radio1 = True
radio2 = False
radio3 = False
radio4 = False
#--------------------------------------------

# Global variables for picture-----------
pic = None
tkPic = None
tkPic2 = None
picToConvert = None
picWidth = 0
picHeight = 0
canvas1 = None
#---------------------------------------------

def rotateIt(pic):
    pictureRotated = pic.rotate(180)
    return pictureRotated
# Function for radio buttons

def whichSelected(numberSelected):
        global radio1
        global radio2
        global radio3
        global radio4
        if numberSelected == 4:
            radio1 = False
            radio4 = True
        if numberSelected == 3:
            radio1 = False
            radio3 = True
        if numberSelected == 2:
            radio1 = False
            radio2 = True
        if numberSelected == 1:
            radio1 = True


# Gray Algorithms---------------------------------------------
def grayAverage(r,g,b):
    algorithm = (r + g + b) // 3
    return (algorithm)

def invertRGB(r,g,b):
        r = 255 - r
        g = 255 - g
        b = 255 - b
        return (r,g,b)

def lightness(r,g,b):
        algorithm = (max(r, g, b) + min(r, g, b)) // 2
        return (algorithm)

def luminosity(r,g,b):
        algorithm = int(((0.21 * r) + (0.71 * g) + (0.07 * b)))
        return (algorithm)

def getRGB(r,g,b):
        red = eval( input ("Enter the value of red: "))
        green = eval(input ("Enter the value of green: "))
        blue = eval(input ("Enter the value of blue: "))
        algorithm =  red-r + green-g + blue-b // 3
        return (algorithm)
# End Gray Algorithms-----------------------------------------------------------------------------

# Draws window, opens picture selected by user, packs the canvas
def drawWindow():
    window = tkinter.Tk()
    window.geometry("840x550")
    window.title(os.environ.get( "USERNAME" )) # sets the window title to the
    return window

def drawCanvas():
    global window
    global canvas1
    canvas1 = tkinter.Canvas(window, width = 820, height =340) # Draws a canvas onto the tkinter window
    canvas1.pack()
    return canvas1

# Global variables for window and canvas
window = drawWindow()
canvas1 = drawCanvas()
# -----------------------------------------------------------------------------------

    # Radio Button Code---------------------------------------------------------
def drawRadioButtons():
    global window
    var = tkinter.IntVar()
    option1 = tkinter.Radiobutton(window, text ='Average Grayscale           ',variable = var, value = 1,command =  lambda: whichSelected(1))
    option2 = tkinter.Radiobutton(window, text ='Lightness Grayscale         ',variable = var, value = 2, command = lambda: whichSelected(2))
    option3 = tkinter.Radiobutton(window, text ='Luminosity Grayscale      ',variable = var, value = 3, command = lambda: whichSelected(3))
    option4 = tkinter.Radiobutton(window, text ='Invert',variable = var, value = 4, command = lambda: whichSelected(4))

    option1.select() # Sets the first button to clicked
    # Pack Radio Buttons
    option1.pack(anchor = 'sw')
    option2.pack(anchor = 'sw')
    option3.pack(anchor = 'sw')
    option4.pack(anchor = 'sw')
    # End Radio Button code ---------------------------------------------------------

def openImage():
    global window
    global canvas1
    global pic
    global picWidth
    global picHeight
    global tkPic
    global tkPic2
    global picToConvert
    canvas1.delete('all')
    del tkPic
    picToConvert = filedialog.askopenfilename(defaultextension='.jpg') # Used to open the file selected by the user
    pic = Image.open(picToConvert)
    pic.thumbnail((400,320))
    picWidth, picHeight = pic.size # PIL method .size gives both the width and height of a picture
    tkPic = ImageTk.PhotoImage(pic, master = window) # Converts the pic image to a tk PhotoImage
    canvas1.create_image(10,10,anchor='nw', image = tkPic)

def saveImage():
    global pic
    toSave = filedialog.asksaveasfile(mode='w',defaultextension='.jpg')
    pic.save(toSave)

def change_pixel():
    global window
    global canvas1
    global tkPic2
    global pic
    global radio1
    global radio2
    global radio3
    global radio4
    # Treats the image as a 2d array, iterates through changing the
    #values of each pixel with the algorithm for gray

    rgbList = pic.load() #Get a 2d array of the pixels
    for row in range(picWidth):
        for column in range(picHeight):
            rgb = rgbList[row,column]
            r,g,b = rgb # Unpacks the RGB value tuple per pixel
            if radio1 == True:
                grayAlgorithm1 = grayAverage(r,g,b)
                rgbList[row,column] = (grayAlgorithm1, grayAlgorithm1, grayAlgorithm1)
            elif radio2 == True:
                grayAlgorithm1 = lightness(r,g,b)
                rgbList[row,column] = (grayAlgorithm1, grayAlgorithm1, grayAlgorithm1)
            elif radio3 == True:
                grayAlgorithm1= luminosity(r,g,b)
                rgbList[row,column] = (grayAlgorithm1, grayAlgorithm1, grayAlgorithm1) # Gives each pixel a new RGB value
            elif radio4 == True:
                r,g,b= invertRGB(r,g,b)
                rgbList[row,column] = (r, g, b) # Gives each pixel a new RGB value
        # Converting to a tkinter PhotoImage
    del tkPic2
    tkPic2 = ImageTk.PhotoImage(pic, master = window)
    canvas1.create_image(815,170, anchor='e',image = tkPic2)

# Function to create a button, takes the button text and the function to be called on click
def tkButtonCreate(text, command):
    tkinter.Button(window, text = text, command = command).pack()


def main():
    drawRadioButtons()
    tkButtonCreate('Open Image',openImage)
    tkButtonCreate('Convert', change_pixel)
    tkButtonCreate('Save',saveImage)
    cleanUp()
    window.mainloop()
#convertButton = tkinter.Button(window,text = 'Convert', command = change_pixel).pack()

def cleanUp():
    canvas1.delete('all')
main()
