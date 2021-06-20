""""""
# УРОК 2 ВВЕДЕНИЕ В PYTHON========================================================================================
r"""
УРОК 2
ВВЕДЕНИЕ В PYTHON

print('A','B') - сообщение в консоль 'A B'
print('A','B',sep='asd') - AasdB
print('A', end='zxc')
print('B')               - AzxcB
input('текст вопроса') - вопрос к пользователю из консоли
a = int(a) - привести переменную к целому числу
    float(a) - привести переменную к числу с плавающей точкой
    bool(a) - привести переменную к логическому типу true или false
    none(a) - привести переменную к пустому типу
    str(a) - привести переменную к строковому типу.
print(type(a)) - вывести тип переменной
арифметика    '+' '-' '*' '/' как обычно,
              '//' - деление без остатка(с округлением вниз),
              '%' - остаток от деления
              '**' - возведение в степень
              '=' - переменная слева получает значение выражения справа
              '+=' - переменная слева увеличивается на значение выражения справа
логика    '==' проверка равенства
          '!=' проверка неравенства
          '>' '<' '>=' '<=' проверка истиности знака
          'and' истина если условия и слева и справа являются истиной
          'or' истина если одно из условий является истиной
          'not' истина если выражение справа ложь
========Условный оператор===========
if выражение дающее при решениии true или false: - стартовый условный оператор
    блок команд выполняемых при значении true возле if.
    любые команды внутри блоков давать с отступом в 4 пробела от входа в блок
elif  выражение дающее при решениии true или false:   - НЕОБЯЗАТЕЛЬНЫЙ аналогично if, но является частью условия
                                                        это условие проверяется если все предыдущие elif
                                                        и стартовый if дали результат false.
                                                        ставится на один уровень с if и начинает новый блок
    блок команд выполняемых при значении true возле elif.
else: - НЕОБЯЗАТЕЛЬНЫЙ выполняется в случае если все предыдущие elif и стартовый if дали результат false
    блок команд выполняющихся в случае если все предыдущие elif и стартовый if дали результат false
====================================
==============Цикл==================
while выражение дающее при решениии true или false: - условие цикла. если значение true выполняется блок за ним
    блок команд выполняемых при значении true возле if.
    после выполнения блока условие цикла проверяется снова и в случае true выполняется снова
    блок повторяется пока значение выражения возле while не станет false или не будет выполнена команда
    break - выход из цикла без проверки условия цикла и выполнения последующих команд блока цикла
    continue - пропуск всех последующих команд блока цикла, переход к проверке условия цикла и следующему витку
else: - выполняется если условие цикла имеет значение false
====================================
"""
# УРОК 4 ВСТРОЕННЫЕ ТИПЫ И ОПЕРАЦИИ С НИМИ========================================================================
r"""
УРОК 4
ВСТРОЕННЫЕ ТИПЫ И ОПЕРАЦИИ С НИМИ

строковые переменные
чтобы в строке что-то заключить в одинарные ковычки следует заключать строку в двойные:
a = "asd is 'a'" >>> asd is 'a'
или наоборот:
a = 'asd is "a"' >>> asd is "a"

строка = набор символов, чтобы выдернуть символ следует указать возле строки(переменной строки)
         индекс символа в []. отсчёт индексов начинается с нуля:
a[2] == d
a[-1] == a
срез = часть строки. для получения среза нужно указать первый и последний индекс строки в срезе через : в [].
       индекс указанный вторым не будет включён в срез. не указанный индекс подразумевает начало/конец строки:
a[1:2] == s
a[1:3] == sd
a[:3] == asd
a[1:] == sd is "a"
len(a) == 10 >>> определяет длину строки
a.find('s') == 1 >>> ищет s в строке возвращает индекс первого символа искомого
a.split() >>> разбивает строку на список из строк которые в переменной были разделены указанными в скобках символами
              если в скобках ничего не указано, разделителем считается пробел
a.isdigit() >>> true если a состоит из чисел, иначе false
a.upper() >>> приводит к верхнему регистру
a.lower() >>> приводит к нижнему регистру
a.replace('b', 'c') - заменит строки b на строки c
a.startswith('b') - проверяет является ли строка b началом строки a. Имеет значение True или False
a.endswith('b') - проверяет является ли строка b окончанием строки a. Имеет значение True или False

суммирование строк:
+ не рекомендуется, т.к. все переменные требуется не забывать приводить к строке и расставлять пробелы.
  код трудно читать:
  name = 'Петя'
  age = 30
  str = 'Привет, ' + name + ', тебе ' + str(age) + ' лет.' - Привет, Петя, тебе 30 лет.
% %s для строковых, %d для числовых:
  str = 'Привет, %s, тебе %d лет.'%(name, age)
.format сам форматирует все переменные в строку. Там где требуется добавить переменные в шаблон ставим {}
  str = 'Привет, {}, тебе {} лет.'.format(name, age)
  str = f'Привет, {name}, тебе {age} лет.'

Списки
len(a) - возвращает количество элементов список a
a.append(b) - добавляет элемент b в конец списка a
b = a.pop() >>> b = последнему элементу списка a, из списка a удаляется последний элемент
a.clear() - очищает список a
a.remove(b) - удаляет элемент со значением b из списка a
c = a.count(b) - переменная c становится равна количеству элементов b в списке a
del a[i] - удаляет элемент с индексом i из списка a
b in a - проверяет наличие элемента b в списке a, 
         так же позволяет проверить наличие строки b в строке a если a и b - строки
         возвращает true или false
a.reverse() - переворачивает список a
b = sorted(a) - b принимает значение сортированного списка a

Кортеж - то же что и список, но записывается через (), а не []. 
         кортеж не подлежит изменению.

последовательность - строка'' кортеж() список[]

====Цикл for====
for i in a:     - перебирает элементы в последовательности a присваивая их значения переменной i
    print(i)    - операции в блоке для каждого элемента последовательности. в данном случае вывод элемента
================

диапазон/последовательность
b = 10
a = range(b[,c[,d]]) - а принимает значение диапазона целых чисел от b до последнего числа которое < c с шагом d
a = range(c)         - а принимает значение диапазона целых чисел от 0 до последнего числа которое < c
print(a) >>> range(0, 10)
print(list(a)) >>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = [q,w,e,r]
================
приведение цикла for к привычному по другим языкам виду
for i in range(len(a)): >>> перебор диапазона от 0 до длины списка a
    print(i)            >>> вывод текущего элемента диапазона
    print(a[i])         >>> вывод элемента списка a с индексом равным текущему элементу диапазона
результат:
0
q
1
w
2
e
3
r
================

словарь/dict
объявление словаря
a = {       - старт ввода словаря
    b: c,   - первый элемент словаря с ключом b и значением c
    d: e    - второй элемент словаря с ключом d и значением e
}
h = a[b] >>> c - обращение к элементу с ключом b
a[f] = g - добавление к словарю элемента с ключом f и значением g, 
           если ключ f уже существует, то его значение заменяется значением g 
remove a[f] - удаление из словаря a элемента с ключом f
================
a.keys() - список ключей. Применение для цикла for:
a = {'qwe': 1, 'asd': 'sdf', 'zxc': True}
for key in a.keys(): - перебираем элементы словаря a поочерёдно присваивая переменной key значения ключей
    print(key)       - выводим название ключа key
    print(a[key])    - выводим значение элемента по ключу key
результат:
qwe
1
asd
sdf
zxc
True

for key in a: - работает так же как for key in a.keys():
for val in a.values(): - перебираем элементы словаря a поочерёдно присваивая их значения переменной val
for key, val in a.items(): перебираем элементы словаря a поочерёдно присваивая их ключи и значения переменным key и val
================

множества/set
множества - неупорядоченные наборы не повторяющихся элементов
a = {b, c, d} - объявление множества a с элементами b, c и d
a.add(e) - добавление элемента e в множество a, если его нет в множестве
a.remove(e) - удаление элемента e из множества a
len(a) - возвращает длину множества
s = {b, t, d, u}
v = a | s >>> {b, c, d, t, u} - объединение множеств в новое множество v
                              - в множество v добавляются элементы из множеств a и s
                              - повторяющиеся элементы не добавляются
v = a & s >>> {b, d} - пересечение множеств
                     - имеющиеся в обоих множествах( a и s ) элементы добавляются в новое множество v
v = a - s >>> {c}    - разность множеств 
v = s - a >>> {t, u} - в новое множество v добавляются элементы первого множества, отсутствующие во втором
"""
# УРОК 5 РАЗБОР ПРАКТИЧЕСКОГО ЗАДАНИЯ=============================================================================
r"""
УРОК 5
РАЗБОР ПРАКТИЧЕСКОГО ЗАДАНИЯ

for a in b[:] - цикл работает не со списком b, а с его копией, 
              - позволяет издежать проблем связанных с проскоком через удалённые элементы списка b,
              - следует использовать, если предполагается в процессе цикла изменять список b

str = 'z x c'              
a, b, c = str.split() - переменные a, b, c примут значения фрагментов строки, на которые ее разобьет метод .split()
str = f'qwe {a} rty {b} ui {c}' >>> 'qwe z rty x ui c'

c = a.count(b) - переменная c становится равна количеству элементов b в списке a
"""
# УРОК 6 ПРАКТИКУМ. ИГРА "УГАДАЙ ЧИСЛО"===========================================================================
r"""
УРОК 6
ПРАКТИКУМ. ИГРА "УГАДАЙ ЧИСЛО"

для случайного числа:
import random as rnd - мы подключаем модуль random и в дальнейшем сможем его вызывать с помощью rnd
a = rnd.randint(b,c) - переменная a принимает значения целых чисел от b до c
"""
# УРОК 8 ФУНКЦИИ==================================================================================================
r"""
УРОК 8
ФУНКЦИИ

полезные встроенные функции
b = abs(a) - b = |a|
a = [5, 3, 7]
b = min(a) >>> 3
b = max(a) >>> 7
b = sum(a) >>> 15 - сумма элементов последовательности a
a = 3.17
с = 1
b = round(a,c) >>> 3.2 - округление a до количества знаков после запятой c
enumerate(a,b) - генерирует кортежи со значениями элементов и его итераторами
               - используется в цикле for
               - пример:
====
a = [5, 3, 7]
for i in enumerate(a):
    print(i)
(0, 5)
(1, 3)
(2, 7)
for i in enumerate(a,1):
    print(i)
(1, 5)
(2, 3)
(3, 7)
for i, b in enumerate(a):
    print(i, b)
0 5
1 3
2 7
====

Объявление функции
def a(b,c): - объявление функции a. в скобках указываются параметры b, c итд(параметры указывать не обязательно)
    d = b/c          - блок функции, операции которые выполняются после вызова функции
    return d         - возврат значений из функции, если не указан возвращается None
    
h = a(2,4) >>> h = 0.5   - вызов функции с передачей параметров по порядку
h = a(c=2,b=4) >>> h = 2 - вызов функции с передачей параметров по имени

def a(b = 4, c = 2):     - объявление функции с параметрами по умолчанию
    d = b/c              - блок функции, операции которые выполняются после вызова функции
    return d             - возврат значений из функции, если не указан возвращается None
    
h = a(2,4) >>> h = 0.5   - вызов функции с передачей параметров по порядку
h = a()    >>> h = 2     - вызов функции без параметров(используя параметры по умолчанию)

def a(b, *args):         - объявление функции с бесконечным количеством параметров args при помощи *
    print(b, args)

h = a(2, 3, 4, 5) >>> 2 (3, 4, 5) - параметры args образуют кортеж

def a(s, **kwargs):      - объявление функции с бесконечным количеством именованных параметров args при помощи **
    print(s, kwargs)

h = a(2, b=3, c=4, d=5) >>> 2 {'b': 3, 'c': 4, 'd': 5} - параметры kwargs образуют словарь

-------------------
Области видимости, локальные и глобальные переменные

переменные объявленные после блока функции недоступны внутри функции
переменные объявленные внутри блока функции являются локальными для нее, видимы и изменяемы
переменные объявленные до объявления функции являются для нее видимыми, но неизменяемыми
чтобы сделать их изменяемыми в функции требуется объявить их глобальными, но делать это не рекомендуется:
a = 1
get b():
    global a
-------------------

переменной можно присваивать не только возвращаемое значение функции, но и саму функцию
в последствии можно вызвать эту функцию используя переменную с параметрами так же как эту функцию
так же можно передавать саму функцию как параметр другой функции:
====
def my_filter(numbers, function):
    result = []
    for number in numbers:
        if function(number):
            result.append(number)
    return result
    
numbers = [1,2,3,4,5,6,7,8]

def is_even(number):
    return number % 2 == 0

print(my_filter(numbers, is_even)) >>> [2,4,6,8]

def not_even(number):
    return number % 2 != 0
    
print(my_filter(numbers, not_even)) >>> [1,3,5,7]

безымянные/лямбда функции

b = lambda c: c%2==0 - то же что и  def b(c):
                                        return c % 2 == 0
======                                        
print(my_filter(numbers, lambda number: number % 2 == 0))

равнозначно

def not_even(number):
    return number % 2 != 0
    
print(my_filter(numbers, not_even))
======

функция sorted:

сортировка списков:
a = [1,5,3,5,9,7,11]
b = sorted(a) >>> [1,3,5,5,7,9,11]
b = sorted(a, reverse=True) >>> [11,9,7,5,5,3,1]
со строками работает аналогично

сортировка двухмерных последовательностей:
a = [('msk',1000),('lvi',500),('ant',2000)]
b = sorted(a) >>> [('ant',2000),('lvi',500),('msk',1000)]

i = 1
def key_to_sort(elem):
    return elem[i]      >>> возврат элемента принятого списка с индексом i
    
b = sorted(a, key=key_to_sort)          >>> [('lvi',500),('msk',1000),('ant',2000)]
b = sorted(a, key=lambda elem: elem[i]) >>> [('lvi',500),('msk',1000),('ant',2000)]

функция filter:

filter(func, list) - в первый аргумент вставляется функция(или ее имя) возвращающая только True или False
                   - во второй аргумент вставляется последовательность(или ее имя) для фильтрации
                   - функция filter возвращает последовательность неизвестного типа. требуется использовать функции
                   - list(), tuple(), или другие приводящие аргумент к какой либо последовательности
a = [1,2,3,4,5,6,7,8]

b = list(filter(lambda n: n % 2 == 0, a)) >>> [2,4,6,8] 
                - не забываем приводить функцию filter к какому либо виду последовательности
                
функция map:
map(func, list) - в первый аргумент вставляется функция(или ее имя)
                - во второй аргумент вставляется последовательность(или ее имя)
                - каждый элемент последовательности list поочерёдно отправляется в качестве аргумента в функцию func, 
                - значения возвращаемые при каждом выполнении func формируют последовательность неизвестного типа.
                - требуется использовать функции приводящие аргумент к какой либо последовательности
"""
# УРОК 10 МОДУЛИ И БИБЛИОТЕКИ=====================================================================================
r"""
УРОК 10
МОДУЛИ И БИБЛИОТЕКИ

модуль - в python любой файл с расширением .py
его можно подключить полностью
import b [as a] - импортировать модуль b под именем a

или частично
from a import b, c - импортировать функции b, c из модуля a

Модуль random:
random.random() - случайное число от 0 до 1
random.randint(a, b) - случайное число от a до b включительно
random.choice(a) - случайный элемент последовательности a
random.sample(a, b) - случайный список длинной b из элементов последовательности a
random.shuffle(a) - перемешивает последовательность. не возвращает значение, работает напрямую с последовательностью!

Модуль math
math.factorial(a) - факториал числа a
math.exp(a) - экспонента числа a
math.log(a[, b]) - логарифм a с основанием b
math.log2(a) - логарифм a с основанием 2
math.log10(a) - логарифм a с основанием 10
math.sqrt(a) - квадратный корень a
math.sin(a), math.cos(a), math.asin(a)... - работа с углом a(В РАДИАНАХ!!!)
math.degrees(a) - конвертирует радианы в градусы
math.radians(a) - конвертирует градусы в радианы
math.pi - число пи
math.pow(a, b) - возводит число a в степень b

Импорт сторонних модулей:
находящихся в папке с программой
import b [as a]
находящихся в соседних папках
import c.b [as a] где c это папка с модулем

скрипт внутри подключаемого модуля будет выполняться при подключении
скрипт внутри модуля с подключаемыми из него переменными и функциями будет выполняться при подключении

в каждом модуле есть переменная __name__ которая 
    принимает значение '__main__' при запуске скрипта из этого модуля
    принимает значение равное названию этого модуля при подключении этого модуля
====
# команды выполняемые и при подключении, и напрямую из модуля
a = 'a'
print(a)

# команды которые не будут выполнены при подключении этого модуля
if __name__ == '__main__':
    b = 'b'
    print(b)
====

Пакеты:
Каталоги(с модулями и/или другими пакетами) в папке с программой, содержащие пустой скрипт __init__.py
Это позволяет вызывать скрипты в данных пакетах с любой глубиной вложенности.
Импорт модуля в пакете:
import b.c.[....]a - импорт модуля a из папки(относительно текущего файла) \b\c\[...\]

Модуль os:
os.name - имя операционной системы
os.chdir(a) - смена текущей директории с путём a
os.getcwd() - текущая рабочая директория
os.listdir(path='.') - отображает содержимое указанной папки(по умолчанию текущей рабочей)
os.mkdir(a) - создание директории с путём a(предварительно путь можно сгенерировать с помощью os.path.join())
os.path - модуль для работы с путями
os.path.isdir(path) - проверяет является ли путь папкой. Возвращает True если путь ведёт к папке и False если к файлу.
os.path.exists(a) - возвращает True если путь a существует
os.rmdir(a) - удаляет папку с путём a 
os.path.join(a[,b[,c[...]]]) - соединяет пути с учётом особенностей ОС:

a = os.path.join(os.getcwd(), 'b')
os.mkdir(a)                         - создание папки с именем 'b' в текущей активной папке

Модуль sys:
sys.executable - путь к интерпретатору python
sys.exit() - выход из программы
sys.platform - инфо об ОС
sys.path - список путей поиска модулей
sys.argv - список аргументов командной строки

Переменная sys.path:
Имеет тип list состоящий из путей к модулям
Ее можно менять при необходимости, добавляя пути с помощью sys.path.append(полный путь)

Переменная sys.argv:
Имеет тип list и содержит аргументы переданные в скрипт. 
sys.argv[0] - путь до скрипта
остальные передаются при вызове скрипта из терминала через пробел
вызов терминала - меню View > Tool Windows > Terminal или Alt + F12
вызов скрипта из терминала:
python [относительный путь до скрипта] [параметры через пробел]
"""
# УРОК 11 РАЗБОР ПРАКТИЧЕСКОГО ЗАДАНИЯ============================================================================
r"""
УРОК 11
РАЗБОР ПРАКТИЧЕСКОГО ЗАДАНИЯ

для выявления наличия данных в переменной достаточно в блоке if указать переменную - 
в случае отсутствия данных она вернёт false

if a:
    какой-то блок
else:
    блок выполняемый при пустом значении а
"""
# УРОК 12 РАБОТА С ФАЙЛАМИ. КОДИРОВКИ=============================================================================
r"""
УРОК 12
РАБОТА С ФАЙЛАМИ. КОДИРОВКИ

f = open('a','mode'[, encoding='c'])    - присвоение файла a с режимом mode переменной f
                                        - режимы открытия файла:
                                        - r чтение
                                        - w запись, если файла нет - создается новый, содержимое существующего удаляется
                                        - x запись, если файл существует выдаётся ошибка
                                        - a дозапись
                                        - + открытие на чтение и запись
                                        - b байтовый тип данных - добавляется к букве режима чтения/записи
                                        - режим encoding='кодировка' указывает в какой кодировке будут представлены  
                                        - данные НЕбайтовом типе данных
f.write(a)      - записать строку a в файл открытый как f
f.writelines(a) - записать список строк в файл открытый как f
                - строки при записи в файл не переносятся. 
\n              - Для переноса строк следует использовать символ конца строки. 
                - символ конца строки считается строкой при считывании файла.
f.read() - чтение всего файла
for line in f:                          - чтение файла построчно. 
    b.append(line.replace('\n', ''))  - для удаления символов конца строки рекомендуется использовать .replace
a = f.readlines() - чтение строк файла f в список a
После работы с файлами их необходимо закрывать т.к. они тратят ресурсы системы
f.close() - команда закрытия файла, но если произойдёт исключение, файл останется открыт
with - рекомендуется вместо open()/close()
with open('a.txt', 'r') as f:           - после выполнения вложенных блоков файл закроется автоматически. 
    for line in f:
        b.append(line.replace('\n', ''))
======
Строки в Python бывают двух типов:
str - обычные строки
bytes - строки байт
bytearray - изменяемая строка байт
sb = b'Hello World' - строки байт сохраняются в переменную так же, как обычная но с буквой b перед кавычками
                    - строки байт при объявлении таким способом поддерживают ТОЛЬКО символы из ASCII таблицы.
при запросе символа строки байт по индексу возвращается не символ, а его код таблице символов
при запросе среза отображается содержимое среза
символы отсутствующие в ASCII будут в любом случае отображаться в виде шифра

основные кодировки:
ASCII   - американские символы
latin-1 - +европейские
UTF-8   - универсальная кодировка поддерживающая большинство языков
чем универсальнее кодировка тем больше байт занимает каждый символ

a = 'ёпрст'
b = a.encode('utf-8') >>> b'\xd1\x91\xd0\xbf\xd1\x80\xd1\x81\xd1\x82' 
                        - кодирует строку a в байтовую строку в кодировку utf-8 и передает в переменную b
                        - указанная кодировка должна поддерживать передаваемые в строке символы, иначе ошибка

c = b.decode('utf-8') >>> 'ёпрст'   - декодирует байтовую строку b из кодировки utf-8 в переменную c
                                    - должна быть указана кодировка в которую была изначально закодирована строка
                                    - если ошибиться с кодировкой вывод будет неверным
======
модуль pickle предназначен для сохранения/загрузки объектов в файлах

dump - сохранение объекта в файл:
data = {'a': 'b', 'c': ['d','e']}
with open('a.dat', 'wb') as f:
    pickle.dump(data, f)        - сохранение объекта data в файле a.dat
with open('a.dat','rb') as f:
    loaded = pickle.load(f)     - загрузка объекта в переменную loaded из файла a.dat
a = pickle.dumps(data) - преобразование объекта data в строку байтов в переменной a
loaded = pickle.loads(a) - загрузка объекта из строки байтов a в переменную loaded
======
формат JSon - представление объектов в виде простых строк

with open('a.dat', 'w') as f:
    tmp = json.dump(data, f)                            - сохранение объекта data в формате json в файл a.dat
with open('a.dat', 'r') as f:
    loaded = json.load(f)                               - загрузка объекта из файла a.dat в переменную loaded
a = json.dumps(data) >>> '{"a": "b", "c": ["d","e"]}'   - преобразование объекта data в текстовую переменную a
loaded = json.loads(a) >>> {'a': 'b', 'c': ['d','e']}   - преобразование строки a в формате json в объект loaded
"""
# УРОК 14 ПОЛЕЗНЫЕ ИНСТРУМЕНТЫ. ОБРАБОТКА ИСКЛЮЧЕНИЙ==============================================================
r"""
УРОК 14
ПОЛЕЗНЫЕ ИНСТРУМЕНТЫ. ОБРАБОТКА ИСКЛЮЧЕНИЙ

Тернальный оператор:
a = b if c else d   - a = b если значение выражения c = True, a = d если c = False

Генераторы работают быстрее чем циклы!
Генератор списков:
a = [b for c in d if e] - равнозначное выражение:    for c in d:
                                                        if e:
                                                            b = чтото
                                                            a.append(b)
                         - a - список-результат
                         - for c in d - цикл по элементам последовательности d
                         - [if e - условие при выполнении которого происходит вычисление значения b] - необязательно
                         - b - выражение, результат вычисления которого добавляется в список a, например элемент c
Пример:
d = [1,2,3,4,5,-1,-2,-3]    - задача убрать отрицательные числа
a = [c for c in d if c > 0] >>> [1,2,3,4,5]

Генератор словарей:
a = {b: c for d in e}   - равнозначно выражению:    for d in e:
                                                        a[b] = c
                        - a - словарь результат
                        - for d in e - цикл по элементам последовательности e(обычно список кортежей)
                        - b - выражение, при вычислении которого получается ключ в словаре a
                        - c - выражение, при вычислении которого получается значение для ключа b
Пример:
e = [(1,'a'),(2,'b'),(3,'c')]   - задача преобразовать список кортежейй в словарь
a = {d[0]: d[1] for d in e} >>> {1: 'a', 2: 'b', 3:'c'}

====
Правила приведения типов к bool:
True = непустая последовательность, непустая строка, число не равное нулю
False = Пустая последовательность/строка, None, 0

Особенности работы and
оператор and возвращает первую False или последнюю True в выражении, 
не выполняет проверки после обнаружения первой False:
a = [1] and [2] and {} and 1 and 0 >>> {}
a = [1] and 1 and 'sdfds' and 1.1 >>> 1.1
a = [] and b/0 >>> []
a = b/0 and [] >>> error

Оператор or возвращает последнюю False или первую True в выражении,
не выполняет проверки после обнаружения первой True:
a = [] or [2] or {} or 1 or 0 >>> {2}
a = [] or 0 or '' or None >>> None
a = [1] or b/0 >>> [1]
a = b/0 or [1] >>> error

При работе со списком! в случае присваивания значения списка в другую переменную присваивается по сути ссылка на список:
a = [1,2,3]
b = a
b[1] = 100
print(a) >>> [1,100,3]

аналогичная ситуация при передаче списка в качестве аргумента функции
чтобы этого избежать используется модуль copy:
from copy import deepcopy

b = deepcopy(a)
___________________
Исключительные ситуации/исключения/ошибки

для обработки исключений требуется:
код который может вызвать исключение требуется поместить в блок try:, а блок реакции на исключение в блок except:
try:
    блок исполняющийся при 
    нормальной работе программы
except[ тип исключения[ as N]]:             - где N переменная в которую будут записаны данные об исключении
    блок исполняющийся в случае исключения
    
если блок except без типа исключения, он будет выполняться при любых исключениях.
можно создать несколько блоков except для разных типов исключений
после блоков except: можно создать блок else: который будет выполнен в случае отсутствия исключения
после блока else: создаётся блок finally: который будет выполняться в любом случае

Так же можно вызвать исключение с помощью команды raise:
raise тип_исключения('текст исключения')
"""
# УРОК 16 ПРАКТИКУМ. КОНСОЛЬНЫЙ ФАЙЛОВЫЙ МЕНЕДЖЕР=================================================================
r"""
УРОК 16
ПРАКТИКУМ. КОНСОЛЬНЫЙ ФАЙЛОВЫЙ МЕНЕДЖЕР

Модуль os:
os.name - имя операционной системы
os.chdir(a) - смена текущей директории с путём a
os.getcwd() - текущая рабочая директория
os.listdir(path='.') - отображает содержимое указанной папки(по умолчанию текущей рабочей)
os.mkdir(a) - создание директории с путём a(предварительно путь можно сгенерировать с помощью os.path.join())
os.rmdir(a) - удаляет пустую папку с путём a
os.remove(a) - удаляет файл с путём а
os.path - модуль для работы с путями
os.path.isdir(path) - проверяет является ли путь папкой. Возвращает True если путь ведёт к папке и False если к файлу.
os.path.exists(a) - возвращает True если путь a существует
os.path.join(a[,b[,c[...]]]) - соединяет пути с учётом особенностей ОС:

Модуль shutil
shutil.copytree(a, b) - копирует папку. источник полное имя(с путём) a, результат полное имя b
shutil.copy(a, b) - копирует файл. источник полное имя(с путём) a, результат полное имя b

Модуль datetime
datetime.datetime.now() - текущая дата-время

"""
# АЛГОРИТМЫ
# УРОК 4 ПРОФИЛИРОВАНИЕ КОДА============================================================================
r"""
Измерение времени запуска - модуль timeit:
    import timeit
    print(timeit.timeit("x = 2 + 2"))
Возвращено будет время выполнения операции

Профилирование
для профилирования кода требуется импортировать модуль cProfile, обернуть исполняемую часть кода в функцию и
    запустить её в профайлере:
    
        import cProfile
        def main():
            a = [3,5,6,7]
            s = let(a)
            t = sum(a)
        
        cProfile.run('main()')
    
"""
# УРОК 5 КОЛЛЕКЦИИ. СПИСОК. СЛОВАРЬ. ОЧЕРЕДЬ.=====================================================================
r"""
Работают из модуля collections
    import collections

collections.Counter(a) - создаёт обект на базе словаря из последовательности a где ключами являются элементы 
                        последовательности, а значениями - количество совпадений с этими элементами в последовательности
                        в случае если a является словарём объект использует значения из a.
                            если в словаре a есть неint элементы это будет вызывать ошибки при использовании методов
                            объекта Counter.
    >>> counter = collections.Counter(['spam', 'egg', 'spam', 'counter', 'counter', 'counter'])
    >>> counter
    Counter({'counter': 3, 'spam': 2, 'egg': 1})

collections.Counter(a).elements() - возвращает генератор с последовательностью a. 
                                    Порядок элементов соответствует порядку ключей в хэше.
                                    Отрицительные и нулевые элементы игнорируются.

collections.Counter(a).most_common(b) - возвращает список кортежей из ключей и значений Counter(a), 
                                        отсортированных по убыванию.
                                        Количество кортежей равно b если длина словаря достаточна,
                                            либо количеству ключей в словаре если длина словаря меньше b

collections.Counter(a).subtract(b) - изменяет коллекцию a вычитая из её значений значения последовательности b

Deque
очередь. добавлять и удалять элементы можно только с начала или с конца очереди
    append(x) – добавляет элемент x в конец очереди;
    appendleft(x) – добавляет элемент x в начало очереди;
    clear() – очищает очередь;
    count(x) – возвращает количество элементов очереди, равных x;
    extend(iterable) – добавляет в конец очереди все элементы iterable;
    extendleft(iterable) – добавляет в начало очереди все элементы iterable (начиная с последнего);
    pop() – удаляет и возвращает последний элемент очереди;
    popleft() – удаляет и возвращает первый элемент очереди;
    remove(value) – удаляет первое вхождение value в очереди;
    reverse() – разворачивает очередь;
    rotate(n) – последовательно переносит n элементов из начала в конец (если n отрицательно, то с конца в начало).

defaultdict
Объект на базе словаря с упрощённым созданием значений. 
    создаётся словарь через
    collections.defaultdict(type) - действия со значениями производятся в соответствии с типом последовательности
                                    при обращении к несуществующему ключу автоматически создаётся ключ со значением
                                        равным пустому элементу указанного типа.
    >>> defdict = collections.defaultdict(list)
    >>> print(defdict)
    defaultdict(<class 'list'>, {})
    >>> for i in range(5):
    >>>     defdict['a'].append(i)
    >>> print(defdict)
    defaultdict(<class 'list'>, {'a': [0, 1, 2, 3, 4]})

OrderedDict
коллекция на базе словаря. Запоминает порядок следования ключей.
При принте выводится в виде списка кортежей.
popitem(last=True)          – удаляет последний элемент, если last=True, и первый, если last=False;
move_to_end(key, last=True) – добавляет ключ в конец, если last=True, и в начало, если last=False.

Namedtuple
именованный кортеж. можно обращаться к элементам кортежа как к атрибутам.
сначала создаётся класс, потом будущий объект должен скормить в класс значения элементов:
Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(x=1, y=2)
p.x == p[0] == 1



Методы сравнения множеств:
set_a.isdisjoint(set_b)     - вернёт True если в множествах нет совпадающих элементов
set_b.issubset(set_a)       - вернёт True если все элементы set_b имеются в set_a
set_b.issuperset(set_a)     - вернёт True если все элементы set_a имеются в set_b

способ создать словарь:
my_keys = ('a', 'b', 'c')
my_values = [1, 2] 
my_dict = dict(zip(my_keys, my_values)) # {'a': 1, 'b': 2}
"""
# ================================================================================================================
r"""

"""
qa_list = {
    'question1': {'answer1': 1, 'answer2': 2},
    'question2': {'answer1': 1, 'answer2': 2}
}

summ = 0
for question in range(3):
    answer = input(f'{question}\n input answer')
    summ += qa_list[question].get(answer, 0)

print(summ)
