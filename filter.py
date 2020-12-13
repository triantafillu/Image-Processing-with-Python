import numpy as np

#Puts a filter on every pixel
def filter(image, filter):
    filtered_image = np.zeros_like(image)

    # v1 v2 v3
    # v4 v5 v6
    # v7 v8 v9
    v1 = filter[0, 0]
    v2 = filter[0, 1]
    v3 = filter[0, 2]
    v4 = filter[1, 0]
    v5 = filter[1, 1]
    v6 = filter[1, 2]
    v7 = filter[2, 0]
    v8 = filter[2, 1]
    v9 = filter[2, 2]

    #Create a frame from zeroes around the image
    framed_image = np.zeros((image.shape[0] + 2, image.shape[1] + 2))
    framed_image[1:-1, 1:-1] = image

    # j-1,i-1  j-1,i  j-1,i+i
    # j,i-1     j,i   j,i+1
    # j+1,i-1  j+1,i  j+1,i+1
    for i in range(image.shape[1]):
        for j in range(image.shape[0]):
            filtered_image[j,i] = framed_image[j-1,i-1]*v1 + framed_image[j-1,i]*v2 + framed_image[j-1,i+1]*v3 + framed_image[j,i-1]*v4 + framed_image[j,i]*v5 + framed_image[j,i+1]*v6 + framed_image[j+1,i-1]*v7 + framed_image[j+1,i]*v8 + framed_image[j+1,i+1]*v9

    return filtered_image