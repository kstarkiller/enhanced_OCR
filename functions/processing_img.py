import cv2

def processing_img(image_path):
    # read the image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # negative image
    img = cv2.bitwise_not(img)

    # resize the image
    img = cv2.resize(img, (48, 48))

    # normalize the image
    img = img / 255.0

    return img