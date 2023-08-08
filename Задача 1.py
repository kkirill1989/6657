#Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
#Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def kort(s: str) -> tuple:
    *a, b = s.split("/") 
    b, c = b.split(".")
    result = (a, b, c)
    return result

s = "D:/studying/GeekBrains/Python/Homeworks/work.txt"
print(kort(s))