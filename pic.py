from PIL import Image

# RGB values for recoloring.
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)
black = (0, 0, 0)
white = (239, 227, 227)
pink = (233, 91, 233)
babyBlue = (1, 145, 255)
neongreen = (1, 255, 1)
neonorange = (255, 120, 1)


# Import image.
my_image = Image.open("coke.jpg") #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.

recolored = [] #list that will hold the pixel data for the new image.

#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.

def originalfilter():
    for pixel in image_list:
        intensity = pixel[0] + pixel[1] + pixel[2]
        if (intensity < 182) :
            recolored.append(darkBlue)
        elif (182 <= intensity < 364):
            recolored.append(red)
        elif (364 <= intensity , 546):
            recolored.append(lightBlue)
        elif (intensity >= 546):
            recolored.append(yellow)
def cokefilter():
    for pixel in image_list:
        intensity = pixel[0] + pixel[1] + pixel[2]
        if (intensity < 182) :
            recolored.append(black)
        elif (182 <= intensity < 364):
            recolored.append(red)
        elif (364 <= intensity , 546):
            recolored.append(white)
        elif (intensity >= 546):
            recolored.append(yellow)
def cottoncandy():
    for pixel in image_list:
        intensity = pixel[0] + pixel[1] + pixel[2]
        if (intensity < 132) :
            recolored.append(babyBlue)
        elif (132 <= intensity < 324):
            recolored.append(pink)
        elif (324 <= intensity , 496):
            recolored.append(white)
        elif (intensity >= 496):
            recolored.append(yellow)
def neon():
    for pixel in image_list:
        intensity = pixel[0] + pixel[1] + pixel[2]
        if (intensity < 132) :
            recolored.append(babyBlue)
        elif (132 <= intensity < 324):
            recolored.append(neongreen)
        elif (324 <= intensity , 496):
            recolored.append(neonorange)
        elif (intensity >= 496):
            recolored.append(yellow)


print ("Which filter do you want?")
print ("Press 1 for the original")
print ("Press 2 for the coke themed")
print ("Press 3 for the cotton candy theme")
print ("Press 4 for the neon theme")
user_input = input()
if user_input == "1":
    originalfilter()
if user_input == "2":
    cokefilter()
if user_input == "3":
    cottoncandy()
if user_input == "4":
    neon()


# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recoke.jpg", "jpeg") #save the new image as "recolored.jpg"
