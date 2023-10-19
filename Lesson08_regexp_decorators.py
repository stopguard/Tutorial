""""""
# РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ==================================================================================================
r"""
для работы с регулярными выражениями используется 

модуль re
в строке регулярного выражения нужно использовать сырые r-строки:
    r'блаблабла'
    Полезные ссылки:    Статья на хабре:
                        https://habr.com/ru/post/349860/
                        Более полная инфа:
                        https://docs-python.ru/standart-library/modul-re-python/sintaksis-reguljarnogo-vyrazhenija/
                        Отладчик регулярок:
                        https://regex101.com/r/F8dY80/3
    a.findall(b)    - возвращает из строки b список совпадений с регулярным выражением a
    a.search(b)     - возвращает из строки b Match объект вхождения регулярного выражения a с аттрибутами 
                        span=(начало, конец среза вхождения), match='срез вхождения'
    a.match(b)      - как search, но ищет только в начале строки
    a.finditer(b)   - возвращает из строки b итератор с Match объектами вхождений регулярного выражения a
    a = re.compile(b[, flags])  - преобразовывает строку b в регулярное выражение a с флагами flags
                                - флаг re.IGNORECASE - игнорирование регистра
                                - флаг re.MULTILINE - для обработки многострочных текстов

Валидация строки на отсутствие НЕбукв русского алфавита:
    r'^[А-ЯЁ][а-яё]+$'
Валидация строки на похожесть формата на дату (пропустит даты типа "48.67.3673"):
    r'^(\d{2}[./-]){2}\d{4}$'
    дефис должен быть последним при перечислении символов в []
Парсинг списка покупок:
    txt = '''
    Иван сегодня сделал заказ: "iPhone 12"  (158900,6 руб),
    "Galaxy S21"(98653.7 р).
    Позже он добавил в корзину "iPad"\t(32451)
    '''
    
    RE_PRODUCTS = re.compile(r'"([^"]+)"\s*\((\d+(?:[,.]\d+)*).*\)')
    print(RE_PRODUCTS.findall(txt))
        # [('iPhone 12', '158900,6'), ('Galaxy S21', '98653.7'), ('iPad', '32451')]

Список символов в регулярках
    .       - один любой символ
    \d      - любая цифра
    \D      - любая НЕцифра
    \s      - любой пробельный символ(пробел, таб, конец строки итд)
    \S      - любой НЕпробельный символ
    \w      - любая буква, цифра, _
    \W      - что угодно кроме \w
    [..]    - один из указанных символов, можно указывать диапазоны через '-', для указания '-' - поставить его в конец
    [^..]   - любой символ кроме указанных
    \b      - начало или конец слова
    \B      - НЕ начало или НЕ конец слова
    |       - или
    (..)    - группа с захватом
    (?:..)  - группа без захвата
    \num    - содержимое группы(с захватом) номер num
    \       - экранирование спецсимволов
    ^       - начало строки
    $       - конец строки
    \A      - начало текста
    \Z      - конец текста
    (?P<name>..)    - именованная группа
    (?P=name)       - ссылка на именованную группу
    
    \d≈[0-9]
    \D≈[^0-9]
    \w≈[0-9a-zA-Zа-яА-ЯёЁ] + неарабские цифры
    \s≈[ \f\n\r\t\v]
            - внутри скобок требуется экранировать только ] и \

Квантификаторы
    {n}     - n повторений
    {m,n}   - от m до n повторений
    {m,}    - не менее m повторений
    {,n}    - не более n повторений
    ?       - == {0,1}
    *       - == {0,}
    +       - == {1,}
    квант?  - дана строка                 '(a + b) * (c + d) * (e + f)' 
                            r'\(.*\)' =>  '(a + b) * (c + d) * (e + f)'
                            r'\(.*?\)' => '(a + b)'
            - делает квантификаторы ленивыми, заставляет искать минимум повторений

Проверки
    (?=..)  - опережающая позитивная проверка
    (?!..)  - опережающая негативная проверка
    (?<=..) - ретроспективная позитивная проверка
    (?<!..) - ретроспективная негативная проверка
    (?(id/name)yes-pattern|no-pattern)  - если группа с указанным именем/номером существует
                                          используется yes иначе no(необязательный аргумент)
"""
# ДЕКОРАТОРЫ============================================================================================================
r"""
Синтаксически функция A объявленная выше функции B и 
    указанная на сразу над объявлением функции B с префиксом @ становится декоратором.
    в примере ниже p_wrapper является декоратором для функции render_input:
        def p_wrapper(func):
            def tag_wrapper(*args, **kwargs):
                markup = func(*args, **kwargs)
                return f'<p>{markup}</p>'
        
            return tag_wrapper
        
        
        @p_wrapper
        def render_input(field):
            return f'<input id="id_{field}" type="text" name="{field}">'
        
        
        username_f = render_input('username')
        print(username_f)

Первое - аргументом декоратора становится оборачиваемая функция(над которой написон декоратор)
Второе - внутри декоратора должна быть функция которая пример аргументы декорируемой функции

для вызова данных о декорируемой функции из внешнего декоратора, 
    требуется декорировать внутреннюю функцию этого декоратора декоратором 
        @wraps
    предварительно его требуется импортировать из модуля functools. например без wraps:
        from functools import wraps
        
        
        def simple_cache(func):
            # @wraps(func)
            def wrapper(*args):
                res = func(*args)
                return res
            return wrapper
        
        
        def logger(func):
            def wrapper(*args):
                result = func(*args)
                funct = func.__name__
                print(f'\tcall {funct}({", ".join(map(str, args))})')
                return result
            return wrapper
        
        
        @logger
        @simple_cache
        def render_input(field):
            return f'<input id="id_{field}" type="text" name="{field}">'
        
        
        username_f = render_input('username')
    
    >>> call wrapper(username)

    с wraps:
    
        from functools import wraps
        
        
        def simple_cache(func):
            @wraps(func)
            def wrapper(*args):
                res = func(*args)
                return res
            return wrapper
        
        
        def logger(func):
            def wrapper(*args):
                result = func(*args)
                funct = func.__name__
                print(f'\tcall {funct}({", ".join(map(str, args))})')
                return result
            return wrapper
        
        
        @logger
        @simple_cache
        def render_input(field):
            return f'<input id="id_{field}" type="text" name="{field}">'
        
        
        username_f = render_input('username')
    
    >>> call render_input(username)
"""
from functools import wraps as wrp


def simple_cache(func):
    @wrp(func)
    def wrapper(*args):
        res = func(*args)
        return res

    return wrapper


def logger(func):
    def wrapper(*args):
        result = func(*args)
        funct = func.__name__
        print(f'\tcall {funct}({", ".join(map(str, args))})')
        return result

    return wrapper


@logger
@simple_cache
def render_input(field):
    return f'<input id="id_{field}" type="text" name="{field}">'


username_f = render_input('username')
print(username_f)
