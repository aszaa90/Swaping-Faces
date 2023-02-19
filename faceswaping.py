import numpy as np
import cv2

image = np.array([
[0,0,0],
[0,255,0],
[0,0,0],
[0,255,0],
[0,0,0],
], dtype=np.uint8)

image = cv2.resize(
    image,
    (90,150),
    interpolation=cv2.INTER_NEAREST)
cv2.imwrite('8.jpg', image)

