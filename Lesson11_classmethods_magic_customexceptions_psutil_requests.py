""""""
# СТАТИЧЕСКИЕ МЕТОДЫ====================================================================================================
r"""
Методы класса не обязательно принимающие в качестве аргументов объекты.
Работают через декоратор @staticmethod
"""
# МЕТОДЫ КЛАССА=========================================================================================================
r"""
Методы в которые передаётся класс в качестве параметра. 
По умолчанию в метод передаётся класс объекта из которого вызывается метод.
Работают через декоратор @classmethod
"""
# ВСТРОЕННЫЕ МЕТОДЫ И АТРИБУТЫ ОБЪЕКТОВ КЛАССОВ=========================================================================
r"""
Атрибуты:
__name__        - имя класса
__module__      - имя модуля
__dict__        - словарь атрибутов класса
__bases__       - кортеж родительских классов
__doc__         - строка документации класса
__class__       - класс к которому принадлежит экземпляр вызвавший метод
Методы:
__init__        - конструктор
__del__         - деструктор
__hash__        - возвращает хеш-значение объекта, равное 32-битному числу
__getattr__     - возвращает атрибут, недоступный обычным способом
__setattr__     - присваивает значение атрибуту
__delattr__     - удаление атрибута
__call__        - выполняется при вызове экземпляра класса
__str__         - вызывается при приведении объекта к строке
__repr__        - улучшенный __str__
__getitem__     - вызывается при получении элемента по индексу/ключу
__setitem__     -            при присвоении значения элементу по индексу/ключу
__delitem__     -            при удалении элемента по индексу/ключу
"""
# ПРИМЕР ООП-ПРОГРАММЫ==================================================================================================
r"""
В рамках ООП, предполагается выполнение предварительного проектирования. 
План выполнения проекта должен выглядеть примерно так:
1.  Сформулировать задачу
2.  Определить объекты участвующие в решении задачи
3.  Выделить классы на основе которых генерируются объекты с определением потомков и наследников.
4.  Вывести основные атрибуты и методы объектов
5.  Создать классы, атрибуты и методы
6.  Создать объекты
7.  Выполнить решение задачи

Разработка виртуальной модели образовательного процесса:
Реальные объекты этой модели - студенты, преподаватель, знания.
Следовательно нужны классы "Преподаватель", "Студент", "Курс"
У классов "Преподаватель" и "Студент" есть общие параметры имени и фамилии, 
    следовательно получается родительский класс "Персона", в котором выделяем общие для преподавателей и студентов
    методы и атрибуты
В классе "Преподаватель" наследуем атрибуты из класса "Персона" и добавляем метод "обучение()", 
    который получает в аргументы ссылку на объект класса "Предмет" и список студентов изучающих предмет.
    В методе "обучение()" для каждого студента требуется вызвать метод "усвоение()",
    который будет фиксировать получение знаний студентом в атрибут-список "знания".
В классе "Студент" так же наследуем атрибуты из класса "Персона" и 
    определяем метод "усвоение()" для пополнения списка "знания".
Создадим так же класс "Курс", которыйбудет содержать список предметов "предметы" возвращаемый методом "список_предметов"


        class Person:
            def __init__(self, name, surname):
                self.name = name
                self.surname = surname
            def __str__(self):
                return f"Name and surname: {self.name} {self.surname}"
        
        class Teacher(Person):
            def to_teach(self, subj, *pupils):
                for pupil in pupils:
                    pupil.to_take(subj)
        
        class Pupil(Person):
            def __init__(self, name, surname):
                super().__init__(name, surname)
                self.knowledges = []
            def to_take(self, subj):
                self.knowledges.append(subj)
        
        class Subject:
            def __init__(self, *subjects):
                self.subjects = list(subjects)
            def my_list(self):
                return self.subjects


        s = Subject("maths", "physics", "chemistry")
        t = Teacher("Ivan", "Ivanov")
        print(t)
        
        p_1 = Pupil("Petr", "Petrov")
        p_2 = Pupil("Sergey", "Sergeev")
        p_3 = Pupil("Vladimir", "Vladimirov")
        print(f"{p_1}; {p_2}; {p_3}")
        
        t.to_teach(s, p_1, p_2, p_3)
        print(p_1.knowledges[0].my_list())
"""
# СОЗДАНИЕ СОБСТВЕННЫХ ИСКЛЮЧЕНИЙ=======================================================================================
r"""
Для создания собственного исключения требуется создать класс с родителем Exception в конструкторе которого будут 
    приниматься некие данные о переменных участвовавших в исключении и/или текст передаваемый с вызовом исключения.
Для вызова исключения используется ключевое слово raise и имя исключения с передачей в него необходимых аргументов:
        class OwnError(Exception):
            def __init__(self, txt):
                self.txt = txt
        
        inp_data = input("Введите положительное число: ")
        
        try:
            inp_data = int(inp_data)
            if inp_data < 0:
                raise OwnError("Вы ввели отрицательное число!")
        except ValueError:
            print("Вы ввели не число")
        except OwnError as err:
            print(err)
        else:
            print(f"Все хорошо. Ваше число: {inp_data}")
            
Результаты:
Введите положительное число: 5
Все хорошо. Ваше число: 5

Введите положительное число: text
Вы ввели не число

Введите положительное число: -65
Вы ввели отрицательное число!

Помимо прочего для экземпляров класса Exception доступен метод __str__().
    С его помощью можно выводить значения атрибутов исключения
Так же можно использовать встроенные средства вывода данных об ошибке.
Модуль traceback позволяет собирать информацию о программе при появлении исключения.
В частности его функция format_exc() позволяет выводить стандартное сообщение об ошибке без использования переменной.
"""
# БИБЛИОТЕКА PSUTIL=====================================================================================================
r"""
Позволяет получить информацию о параметрах процессора памяти и дисков.
Функции модуля:
cpu_stats()  - возвращает строку вида scpustats(ctx_switches=2308, interrupts=1763, soft_interrupts=0, syscalls=11512)
disk_usage("disk_name:") - возвращает строку вида sdiskusage(total=89272253, used=9932360, free=79339893, percent=11.1)
virtual_memory() - возвращает строку вида svmem(total=854712, available=377740, percent=55.8, used=476971, free=377740)
"""
# БИБЛИОТЕКА REQUESTS===================================================================================================
r"""
        import requests
        
        resp = requests.get('https://github.com/requests')
        print(resp)
        print(type(resp))
        
        resp = requests.put('https://github.com/requests/put')
        print(resp)
        resp = requests.delete('https://github.com/requests/delete')
        print(resp)
        resp = requests.head('https://github.com/requests/get')
        print(resp)
        resp = requests.options('https://github.com/requests/get')
        print(resp)
        print('\n\nПередача аргументов в запросе')
        data = {'key1': 'value1'}
        resp = requests.get("https://github.com/requests/get", params=data)
        print(resp)
        print('\n\nСодержимое объекта response')
        resp = requests.get("https://github.com/requests/")
        print(resp.text)
        print('\n\nКоды состояний и заголовки')
        resp = requests.get("https://github.com/requests/")
        print(resp.status_code)
        print(resp.headers)
        
Переменная resp содержит ссылку на объект Response. 
Средствами библиотеки requests можно выполнять стандартные запросы: PUT, DELETE, HEAD, OPTIONS.
"""
# ======================================================================================================================
r"""

"""
