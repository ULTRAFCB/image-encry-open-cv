import cv2
import numpy as np


def main():
    # 1.Load image
    img_src = cv2.imread(r"Absolute Address")
    width, height, deep = img_src.shape

    # 2.creat key
    img_key = np.random.randint(0, 256, size=[width, height, deep], dtype=np.uint8)

    # 3.img encry
    imp_ency = cv2.bitwise_xor(img_src, img_key)

    # 4.img encry
    img_decrypt = cv2.bitwise_xor(imp_ency, img_key)

    # 5.show result
    cv2.imshow("img_src", img_src)
    cv2.imshow("img_key", img_key)
    cv2.imshow("imp_ency", imp_ency)
    cv2.imshow("img_decrypt", img_decrypt)

    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
