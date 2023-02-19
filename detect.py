import cv2
image = cv2.imread('marriage.jpg')
haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def apply(resized1, face2):
    resized1_h, resized1_w, _ = resized1.shape
    face2[:resized1_h, :resized1_w] = resized1
    return face2


def resize_to_fit(face1, face2):
    face1_h, face1_w, _ = face1.shape
    face2_h, face2_w, _ = face2.shape
    factor = min(face2_h / face1_h, face2_w / face1_w)
    return cv2.resize(face1, None, fx=factor, fy=factor)


def get_face_selector(rectangle):
    x, y, w, h = rectangle
    return(slice(y, y+h), slice(x, x+w))


def swap_faces(image, haar_cascade):
    rectangles = haar_cascade.detectMultiScale(
        image, scaleFactor=1.1)

rectangles = 
for (rectangle1, rectangle2) in rectangles:
    mask1 = get_face_selector(rectangle1)
    mask2 = get_face_selector(rectangle2)
    face1 = image[mask1]
    face2 = image[mask2]
    resized1 = resize_to_fit(face1, face2)
    resized2 = resize_to_fit(face2, face1)
    image[mask1] = apply(resized2, face1)
    image[mask2] = apply(resized1, face2)


cv2.imwrite("out.jpg", image)
