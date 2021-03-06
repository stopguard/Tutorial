""""""
r"""
Модуль os
r-строки - игнорируют управляющие символы в строке
'\n dsf' == '
 dsf'
r'\n dsf' == '\n dsf'

os.listdir(path)    - возвращает список содержимого директории по указанному пути
                    без просмотра содержимого вложенных папок
os.scandir(path) - аналогично listdir но возвращает генератор. Работает быстрее.
                    Занимает итерируемые ресурсы пока не истощён.
                    Необходимо спользовать внутри менеджеров контекста или итераторов.
os.stat(path) - информация о пути. в атрибутах хранятся объём, дата создания, изменения, доступа и другое
os.mkdir(path) - создать папку с указанным путём. Путь где создаётся папка должен существовать
os.makedirs(path) - создаёт указанный путь.
os.rename(old_path, new_path) - переименование/перемещение, путь назначения должен существовать
os.remowe(path) - удаление указанного файла
os.rmdir(path) - удаление указанной папки
os.walk(root) - генератор возвращающий кортежи вида ('path', [dirs], [files])
                последовательно для папки с путём root, а затем для всех вложенных папок рекурсивно
os.path.join(path[,path[,...]]) - собирает путь из указанных фрагментов с учётом особенностей ОС
os.path.isfile(path) - проверка является ли путь файлом
os.path.isdir(path) - является ли путь папкой
os.path.abspath(path) - возвращает абсолютный путь
os.path.relpath(path[, start=None]) - возвращает относительный путь из папки start(по умолчанию текущей)
os.path.basename(path) - возвращает имя файла без пути
os.path.dirname(path) - возвращает путь к указанному файлу
os.path.split(path) - возвращает кортеж из пути и имени файла
os.path.exists(path) - проверка наличия указанного пути

Модуль shutil
shutil.rmtree(path) - удаляет указанную директорию и вложенные папки
shutil.copyfileobj(fileobj, fileobj2[, length]) - копирование файлового объекта в другой используя буфер length
                                                - перед применением необходимо открыть оба файла
shutil.copyfile(path1, path2)   - копирование содержимого одного файла в другой без настроек доступа
                                - возвращает path2
                                - как .copyobj() но открывает файл за нас и включает в себя проверки
shutil.copy(path1, path2)   - копирование файла path1, в файл или папку path2.
                            - сохраняет настройки доступа
                            - возвращает path2
                            - если path2 папка - имя файла сохраняется.
shutil.copy2(path1, path2)  - как .copy() но копирует метаданные
                            - возвращает path2

Обработка исключений
try:
    блок в котором мы ловим ошибки
except (errortypes) as <name for save errorstr>:
    блок выполняемый при заданных ошибках
except (errortypes) as <name for save errorstr>:
    блок выполняемый при заданных ошибках
...
else:
    блок выполняемый в случае отсутствия исключений
finally:
    блок выполняемый в любом случае

Генерация исключений
class errorname(Exception):
    блок выполняемый при генерации исключения errorname

raise errorname - вызов исключения errorname

Иерархия встроенных исключений:
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
"""
