#!/usr/bin/env python3
"""Przeglądarka obrazów OpenCV"""
# coding: utf-8
# pylint: disable=line-too-long
import os
import argparse
import cv2


PARSER = argparse.ArgumentParser()
PARSER.add_argument("-f", "--folder", required=True,
                    help="Path to the image folder")
ARGS = PARSER.parse_args()


if __name__ == "__main__":
    IMAGES_LIST = []
    for file in os.listdir(ARGS.folder):
        if (file.endswith(".jpg")) or (file.endswith(".png")) or (file.endswith(".jpeg")):
            IMAGES_LIST.append(os.path.join(ARGS.folder, file))
    # print("Images List: ", IMAGES_LIST)

    IMAGE_NUM = 0
    NAME = ("Image Viewer "+str(IMAGE_NUM))
    IMG = cv2.imread(IMAGES_LIST[IMAGE_NUM])
    cv2.imshow(NAME, IMG)
    print("\nSterowanie: \nd - następny obraz\na - poprzedni obraz\nesc - zamyka program")

    while True:
        # The function waitKey waits for a key event infinitely (when delay<=0)
        k = cv2.waitKey(100)

        if k == ord('d') and (IMAGE_NUM != len(IMAGES_LIST)-1):
            cv2.destroyAllWindows()
            IMAGE_NUM += 1
            NAME = ("Image Viewer "+str(IMAGE_NUM))
            IMG = cv2.imread(IMAGES_LIST[IMAGE_NUM])
            cv2.imshow(NAME, IMG)

        elif (k == ord('a')) & (IMAGE_NUM > 0):
            cv2.destroyAllWindows()
            IMAGE_NUM -= 1
            NAME = ("Image Viewer "+str(IMAGE_NUM))
            IMG = cv2.imread(IMAGES_LIST[IMAGE_NUM])
            cv2.imshow(NAME, IMG)

        elif k == 27:  # escape key
            break


cv2.destroyAllWindows()
