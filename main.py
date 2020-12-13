from show_image import *
from calculate_brightness import *
from thrasholding import *
from negative import *
from filter import *
from print_menu import *

#Load image
org_image = plt.imread('img.jpg')
gray_image=calculate_brightness(org_image)

# 1. Display the original image
# 2. Display the matrixes of brightness for the original image
# 3. Display the histogram
# 4. Binarization
# 5. Convert to grayscale
# 6. Negative
# 7. Use mask 'South'
# 8. Use mask 'South-East'
# 9. Exit
loop=True
while loop:
    print_menu()
    print("Choose an option: ")
    choice = int(input())
    if choice==1:
        show_image(org_image, 'Original')
    elif choice==2:
        print("\nRed:")
        print(org_image[:,:,0])
        print("\nGreen:")
        print(org_image[:,:,1])
        print("\nBlue:")
        print(org_image[:,:,2])
        print("\nBrightness:")
        print(calculate_brightness(org_image))
    elif choice==3:
        fig, axs = plt.subplots(2, 2)
        axs[0, 0].hist(org_image[:,:,0].ravel(), bins = 256, color = "red")
        axs[0, 0].set_title('Red')
        axs[0, 1].hist(org_image[:,:,1].ravel(), bins = 256, color = "green")
        axs[0, 1].set_title('Green')
        axs[1, 0].hist(org_image[:,:,2].ravel(), bins = 256, color = "blue")
        axs[1, 0].set_title('Blue')
        axs[1, 1].hist(gray_image.ravel(), bins = 256, color = "gray")
        axs[1, 1].set_title('Brightness')

        for ax in axs.flat:
            ax.label_outer()

        plt.show()
    elif choice==4:
        binary=thresholding(gray_image)
        show_image(binary, 'Binary')
    elif choice==5:
        print("\nGreyscale:")
        print(gray_image)
        show_image(gray_image, 'Grayscale')
    elif choice==6:
        negative = negative(org_image)
        show_image(negative, 'Negative')
    elif choice==7:
        filter_south = np.array([[-1,-1,-1],
                                [ 1,-2, 1],
                                [ 1, 1, 1]])
        show_image(filter(gray_image, filter_south), 'South')
    elif choice==8:
        filter_south_east = np.array([[-1,-1,1],
                                     [-1,-2,1],
                                     [1,1,1]])
        show_image(filter(gray_image, filter_south_east), 'South-East')
    elif choice==9:
        loop=False

    else:
        print('There is no such option. Please, try again')



