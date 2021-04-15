Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.path.mkdir
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    os.path.mkdir
AttributeError: module 'ntpath' has no attribute 'mkdir'
>>> os.path
<module 'ntpath' from 'C:\\Users\\ishit\\AppData\\Local\\Programs\\Python\\Python39\\lib\\ntpath.py'>
>>> os.mkdir("C:\Users\ishit\OneDrive\Desktop")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> os.mkdir("C:/Users/ishit/OneDrive/Desktop/python 1")
>>> os.getcwd()
'C:\\Users\\ishit\\AppData\\Local\\Programs\\Python\\Python39'
>>> os.path.exists("C:/Users/ishit/OneDrive/Desktop/python 1")
True
>>> os.path.splitext()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    os.path.splitext()
TypeError: splitext() missing 1 required positional argument: 'p'
>>> os.path.splitext("C:/Users/ishit/OneDrive/Desktop/python 1")
('C:/Users/ishit/OneDrive/Desktop/python 1', '')
>>> os.path.splitext("C:/Users/ishit/OneDrive/Desktop/python 1")
('C:/Users/ishit/OneDrive/Desktop/python 1', '')
>>> os.path.splitext("C:/Users/ishit/OneDrive/Desktop/python 1/ishita.txt")
('C:/Users/ishit/OneDrive/Desktop/python 1/ishita', '.txt')
>>> os.listdir("C:/Users/ishit/OneDrive/Desktop/python 1")
['Day 1 for python.py', 'Day 2 on python.py', 'ishita.txt', 'python-3.9.4-amd64.exe']
>>> root = os.path.splitext("C:/Users/ishit/OneDrive/Desktop/python 1/ishita.txt")
>>> root [0]
'C:/Users/ishit/OneDrive/Desktop/python 1/ishita'
>>> root [1]
'.txt'
>>> import shutile
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    import shutile
ModuleNotFoundError: No module named 'shutile'
>>> import shutil
>>> print("Before copying file:")
Before copying file:
>>> print(os.listdir("C:/Users/ishit/OneDrive/Desktop/python 1"))
['Day 1 for python.py', 'Day 2 for python.py', 'ishita.txt', 'python-3.9.4-amd64.exe']
>>> source = "C:/Users/ishit/OneDrive/Desktop/python 1/ishita.txt"
>>> destination = "C:/Users/ishit/OneDrive/Desktop/python 1/ishita1.txt"
>>> ishita = shutil.copy(source,destination)
>>> 