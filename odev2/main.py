import cv2
import numpy as np

camera = cv2.VideoCapture(0)
sinirlar = [
    ([0, 0, 0], [180, 255, 255]),
    ([0, 0, 0], [5, 255, 255])]
while True:
  ret, frame = camera.read()
  if not ret:
      break

  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  for (alt_deger, ust_deger) in sinirlar:
    alt_deger = np.array(alt_deger, dtype="uint8")
    ust_deger = np.array(ust_deger, dtype="uint8")
  mask = cv2.inRange(hsv, alt_deger, ust_deger)
  red_frame = cv2.bitwise_and(frame, frame, mask=mask)

  cv2.imshow('Orginal Ekran(Kapatmak Icin 1 e basiniz.', frame)
  cv2.imshow('Kirmizi Duyarli Ekran (Kapatmak Icin 1 e basiniz.)', red_frame)

  if cv2.waitKey(1) & 0xFF == ord('1'):
      break
camera.release()
cv2.destroyAllWindows()
