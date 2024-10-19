import matplotlib.pyplot as plt

import cv2
from numpy import ndarray


def histogram_creation(img: ndarray)-> tuple:
    """
    Функция создает гистограмму цветного изображения
    :param img:массив из пикселей(цветное изображение в формате rgb)
    :return:гистограмма для каждого канала,содержащая количество пикселей для каждого из 256 уровней яркости
    """
    hist_b = cv2.calcHist([img], [0], None, [256], [0, 256])
    hist_g = cv2.calcHist([img], [1], None, [256], [0, 256])
    hist_r = cv2.calcHist([img], [2], None, [256], [0, 256])
    return hist_r,hist_g,hist_b


def histogram_drawing(hist_r: ndarray, hist_g: ndarray, hist_b: ndarray) -> None:
    """
    Функция рисует гистограмму на основе переданного массива
    :param hist_r: данные для гистограммы красного канала
    :param hist_g: данные для гистограммы зеленого канала
    :param hist_b: данные для гистограммы синего канала
    :return: None
    """
    plt.figure(figsize=(10, 5))
    plt.plot(hist_r, color='red', label='Красный канал')
    plt.plot(hist_g, color='green', label='Зеленый канал')
    plt.plot(hist_b, color='blue', label='Синий канал')
    plt.xlim([0, 256])
    plt.title('Гистограмма изображения')
    plt.xlabel('Интенсивность пикселей')
    plt.ylabel('Количество пикселей')
    plt.legend()
    plt.show()
