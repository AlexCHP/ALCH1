def are_anagrams(str1, str2):
    # Удаляем знаки препинания и пробелы, приводим к нижнему регистру
    str1_cleaned = ''.join(c.lower() for c in str1 if c.isalnum())
    str2_cleaned = ''.join(c.lower() for c in str2 if c.isalnum())

    # Сортируем строки и сравниваем
    return sorted(str1_cleaned) == sorted(str2_cleaned)


string1 = input("Введите первую строку: ")
string2 = input("Введите вторую строку: ")

if are_anagrams(string1, string2):
    print("Эти строки являются анаграммами.")
else:
    print("Эти строки не являются анаграммами.")
