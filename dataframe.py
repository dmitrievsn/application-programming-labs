import cv2
import pandas as pd
import matplotlib.pyplot as plt

def create_dataframe(annotation_file: str) -> pd.DataFrame:
    """
    Функция создает DataFrame из CSV файла с аннотацией.
    :param annotation_file: csv файл с аннотацией
    :return: DataFrame с абсолютными и относительными путями
    """
    df = pd.read_csv(annotation_file)
    df.columns = ['Относительный путь к файлу', 'Абсолютный путь к файлу']
    return df


def add_image_dimensions(df: pd.DataFrame) -> pd.DataFrame:
    """
    Функция добавляет информацию о высоте, ширине и глубине изображений в DataFrame.
    :param df: DataFrame с аннотацией изображений
    :return: DataFrame с добавленными колонками для высоты, ширины и глубины
    """
    heights = []
    widths = []
    depths = []
    for abs_path in df['Абсолютный путь к файлу']:
        try:
            img = cv2.imread(abs_path)
            if img is not None:
                heights.append(img.shape[0])
                widths.append(img.shape[1])
                depths.append(img.shape[2])
            else:
                heights.append(None)
                widths.append(None)
                depths.append(None)
        except Exception as e:
            heights.append(None)
            widths.append(None)
            depths.append(None)
            print(f"Ошибка при обработке изображения {abs_path}: {e}")
    df['Высота'] = heights
    df['Ширина'] = widths
    df['Глубина'] = depths
    return df


def compute_image_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Вычисляет статистическую информацию для столбцов с размерами изображений.
    :param df: DataFrame с аннотацией изображений, содержащий колонки 'Ширина', 'Высота', 'Глубина'
    :return: DataFrame со статистической информацией
    """
    required_columns = ['Ширина', 'Высота', 'Глубина']
    if not all(col in df.columns for col in required_columns):
        raise ValueError(f"DataFrame должен содержать колонки: {', '.join(required_columns)}.")
    stats = df[required_columns].describe()
    return stats


def filter_images_by_size(df: pd.DataFrame, max_width: int, max_height: int) -> pd.DataFrame:
    """
    Фильтрует DataFrame по максимальным значениям ширины и высоты изображений.
    :param df: DataFrame с аннотацией изображений, содержащий колонки 'Ширина' и 'Высота'
    :param max_width: Значение максимальной ширины, заданное пользователем через терминал
    :param max_height: Значение максимальной высоты, заданное пользователем через терминал
    :return: Отфильтрованный DataFrame
    """
    required_columns = ['Ширина', 'Высота']
    if not all(col in df.columns for col in required_columns):
        raise ValueError(f"DataFrame должен содержать колонки: {', '.join(required_columns)}.")
    filtered_df = df[(df['Ширина'] <= max_width) & (df['Высота'] <= max_height)]
    return filtered_df


def add_area_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    Добавляет новый столбец с площадью изображения в DataFrame.
    :param df: DataFrame с аннотацией изображений, содержащий колонки 'Ширина' и 'Высота'
    :return: DataFrame с добавленным столбцом 'Площадь'
    """
    required_columns = ['Ширина', 'Высота']
    if not all(col in df.columns for col in required_columns):
        raise ValueError(f"DataFrame должен содержать колонки: {', '.join(required_columns)}.")
    df['Площадь'] = df['Ширина'] * df['Высота']
    return df


def sort_by_area(df: pd.DataFrame) -> pd.DataFrame:
    """
    Сортирует DataFrame по площади изображений от меньшего к большему.
    :param df: DataFrame с колонкой 'Площадь'
    :return: Отсортированный DataFrame
    """
    if 'Площадь' not in df.columns:
        raise ValueError("DataFrame должен содержать колонку 'Площадь'.")
    sorted_df = df.sort_values(by='Площадь')
    return sorted_df


def plot_area_distribution(df: pd.DataFrame):
    """
    Строит гистограмму распределения площадей изображений.
    :param df: DataFrame с колонкой 'Площадь'
    """
    if 'Площадь' not in df.columns:
        raise ValueError("DataFrame должен содержать колонку 'Площадь'.")
    plt.figure(figsize=(10, 5))
    plt.hist(df['Площадь'], bins=25, color='green', edgecolor='black')
    plt.title('Распределение площадей изображений')
    plt.xlabel('Площадь')
    plt.ylabel('Количество изображений')
    plt.show()