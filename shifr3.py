file = open('code.txt', 'r')
str2 = file.read()
str2 = str2.lower()
str2 = 'winter, ���������, ���������.'
file = open('text1.txt', 'r')

# ��������� ����� �������� �� ����� �� �����
#data = file.read()


# ������� ����� ������� �� ����
#file1.write(data)

#file1.close()  # �������������, �� ������� �����


class Foo(object):
    def __init__(self, name):
       self.name = name
  
    def __str__(self):
       return '%s' % self.name

a = '��������������������������������!.,?-:;"()0123456789'
b = Foo(a)
strr= ''
for i in range(len(str2)):
    if a.find(str2[i])!= -1 and strr.find(str2[i])==-1:
        strr += str(Foo(str2[i]))
for i in range(len(a)):
    if strr.find(a[i])== -1:
        strr += str(Foo(a[i]))
        
#strr = str(b)
print(strr)
a = strr
def kod(file):
    file1 = open('text.txt', 'w')
    for line in file:
        for i in range(len(line)):
            pos = strr.find(line[i])
            if pos>-1:
                file1.write(strr[len(strr) - pos - 1])
                print(strr[len(strr) - pos - 1])
            else:
                file1.write(line[i])
                print(line[i])

def dekod(file):
    file1 = open('text2.txt', 'w')
    for line in file:
        for i in range(len(line)):
            pos = a.find(line[i])
            if pos>-1:
                file1.write(a[len(strr) - pos - 1])
                print(a[len(strr) - pos - 1])
            else:
                file1.write(line[i])
                print(line[i])
                
print('0 - kod, 1 - dekod')
d = int(input())
if d == 0:
    kod(file)
elif d == 1:
    dekod(file)
print("finish")
        


