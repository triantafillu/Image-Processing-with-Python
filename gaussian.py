# import numpy as np
# def gaussian (img):
#     blur = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])/15.0
#     blur=np.flipud(np.fliplr(blur))
#     output = np.zeros_like(img)
#     image_frame = np.zeros((img.shape[0] + 2, img.shape[1] + 2))
#     image_frame[1:-1, 1:-1] = img
#     for x in range(img.shape[1]):
#         for y in range(img.shape[0]):
#             output[y, x] = (blur * image_frame[y: y + 3, x: x + 3]).sum()
#
#     return output

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
def task1():
  Image.open('img.jpg').show()
  menu()
def task2():
    img = Image.open('img.jpg').convert('RGB')
    arr = np.array(img)
    for j in arr:
        for i in j:
            print(i[0] * 0.3 + i[1] * 0.59 + i[2] * 0.11)
def task3():
  img = Image.open('img.jpg').convert('RGB')
  arr = np.array(img)
  r = [arr[i][j][0] for i in range(len(arr)) for j in range(len(arr[i]))]
  r.sort()
  g = [arr[i][j][1] for i in range(len(arr)) for j in range(len(arr[i]))]
  g.sort()
  b = [arr[i][j][2] for i in range(len(arr)) for j in range(len(arr[i]))]
  b.sort()
  x = [i for i in range(len(r))]
  plo, ax = plt.subplots(3,1)
  ax[0].bar(x, r, color = "red", width = 2)
  ax[1].bar(x, g, color = "green", width = 2)
  ax[2].bar(x, b, color = "blue", width = 2)
  plt.show()
  menu()
def task4():
  img = Image.open('img.jpg').convert('RGB')
  arr = np.dot(np.array(img),[0.3, 0.59, 0.11])
  img = Image.fromarray(arr)
  img.show()
  for i in range(len(arr)):
    for j in range(len(arr[i])):
      if arr[i][j] < 100:
        arr[i][j] = 0
      else:
        arr[i][j] = 255
  img = Image.fromarray(arr)
  img.show()
  menu()


def task5():
    img = Image.open('img.jpg').convert('RGB')
    arr = np.dot(np.array(img), [0.3, 0.59, 0.11])
    img = Image.fromarray(arr)
    img.show()
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] < 100:
                arr[i][j] = 0
            else:
                arr[i][j] = 255
    img = Image.fromarray(arr)
    blur = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])/15.0
    blur=np.flipud(np.fliplr(blur))
    output = np.zeros_like(img)
    image_frame = np.zeros((img.shape[0] + 2, img.shape[1] + 2))
    image_frame[1:-1, 1:-1] = img
    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            output[y, x] = (blur * image_frame[y: y + 3, x: x + 3]).sum()
    plt.imshow(output)
    menu()


def menu():
  inp = int(input("Enter number of task: "))
  if inp == 1:
    task1()
  elif inp == 2:
    task2()
  elif inp == 3:
    task3()
  elif inp == 4:
    task4()
  elif inp == 5:

    task5()

menu()