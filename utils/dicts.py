def get_val(collection, key, default=None):
    """
    Функция возвращает значение из словаря по переданному ключу,
    если ключ существует. В ином случае возвращается значение default
    :param collection: Исходный словарь
    :param key: Ключ значения словаря
    :param default: Значение по умолчанию
    :return: Значение по ключу или значение по умолчанию
    """
    if collection == {}:
        return default
    return collection[key]
