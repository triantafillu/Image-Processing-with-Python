import numpy as np

#Function used to calculate the matrix of brightness of the image
def calculate_brightness(image):
    if image.shape[-1]!=3:
        raise Exception("The image is not RGB")
    # Y: = 0.3 * R + 0.59 * G + 0.11 * B
    coef=np.array([0.3, 0.59, 0.11])
    #Multiply matrices
    brightness = image @ coef
    return brightness







