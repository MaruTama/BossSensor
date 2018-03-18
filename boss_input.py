# -*- coding: utf-8 -*-
import os

import numpy as np
import cv2

IMAGE_SIZE = 64

# 入力画像を入力層のサイズに合わせて成形する
def resize_with_pad(image, height=IMAGE_SIZE, width=IMAGE_SIZE):

    def get_padding_size(image):
        h, w, _ = image.shape
        longest_edge = max(h, w)
        top, bottom, left, right = (0, 0, 0, 0)
        if h < longest_edge:
            dh = longest_edge - h
            top = dh // 2
            bottom = dh - top
        elif w < longest_edge:
            dw = longest_edge - w
            left = dw // 2
            right = dw - left
        else:
            pass
        return top, bottom, left, right

    top, bottom, left, right = get_padding_size(image)
    BLACK = [0, 0, 0]
    constant = cv2.copyMakeBorder(image, top , bottom, left, right, cv2.BORDER_CONSTANT, value=BLACK)

    resized_image = cv2.resize(constant, (height, width))

    return resized_image



images = []
labels = []
# dataディレクトリ内から全画像とラベルを取得する
def traverse_dir(path):
    for file_or_dir in os.listdir(path):
        abs_path = os.path.abspath(os.path.join(path, file_or_dir))
        print(abs_path)
        if os.path.isdir(abs_path):  # dir
            # 再帰してファイルまで探す
            traverse_dir(abs_path)
        else:                        # file
            if file_or_dir.endswith('.jpg'):
                image = read_image(abs_path)
                images.append(image)
                labels.append(path)
                # ちゃんとパディングされているか確認する
                # pad_dir = os.path.abspath(os.path.join(path, "paded"))
                # # フォルダが無い時に作成する
                # if not os.path.exists(pad_dir):
                #     os.mkdir(pad_dir)
                # pad_path = os.path.join(pad_dir,file_or_dir)
                # print(pad_path)
                # cv2.imwrite(pad_path, image)

    return images, labels

# 画像を読む込む
def read_image(file_path):
    # 連番画像ファイルを読み込む
    image = cv2.imread(file_path)
    image = resize_with_pad(image, IMAGE_SIZE, IMAGE_SIZE)

    return image

# データの取得
def extract_data(path):
    images, labels = traverse_dir(path)
    images = np.array(images)
    # ラベルにbossが含まれているときに1にする。その他は0
    labels = np.array([0 if label.endswith('boss') else 1 for label in labels])

    return images, labels
