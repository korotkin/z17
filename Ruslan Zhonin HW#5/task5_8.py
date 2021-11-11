# В заданной строке расположить в обратном порядке все слова. Разделителями
# слов считаются пробелы

string = input('enter the string: ')

list_of_words = string.split(' ')
list_of_words.reverse()
reversed_string = ' '.join(list_of_words)
print(reversed_string)