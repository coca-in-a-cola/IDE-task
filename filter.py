from PIL import Image
import numpy as np

def convert_image_to_mosaic(image, size, gradation_step):
    """
    Конвертирует изображение

    // >>> convert_image_to_mosaic(np.array(Image.open("image.jpg")), 12, 8)
    Вернёт ЧБ мозаику с картинки image.jpg как массив. \
    С размером "пикселя" 12х12 реальных и 8-ю градациями серого \
    см. в Первую и последнюю картинку в README

    :param image: numpy массив пикселей изображения
    :param size: размер блока
    :param gradation_step: количество градаций серого
    :return: обработанный numpy массив пикселей изображения
    """
    for x in range(0, len(image), size):
        for y in range(0, len(image[0]), size):
            image[x:x + size, y:y + size] = get_average_brightness(
                image[x:x + size, y:y + size], size, gradation_step)
    return image


def get_average_brightness(block, size, gradation_step):
    """
    Ищет среднее ЧБ значение на участке пикселей

    :param block: участок пикселей, в котором будем считать среднее
    :param size: тот самый шаг, размер одного будущего пикселя
    :param gradation_step: кол-во градаций серого
    :return: значение от 0 до 255 - яркость пикселя
    """
    average_color = (block[:size, :size].sum() / 3) // size ** 2
    return int(average_color // gradation_step) * gradation_step


def main():
    image_file = Image.open(input("Введите имя файла, которое хотите конвертировать: "))
    block_size = int(input("Введите размер блока: "))
    gradations_count = int(input("Введите количество градаций серого: "))
    image = np.array(image_file)
    gradation_step = 255 // gradations_count

    res = Image.fromarray(convert_image_to_mosaic(image, block_size, gradation_step))
    res.save(input("Введите имя файла, в которой хотите сохранить результат: "))


if __name__ == '__main__':
    main()
