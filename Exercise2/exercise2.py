import cv2

img = cv2.imread("squirrel_cls.jpg")

top_row = cv2.hconcat([img, img])

bottom_row = cv2.hconcat([img, img])

tiled_img = cv2.vconcat([top_row, bottom_row])

print("Original:", img.shape)
print("Tiled:", tiled_img.shape)

cv2.imshow("Tiled Image", tiled_img)

cv2.imwrite("Outputs/tiled_image.jpg", tiled_img)

cv2.waitKey(0)

cv2.destroyAllWindows()