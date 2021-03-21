""""""
# ПЕРЕГРУЗКА ОПЕРАТОРОВ=================================================================================================
r"""
Изменение логики работы операторов языка через спец методы.
    Эти методы отличаются наличием двух подчёркиваний в начале и конце имени.

Перегружаемые операторы:
    + > < >= <= == != += -=

Методы для реализации перегрузки операторов:
    __init__()      - конструктор экземпляра класса, срабатывает при создании экземпляра класса
                        return не нужен
    __del__()       - деструктор, срабатывает при удалении
                        return не нужен
    __setattr__()   - срабатывает при присвоении значения атрибуту
                        для создания атрибута с именем полученным из переменной attr используется конструкция
                        self.__dict__[attr] = value
                        return не нужен
    __getitem__()   - срабатывает при извлечении элемента по индексу
                        для использования требуется атрибут класса список
                        в return возвращаем элемент этого атрибута с указанным индексом. Пример:
                                class Class2:
                                    def __init__(self, *args):
                                        self.my_list = []
                                        for el in args:
                                            self.my_list.append(el)
                                
                                    def __getitem__(self, index):
                                        return self.my_list[index]
                                        
                                print(my_obj[1])  # == my_obj.my_list[1]

    __call__()      - срабатывает при обращении к экземпляру класса как к функции. Примеры:
                            def __call__(self, newparam):
                                self.param = newparam
                            
                            def __call__(self, item1, item2):
                                return item1 + item2

    __str__()       - срабатывает при передаче экземпляра функциям str() и print(), преобразует в строку
                        возвращаемое значение return должно быть типа str - оно становится результатом работы str() итд
    __add__()       - срабатывает при участии экземпляра в сложении
                        при сложении экземпляров через return рекомендуется возвращать безымянный экземпляр класса:
                            def __add__(self, other):
                                return MyClass(self.par1 + other.par1, self.par2 + other.par2)

    __iadd__()      - срабатывает при участии объекта в сложении с присвоением
                        для модификации экземпляра класса возвращать self:
                            def __iadd__(self, other):
                                self.val += other
                                return self

    __isub__()      - срабатывает при участии объекта в вычитании с присвоением
    __gt__()        - срабатывает при сравнении через знак >
                        возвращаемое значение должно быть bool
                            def __gt__(self, other):
                                return self.val > other.val
                                
    __lt__()        -                           через знак <
    __ge__()        -                           через знак >=
    __le__()        -                           через знак <=
    __eq__()        -                           через знак ==
"""
# ПЕРЕОПРЕДЕЛЕНИЕ МЕТОДОВ===============================================================================================
r"""
Для использования методов и атрибутов родителя можно использовать вызов метода класса родителя из метода класса потомка:
        def method(self, arg)
            Parent.method(arg)
"""
# ИНТЕРФЕЙСЫ============================================================================================================
r"""
В ООП - описание поведения объекта.
Абстрактные классы - понтроллируют поведение потомков.
Для использования абстрактных классов необходимо импортировать ABC из модуля abc.
Для использования абстрактных методов необходимо импортировать abstractmethod из модуля abc.
    В примере ниже мы вынуждаем создавать дочерние для MyAbstractClass классы строго 
    с переопределением методов my_method_1 и my_method_2
            from abc import ABC, abstractmethod

            class MyAbstractClass(ABC):
                @abstractmethod
                def my_method_1(self):
                    pass
                @abstractmethod
                def my_method_2(self):
                    pass

"""
# ИНТЕРФЕЙС ИТЕРАЦИИ====================================================================================================
r"""
Реализуется с помощью методов __iter__() и __next__().
__iter__ должен возвращать экземпляр класса в котором находится вызова метода __next__ этого же класса
__next__ является по сути итератором работу которого можно настраивать. 
    В нём должно присутствовать достижимое условие при котором вызывается исключение StopIteration 
    иначе итерация будет бесконечной
            class Iter:
                def __init__(self, lst: list, start=0):
                    self.i = start - 1
                    self.lst = lst
            
                # Метод __iter__ должен возвращать объект-итератор
                def __iter__(self):
                    return self
            
                def __next__(self):
                    self.i += 1
                    if self.i <= 4:
                        return self.lst[self.i]
                    else:
                        raise StopIteration
            
            
            obj = Iter(['q', 'w', 'e', 'r', 't', 'y'])
            for el in obj:
                print(el)
            for el in obj:
                print(el)
"""
# ДЕКОРАТОР @property===================================================================================================
r"""
Позволяет работать с методом как с атрибутом
Так же позволяет устанавливать значение этому атрибуту через декоратор @<atrname>.setter
    имя атрибута и методов под декораторами @property и @<atrname>.setter а так же в <atrname> должно быть одно и то же:
        class Auto:
        
            # конструктор класса Auto
            def __init__(self, year):
                # Инициализация свойств.
                self.year = year
        
            # создаем свойство года
            @property
            def year(self):
                return self.__year
        
            # сеттер для создания свойств
            @year.setter
            def year(self, year):
                if year < 2000:
                    self.__year = 2000
                elif year > 2019:
                    self.__year = 2019
                else:
                    self.__year = year
        
            def get_auto_year(self):
                return f"Автомобиль выпущен в {str(self.year)} году"
        
        
        a = Auto(2090)
        print(a.year)
        print(type(a.year))
        print(a.get_auto_year())
"""
# КОМПОЗИЦИЯ============================================================================================================
r"""
Подразумевает наличие в экземпляре класса A атрибута предполагающего наличие в нём экземпляров другого класса.
Класс A называется контейнером.
        class WindowDoor:
            def __init__(self, wd_len, wd_height):
                self.square = wd_len * wd_height
        
        
        class Room:
            def __init__(self, len_1, len_2, height):
                self.square = 2 * height * (len_1 + len_2)
                self.wd = []
            def add_win_door(self, wd_len, wd_height):
                self.wd.append(WindowDoor(wd_len, wd_height))
            def common_square(self):
                main_square = self.square
                for el in self.wd:
                    main_square -= el.square
                return main_square
"""
# ======================================================================================================================
r"""

"""
# пример 1


class Iter:
    def __init__(self, lst: list, start=0):
        self.i = start - 1
        self.lst = lst

    # Метод __iter__ должен возвращать объект-итератор
    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i <= 4:
            return self.lst[self.i]
        else:
            raise StopIteration


obj = Iter(['q', 'w', 'e', 'r', 't', 'y'])
for el in obj:
    print(el)
for el in obj:
    print(el)

# ========================
# пример 2


class Auto:

    # конструктор класса Auto
    def __init__(self, year):
        # Инициализация свойств.
        self.year = year

    # создаем свойство года
    @property
    def year(self):
        return self.__year

    # сеттер для создания свойств
    @year.setter
    def year(self, year):
        if year < 2000:
            self.__year = 2000
        elif year > 2019:
            self.__year = 2019
        else:
            self.__year = year

    def get_auto_year(self):
        return f"Автомобиль выпущен в {str(self.year)} году"


a = Auto(2090)
print(a.year)
print(type(a.year))
print(a.get_auto_year())
a.year = 90
print(a.year)
print(type(a.year))
print(a.get_auto_year())
