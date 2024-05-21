def recognize(img_array):
    # загрузить модель, предобработать изоброжение (которое сюда пришло в виде массива), через модель понять какой лейбл
    label = 'healthy_potato'
    return label


if __name__ == "__main__":
    img_array = []  # читаем изображение нужными средствами
    label = recognize(img_array)
    print(label)
