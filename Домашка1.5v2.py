import random
def a(m,n):
   ma=[]
   for i in range(m):
        r=[]
        for j in range(n):           
            a=int(input(f'строка {i+1} cтолбец {j+1} '))
            r=r+[a]
        ma=ma+[r]
   return ma
        # здесь крч мы создаём эту ссаную матрицу размером m*m и заполняем
        # рандомными цифрами от 0 до 9
        #ну я хз какой диапозон чиел тебе нужен меняй если чо в рандоме 


def p(arr,q,qq):
    for i in range(q):
        for j in range(qq):
            print(arr[i][j], end=' ')
        print()
        #ну тут все просто вывод массива
def ms(arr,q,qq):
    ms=0 #сумма по строкам
    mx=[] # массив сумм 
    for i in range(q):
        for j in range(qq):
            ms+=arr[i][j]
        mx+=[ms] #добавляем сумму в массив
        ms=0                
    return max(mx)

def msx(arr,q,qq):
    ms=0 
    mx=[] 
    for i in range(q):
        for j in range(qq):
            ms+=arr[i][j]
        mx+=[ms] 
        ms=0                
    return mx

def istr(ar,k):
    return ar.index(k)
def ist(arr,k):
    return arr.index(k)

    
#данная функция выявляет сумму по строкам
def mstx(arr,q,qq):
    ms=0 #сумма по столбацам
    mx=[] # массив сумм
    k=0
    while k<qq:
        for i in range(q):
            ms+=arr[i][k]
        mx+=[ms]#добавляем
        ms=0
        k+=1 #повышаем индекс столбца
    
                   
    return max(mx) #возвращаем максимальную сумму из массива

def mstl(arr,q,qq):
    ms=0 
    mx=[]
    k=0
    while k<qq:
        for i in range(q):
            ms+=arr[i][k]
        mx+=[ms]
        ms=0
        k+=1
    
                   
    return mx


def prs(arr,j,q):
    print("Макс столбец")
    for i in range(q):
        print(a[i][j])

def prst(arr,i):
    print("Макс строка")
    print(arr[i])
        

        
        


#эта хуйня просит ввести количество строк и столбцов ака матрица m*n

m=int(input('Вводи, а то как в прошлый раз '))
n=int(input('Вводи, а то как в прошлый раз '))
a=a(m,n)
msx=msx(a,m,n)
mst=mstl(a,m,n)
        
mxs=0
mxst=0
#максимальный элемент по строкам и столбцам
mxs=ms(a,m,n)
mxst=mstx(a,m,n)

istr=istr(msx,mxs)
ist=ist(mst,mxst)
p(a,m,n)
#print(f'Сумма по сторокам {mxs},Сумма по столбцам ')
prst(a,istr)
prs(a,ist,m)





