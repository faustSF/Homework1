import random
def fm1(m,q):
    for i in range(q):
        m+=[int(random.randint(0, 9))]
        #аполняет множество 1 числами от 0 до 9
def fm2(m,q):
    for i in range(q):
        m+=[int(random.randint(0, 9))]
        #аполняет множество 2 числами от 0 до 9
def find(m1,m2,k1,k2):
    o=[] # создаём массив общих элементов
    for i in range(k1):
        for j in range(k2):
            if m1[i]==m2[j]: #если они равны
                o+=[m1[i]]   #то добавляем
    return o
    

k1=int(input('вводи количество элементов первого монжества '))
k2=int(input('вводи количество элементов второго монжества '))
m1=[k1]
m2=[k2]
#множества 1 и 2

fm1(m1,k1)
fm2(m2,k2)
o=find(m1,m2,k1,k2)
print(m1)
print(m2)
print(o)
