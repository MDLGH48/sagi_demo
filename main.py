import numpy as np
import cv2


def numpy_test(x):
    rand_num = np.random.randint(x)
    return f"numpy test... your random number is = {rand_num}"


def cv2_test():
    # https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html
    test_img = cv2.imread('test_image.png', 0)
    cv2.imshow('test_image_window', test_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("open cv works")


if __name__ == "__main__":
    print(numpy_test(3))
    cv2_test()
