import argparse


def value_input() -> argparse.Namespace:
    """
    Функция, позволяющая осуществить ввод ключевого слова, пути к директории, кол-ва изображений, пути к файлу для аннотации
    :return: аргументы
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir_name', type=str, help='Путь к директории')
    parser.add_argument('-f', '--annotation_file', type=str, help='Путь к файлу для аннотации')
    parser.add_argument('-mw', '--max_width', type=int, help='Максимальная ширина')
    parser.add_argument('-mh', '--max_height', type=int, help='Максимальная высота')
    args = parser.parse_args()
    return args