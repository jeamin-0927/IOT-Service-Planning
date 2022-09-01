import cv2

img = cv2.imread('bts.jpeg')
img2 = cv2.resize(img, (600, 400))

gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

cv2.imshow('origin', img2)
cv2.imshow('gray', gray)

while 1:
    if cv2.waitKey() == ord('q'):
        break

cv2.imwrite('gray.jpg', gray)

cv2.destroyAllWindows()
