def find_word(f, word):
    g_index = 0  # Глобальный индекс (позиция в тексте)
    count_strok = 0
    for line in f:  # Чтение файла построчно
        count_strok += 1

        index = 0  # Локальный индекс для текущей строки
        while index != -1:
            index = line.find(word, index)  # Поиск слова в строке
            if index > -1:
                yield g_index + index  # Возврат глобальной позиции вхождения
                index += 1  # Смещение для поиска следующего вхождения
        g_index += len(line)  # Увеличиваем глобальный индекс на длину строки

    print(count_strok)


# Основная часть программы
try:
    with open("l.txt", encoding="utf-8") as file:  # Открытие файла
        a = find_word(file, "генератор")  # Поиск слова "генератор"
        print(list(a))  # Преобразование генератора в список и вывод
except FileNotFoundError:
    print("Файл не найден")  # Если файл не найден
except:
    print("Ошибка обработки файла!")  # Любая другая ошибка
