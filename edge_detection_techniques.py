# -*- coding: utf-8 -*-
"""Edge detection techniques.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HgZwF-mvjR9X-OGfKSSCOhyz9vCxlLBz
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# loading image
img0 = cv2.imread('/content/I2.jpg',)

# converting to gray scale
gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)

# remove noise
img = cv2.GaussianBlur(gray,(3,3),0)
#Sobel edge detection
# convolute with proper kernels
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)  # x
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)  # y

plt.subplot(2,2,1),plt.imshow(img, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()

#Canny edge detection
edges = cv2.Canny(img,10,20)
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Canny-Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()

"""Sobel Edge Detection:

Sobel edge detector is a gradient based method based on the first order derivatives. It calculates the first derivatives of the image separately for the X and Y axes.

The operator uses two 3X3 kernels which are convolved with the original image to calculate approximations of the derivatives - one for horizontal changes, and one for vertical. The picture below shows Sobel Kernels in x-dir and y-dir:

![SobelKernelX.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHkAAABTCAIAAAA0rz9OAAAAA3NCSVQICAjb4U/gAAAAGXRFWHRTb2Z0d2FyZQBnbm9tZS1zY3JlZW5zaG907wO/PgAABNhJREFUeJztnb9L61AUx6+PCCJFJEOknUpaOoqx/gHtKBSxIA7ioKmzU/IfZGqdHQrWf0CsQ0kWwQ6O1oqIk4J0MBgklFJEsNA3FEpem9bm3twb6zufqTm5Ob3nq94fyclxptvtIoAJf4LuwH8EaM0O0JodoDU7QGt2uGutqurMELVajXHnpgVJkga0mp2dHW7GuV5s2zZCSFEUpzESidDo6C/g8PDw8fGxf3h+ft5oNFzadd2QZZnjONdTwLeMUo/FeG2aZjqd9tGVqqq5XC6bzfriE68PGBe6jyE+YhjG9va2IAi+eEskEtVqNZlMIoQKhYIkSfV63RfPE0ISDsXfa9M0JUkqFovz8/O+OMzlcvF4vCc0QkhV1YeHB8MwfHH+LeThUNQ6HA7X6/VyuezXpFqpVKLRqNPC8/zZ2ZkvznvEYrFRp8jDmab1tWVZ8XjcaYlEIpVKJaj+eGVqtDZNEyE0MFAuLi5+fHwE1CPPTI3Wr6+vrvbPz0/GPcFmarR2pdlsBt0FD3he8327U49EIuFwGLc/49wOG1ut1tzcnO/fRQlvWtdqtYODg/FtVldXT05OCLrkTu/nZ1nWgJ1kQZlOp517a4SQbdtLS0tOSygUen5+xv4KJ960TiaTjPcOTgRBeHp6clra7XYmk8F2eHV1NWCJxWJ+KTvMNI3XmUzm/v7eabEsa2trK6j+eIWR1u12m9yJpmmWZfUnDFVVRVFcX18n9+wVvHDo3g/JZrMvLy93d3cIIUmSotHo8fEx9swZDoer1aqiKGtra7Zt27ZN7+/dFcJw6GpdLpf9dZhMJocHWWYQhjNN4zUDFhYW6DkHrf+B6ioLtGYHaM0O0JodoDU7QGt2gNbsAK3ZQXffaBhGsVhsNpuNRmN5eZl8G2ma5s7OTn+P7vu+dDyk4XjK3PGEruuyLPcPRVEUBIHQZygUurm56X3O5/MrKyuEDidn8nBGqUdR61Qq5TzUdR0hpCgKtkNZlgfE5ThO13Vsh56YPJwAcsyur6+daWC9m5+Xl5fYDoPNDyEPh6LWPM8PP3tttVrYDoPNDyEPh+Lc+Pb25jzs3eNPpVJ43kblhww8FaMHeTjs1nyapnEcp2ka3uU/LT8EIxzqeao9DMO4uLjQdd3fdIag8kPwwnHXmud5nuddT+Hlh+zt7ZVKJZJngz8qP2R8OKPUc9daEIRQKDRsx8sPkSRJUZT9/f3xF47n5+SHfBvOKPWov8Mhy3I+n3cuS7FdCYKwubk5YHHuL8gRRXF8g0nCCeYdjkKhwPO8qqp9S7FYxPYWeH4IYTgU50bDMI6OjjKZTC6X61ls2x41DUyCpmmJRKJWq/VeLWCcH0IeDkWtNzY2Op1OqVRyGvP5PLbDYPNDyMOhqPXX15fvPgPMDyEPB+5f/wPkh7AD8kN+CaA1O0BrdoDW7ACt2QFaswO0ZgfUD8HsA8aFUD/EG1A/hAVQPwTqh9AB6ocwAuqHsOOn5YdgMDVauwL1Q6B+iDtQPwTqh7gB9UPYEXh+CCFQPwQHqB9CHagfwg6oH+InkB/CDsgP+SWA1uwYOTd2Op1CoeC07O7u0th8/wJOT0/f39/7h7e3t+7tRmXPD7dk9obs1CGK4oBWru8VzHTh/9yxAsZrdoDW7ACt2QFas+MvU2ABNuC8w+YAAAAASUVORK5CYII=)

![SobelKernelY.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIoAAABTCAIAAADP1AjUAAAAA3NCSVQICAjb4U/gAAAAGXRFWHRTb2Z0d2FyZQBnbm9tZS1zY3JlZW5zaG907wO/PgAABOdJREFUeJztnT9L+04cx88fEUSKSIaUdiqtDyBRH4AZhSItiENx0NbZKX0GnVJHcShYwbmoQ2lGfQBWxUEcFMShwSBBShHBQn9DoYQ0zbdJ7l/Pe03mw5H35+79vW/uzuTj3GAwABxa+Y90Ahw/uD1Uw+2hGm4P1XB7qMbDnnK5PDdGu93GnxyTKIriGtv5+flJjYXxkG3bAABN05zBZDIJPdG/yeHh4dPT0+jy4uLi/f19UmMPewAAgiBUq1X4qXEA2N/fd17atn1+fj6pMY5nj2maqqpiEHJhGEY+n1dVNZPJ5PN5/AlE77j37IGIYRg7OzuSJKEWGtdtNBqXl5fDy0wmE4/HPz4+cCYQveMIZ49pmoqi1Gq1xcVFdCqT0HX99PR0dHl8fGxZVrlcxiANs+ODMYrFoiAI43FP0un0P9vIsjxNsxD43FYQhFwu54wAAGRZxiA9YpqO+482s/seURS/vr5cwW63SySZ0CB/9pDC9ZgZ7ts2NjbIZBMWZmePi0qlIghCpVIhnUgwmJ09TgzDuLq6arVaiUSCdC7B+BOzZ29vr16vb25ukk4kMMFmj6qqzgMJAIBt2/F43BmJxWKvr68QUoOkriiKpmmuvToe6egEs+f6+toVyWQyiMyAol4qlQqFwmi7YxhGuDlEquMs/+dWrVZFUXRuRWu1GsF8QoBpadDr9fAIjTAM4+joKJvNlkqlYcS2bVEUMacRseNo7cnn829vbw8PDwAARVFSqdTJyQme5dPW1la/36/X686grusYpAG8jqO1Z3QiiZ/f319S0gBex6M+e5aWlqDkMXPqeKSj2nN/fw8lj5lTxyPN8sqNAbg9VMPtoRpuD9Vwe6iG20M13B6qQXhqYJpmoVBYX1+3bdu2bcwnCIyoB313ZHpisdjt7e3wZ13XIb4lw5K6/2ijsqdYLLpyEgSh1WpFvC176mRepGo2m6lUyhkRRbHRaCCSY1UdlT2WZa2srDgjyWSy2WwikmNVHYk9pmkCAFyvFy8vL39/f6OQY1gdiT2dTscz/vPzg0KOYXV8+57xV2pxMqPqHvaIohjxd/Ken9J1u92FhYUot2VS3X+0PeyRJCkWi4XODwAw/KW6ZVmuOJ4vSWZL3X+0Pex5fn72+dpxSiRJenl5cUZ6vV42m414W/bU/Ucb1bMnm80+Pj46I5ZlbW9vI5JjVj3oPnZKOp2O82BD0zREX2DNurr/aKM6Ek0kEjc3N5qmjY4Fsb3ry5R6UD85cPmjHy+yAbeHarg9VMPtoRpuD9Vwe6iG20M13B6q4fZQDbP13IgXcwO8npuPKNliboDXc/OBYDE3QFU9t2lAV89tEqiLuU0Jr+fmDRvF3ACrFanYKOYG/sjCekaLuQFWZ4+T2S3mBkLY889q/clkEtFAhJOGVcyNSMeD2dNutw8ODvzbrK6uOhe1sAgnDaWYW2j16ASzZ21tjVQhjhDSsIq5hVOHArNLAwaKuQFW67lRUswNRO940H1sIHK5nCzLQyFZlnO5XKfTgXJnfwTB45+drusYpIdM33EyryEOIVXPjWwxN0BPPTcOUrg9VMPtoRpuD9V4Lw36/b7rb8ft7u7O4pkVhZydnX1+fo4u7+7u/Fp7LvXGm2ErqcE86XTaNbY+C+u5Af+L8xTDnz1Uw+2hGm4P1XB7qOZ/FQIhw0mlYOAAAAAASUVORK5CYII=)

Canny Edge Detection:

Edge detection is one of the fundamental operations when we perform image processing. It helps us reduce the amount of data (pixels) to process and maintains the structural aspect of the image. We're going to look into many people think it as the ultimate edge detectorm Canny Edge Detection. With this detector, we get clean, thin edges that are well connected to nearby edges.

The canny edge detector is a 4-step detection process. The steps are:

Noise Reduction - 5x5 Gaussian filter
Calculating gradients - Finding Intensity Gradient of the Image
Nonmaximum suppression - upper threshold
Thresholding with hysterysis - upper/lower threshold
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# loading image
img0 = cv2.imread('/content/I3.jpg',)

# converting to gray scale
gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)

# remove noise
img = cv2.GaussianBlur(gray,(3,3),0)
#Sobel edge detection
# convolute with proper kernels
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)  # x
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)  # y

plt.subplot(2,2,1),plt.imshow(img, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()
#Canny edge detection
edges = cv2.Canny(img,10,20)
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Canny-Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()

import cv2
import numpy as np
from matplotlib import pyplot as plt

# loading image
img0 = cv2.imread('/content/I4.jpg',)

# converting to gray scale
gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)

# remove noise
img = cv2.GaussianBlur(gray,(3,3),0)
#Sobel edge detection
# convolute with proper kernels
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)  # x
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)  # y

plt.subplot(2,2,1),plt.imshow(img, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()
#Canny edge detection
edges = cv2.Canny(img,10,20)
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Canny-Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()