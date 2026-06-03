import cv2

img = cv2.imread("stuff.jpg")

cv2.line(
    img,
    (50, 50),
    (500, 50),
    (0, 255, 0),
    3
)

cv2.rectangle(
    img,
    (100, 100),
    (300, 250),
    (255, 0, 0),
    3
)

cv2.circle(
    img,
    (320, 240),
    50,
    (0, 0, 255),
    3
)

cv2.putText(
    img,
    "Harsh",
    (50, 450),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 255, 255),
    2
)

resized_img = cv2.resize(img, (320, 240))

cropped_img = img[100:300, 200:500]

print("Original:", img.shape)
print("Resized:", resized_img.shape)
print("Cropped:", cropped_img.shape)

cv2.imshow("Original with Shapes", img)
cv2.imshow("Resized", resized_img)
cv2.imshow("Cropped", cropped_img)

cv2.imwrite("Outputs/final_image.jpg", img)
cv2.imwrite("Outputs/resized_image.jpg", resized_img)
cv2.imwrite("Outputs/cropped_image.jpg", cropped_img)

cv2.waitKey(0)

cv2.destroyAllWindows() 