import cv2
import numpy as np
import matplotlib.pyplot as plt


foto = cv2.imread('.\image\deneme3.jpeg',0)
print(foto.shape)

height, width = foto.shape


histogram = np.zeros(256)
print(histogram)

# Her bir piksel için yoğunluğunu histogramda arttırma
for i in range(height):
    for j in range(width):
        histogram[foto[i, j]] += 1

# Histogramı çiz
plt.plot(histogram)
plt.show()
print(histogram)
cv2.imshow("deneme2",foto)
cv2.waitKey()