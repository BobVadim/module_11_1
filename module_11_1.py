import requests
import numpy

r = requests.get('https://api.mixupload.org/genres')
print(r.content)
print(r.text)

file = 'file1.txt'
with open(file, 'r', encoding='utf-8') as f:
    s = f.read()
    print(s)

a = numpy.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[a < 5])
