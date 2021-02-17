""""""
"""
isinstance(obj, type) - определяет является ли объект obj типом type
dir(obj) - выводит список методов применимых для объекта obj
a.extend(c) - добавляет в список а содержимое списка с
a.pop(c) - удаление элемента по индексу с и возвращает значение
a.remove(c) - удаление элемента по значению с
a.count(c) - называет количество элементов с
a.insert(b, c) - вставка элемента c в индекс b со сдвигом всех существующих элементов начиная с b
a.reverse() - разворачивает список
reversed(a) - разворачивает a преобразовывая в иттератор. требуется использовать преобразование в последовательность
a = b[c:d:e] - a = срез из списка b с начальным индексом c, конечным индексом(не включённым в срез) d и шагом e
               отрицательный шаг означает отсчёт с конца
a.sort() - сортировка последовательности a
b = sorted(a) - запись сортированных элементов последовательности a в список b
a = b.join(c) - собрать строку a из элементов последовательности c вставив между элементами разделительную строку b
a = b.upper() - строка а приравнивается к строке b в ВЕРХНЕМ регистре
a = b.lower() - строка а приравнивается к строке b в нижнем регистре
a = b.title() - строка а получает значение строки b, но в a все слова начинаются с большой буквы
                (остальные буквы маленькие)
a = b.capitalize() - строка а получает значение строки b, но в a только первая буква строки заглавная
a = b.replace(x, y, z) - возвращает строку b с подстроками x заменёнными на подстроки y z раз
к строкам применимы все методы кортежей
f'{a:arg}' - добавить в строкку переменную а с форматированием arg
"""