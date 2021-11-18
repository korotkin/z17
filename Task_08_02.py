"""
Task_08_02
Даны три слова. Выяснить, является ли хоть одно из них палиндромом
("перевертышем"), т. е. таким, которое читается одинаково слева направо и
справа налево. (Определить функцию, позволяющую распознавать слова
палиндромы.)
"""

def palindrome_words(word: str):
        palindrome = word[::-1]
        if word == palindrome:
            result = f"Слово {word} является палиндромом"
            return result
        else:
            result = f"Слово {word} не является палиндромом"
            return result


words = ["радар", "питон", "потоп", "школа", "довод"]
for word in words:
    result = palindrome_words(word)
    print(result)


