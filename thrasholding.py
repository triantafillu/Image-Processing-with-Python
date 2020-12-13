#Binarizationn
def thresholding(image):
    thresh = 127 #50% of 255
    #Binary mask:
    #if > 127 - white
    #if < 127 - black
    binary = (image>thresh)
    print(binary)
    return binary

