file = open('code.txt', 'r')
str = file.read()
str = str.lower()
b = ''
dict = {}
matr = []
matr1 = []
for i in range(97,123):
    b += (chr(i))
a = b.replace('j','')
print("alphabet")
print(a)

ii=0
jj=0
kol = len(str)
for i in range (kol):
  if ii> 4:
      matr.append(matr1)
      matr1 = []
      ii = 0
      jj+=1
  if a.find(str[i])!=-1:
      matr1.append(str[i])
      dict[str[i]] = ii * 10 + jj
      a = a.replace(str[i],'')
      ii+=1
kol = len(a)

for i in range (kol):
  if ii> 4:
      matr.append(matr1)
      matr1 = []
      ii = 0
      jj+=1
  matr1.append(a[0])
  dict[a[0]] = ii * 10+ jj
  a = a.replace(a[0],'')
  ii+=1

matr.append(matr1)
file1 = open('message.txt', 'r')
print(matr)
STROKA = file1.read()
STROKA = STROKA.lower()
STROKA = STROKA.replace('j','i')
i = 0
num = 0

while i <len(STROKA):
  if b.find(STROKA[i])== -1:
    STROKA = STROKA.replace(STROKA[i],'')
  else:
      i+=1
    
newstr = ''
itog = ''
for i in range(len(STROKA)):
    zn = dict[STROKA[i]]
    zn2 = zn / 10
    zn1 = zn % 10
    num = i % 4
    if num == 0:
        if zn1 ==4: zn1 = -1
        newstr = matr[zn1+1][zn2]
    elif num == 1:   
        newstr = matr[zn1][zn2-1]
    elif num == 2:    
        newstr= matr[zn1-1 ][zn2]
    elif num == 3:
        if zn2 ==4: zn2 = -1
        newstr= matr[zn1 ][zn2+1]
    itog += newstr
       
print(itog)
file2 = open('itog.txt', 'w')
file2.write(itog)
