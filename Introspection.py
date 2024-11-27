import inspect
"""
"Inspect" - стандартный модуль Python, который предоставляет набор функций для получения информации о живых объектах, 
таких как модули, классы, методы, функции и фреймы. Он полезен для интроспекции — процесс анализа структуры объектов, 
их атрибутов и методов в процессе выполнения программы 
"""

# Пример класса для тестирования
class MyClass:
    def __init__(self, value):
        self.value = value

    def my_method(self):
        return self.value * 2

    @classmethod
    def my_class_method(cls):
        return "Это метод класса."


# Функция интроспекции
def introspection_info(obj):
    info = {
        'type': str(type(obj).__name__),
        'attributes': [],
        'methods': [],
        'module': getattr(obj, '__module__', None),
        'additional_info': {}
    }

    # Получение атрибутов объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    info['attributes'] = attributes

    # Получение методов объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    info['methods'] = methods

    # Для дополнительных данных можно использовать inspect
    try:
        info['additional_info']['doc'] = inspect.getdoc(obj)
        info['additional_info']['is_instance'] = isinstance(obj, object)
    except Exception as e:
        info['additional_info']['error'] = str(e)

    return info


# Пример работы
number_info = introspection_info(42)
print("Информация о числе:")
print(number_info)

# Информация о классе
class_info = introspection_info(MyClass(10))
print("Информация о классе MyClass:")
print(class_info)