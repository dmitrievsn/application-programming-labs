import os


from image import *
from input import value_input
from hist import *


def main():
    path_im=value_input().path_image
    path_new_im=value_input().path_new_image
    try:
        if not os.path.exists(path_im):
            raise FileNotFoundError(f"Файл не найден: {path_im}")
        img = cv2.imread(path_im)
        if img is None:
            raise ValueError("Не удалось загрузить изображение. Проверьте путь.")
        dimensioning(path_im)
        hist_r,hist_g,hist_b=histogram_creation(img)
        histogram_drawing(hist_r,hist_g,hist_b)
        new_im=grayscale_image(img)
        save_grayscale_image(new_im, path_new_im)
        image_output(img,new_im)
    except Exception as e:
        print(f'Error: {e}')


if __name__ == "__main__":
    main()
