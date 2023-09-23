import random
def a(m,n):
   ma=[]
   for i in range(m):
        r=[]
        for j in range(n):           
            a=int(random.uniform(0, 9))
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
    return max(mx) #возвращаем максимальную сумму из массива
#данная функция выявляет сумму по строкам
def mst(arr,q,qq):
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
#данная функция выявляет сумму по столбцам

#эта хуйня просит ввести количество строк и столбцов ака матрица m*n

m=int(input('Вводи, а то как в прошлый раз '))
n=int(input('Вводи, а то как в прошлый раз '))
a=a(m,n)

        
mxs=0
mxst=0
#максимальный элемент по строкам и столбцам
mxs=ms(a,m,n)
mxst=mst(a,m,n)
p(a,m,n)
print(f'Сумма по сторокам {mxs},Сумма по столбцам {mxst}')



