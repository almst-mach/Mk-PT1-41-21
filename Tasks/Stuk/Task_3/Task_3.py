SEP = " "


def search_start_line(line: str, start_new_line: int, step: int) -> int:
    """Ф-ия определения позиции начала следующей подстроки

    Args:
        line (str): подстрока основной строки
        start_new_line (int): позиция начала следующей подстроки
        step (int): длина строки

    Raises:
        ValueError: длина строки меньше длины слова

    Returns:
        int: позиция начала следующей подстроки
    """
    pos = line.rfind(" ") + 1
    if not pos:
        raise ValueError("Хьстон, у нас проблема! Длина строки меньше длины слова!")
    if pos >= step:
        return start_new_line
    else:
        return start_new_line - step + pos


def create_list_words(line: str, flag_last_line: bool) -> list:
    """Формирование списка слов в подстроке

    Args:
        line (str): подстрока
        flag_last_line (bool): флаг последней подстроки в строке 

    Returns:
        list: список слов
    """
    if flag_last_line or line[-1] == " " or line[-2] == " ":
        list_words = line.split()
    else:
        list_words = line.split()[:-1]
    return list_words


def get_length_words(list_words: list) -> int:
    """Подсчет кол-ва символов во всех эл-тах списка

    Args:
        list_words (list): список слов

    Returns:
        int: кол-во символов во всех эл-тах списка
    """
    count = 0
    for word in list_words:
        count += len(word)
    return count


def get_count_spaces(count_spaces: int, count_words: int) -> list:
    """Фомирование списка с кол-вом разделительных символов между словами

    Args:
        count_spaces (int): кол-во символов разделителей
        count_words (int): кол-во слов

    Returns:
        list: список с кол-вом разделительных символов между словами
    """
    length_space = count_spaces // (count_words - 1)
    list_spaces = [length_space for i in range(count_words - 1)]

    count_additional_space = count_spaces % (count_words - 1)
    for i in range(count_additional_space):
        list_spaces[i] += 1
    return list_spaces


def create_format_line(list_words: list, count_words: int, count_spaces: int) -> str:
    """Формирование одной новой строки фиксированной длины

    Args:
        list_words (list): список слов из которых формируется строка
        count_words (int): кол-во слов в строке
        count_spaces (int): кол-во символов разделителей

    Returns:
        str: форматированная строка фиксированной длины
    """
    list_spaces = get_count_spaces(count_spaces, count_words)
    out_line = list_words[0]
    for i, count_space in enumerate(list_spaces):
        out_line += SEP * count_space + list_words[i+1]
    return out_line

    
def create_output_line(line: str, step: int, flag_last_line = False) -> str:
    """Формирование одной новой строки фиксированной длины

    Args:
        line (str): строка, которую нужно отформатированть
        step (int): длина выходной строки
        flag_last_line (bool, optional): флаг последней подстроки в строке. Defaults to False.

    Returns:
        str: форматированная строка фиксированной длины
    """
    list_words = create_list_words(line, flag_last_line)
    length_words = get_length_words(list_words)
    count_words = len(list_words)
    count_spaces = step - length_words

    if count_words == 1:
        return list_words[0]
    elif count_words == 0:
        return ""
    elif flag_last_line:
        count_spaces = count_words - 1
        return create_format_line(list_words, count_words, count_spaces)
    else:
        return create_format_line(list_words, count_words, count_spaces)


def format_text(line: str, step: int):
    """ Преобразование строки в строки фиксированной длины.
        Если строка длинная, то переносим слова на новые строки.
        Для формирования визуального эффекта равенства строк, 
        добавляем пробелы между словами, если это необходимо.   

    Args:
        line (str): строка текста
        step (int): длина новой строки

    Returns:
        list: список новых строк
    """
    length_line = len(line)
    out_lines = []

    start_step = 0
    finish_step = start_step + step + 1
    while finish_step <= length_line:
        current_line = line[start_step:finish_step]
        start_step = search_start_line(current_line, finish_step-1, step)
        finish_step = start_step + step + 1
        out_lines.append(create_output_line(current_line, step) + "\n")
        
    current_line = line[start_step:length_line]
    out_lines.append(create_output_line(current_line, step, True) + "\n")
    return out_lines


def input_step(min_width: int) -> int:
    """Обработка ввода длины строки

    Args:
        min_width (int): минимальная длина строки

    Returns:
        int: длина строки
    """
    while True:
        width = input("Введите максимальное количество символов в строке (не менее 35): ")
        try:
            width = int(width)
        except ValueError:
            print("Некорректно введен параметр! Попробуйте ещё раз.")
            continue
        
        if width > min_width:
            break
        print("Введите число больше ", min_width, "!", sep="")
    return width

def main():
    min_width_line = 35
    step = input_step(min_width_line)

    with (open(r"Tasks/Stuk/Task_3/text.txt", "r", encoding="utf-8") as file_in, 
          open(r"Tasks/Stuk/Task_3/text_out.txt", "w", encoding="utf-8") as file_out):
        for line in file_in:
            try:
                out_lines = format_text(line, step)
            except ValueError as err:
                print(err)
                return
            file_out.writelines(out_lines)
    print("Операция выполнена успешно!")

main()

