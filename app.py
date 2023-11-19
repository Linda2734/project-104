import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "sun", (20,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "mercury", (100,250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "venus", (200,250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "earth", (300,250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "mars", (400,250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "jupiter", (500,250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
# cv2.putText(img, "saturn", (20,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
# cv2.putText(img, "uranus", (20,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
# cv2.putText(img, "neptune", (20,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))

cv2.imshow("output window", img)
cv2.waitKey(4000)