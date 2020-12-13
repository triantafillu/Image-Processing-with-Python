import matplotlib.pyplot as plt

#Used to display an image
def show_image(image, title):
    plt.imshow(image, cmap='gray') #cmap - ignored for RGB(A), is needed for balck/white binarization
    #Add title
    plt.title(title)
    #Don't show axis
    plt.axis('off')
    plt.show()