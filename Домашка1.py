import random
def p(arr,q):
    for i in range(q):
        for j in range(q):
            print(arr[i][j], end=' ')
        print()
        #ну тут все просто вывод массива
def ms(arr,q):
    ms=0 #сумма по строкам
    mx=[] # массив сумм 
    for i in range(q):
        for j in range(q):
            ms+=arr[i][j]
        mx+=[ms] #добавляем сумму в массив
        ms=0                
    return max(mx) #возвращаем максимальную сумму из массива
#данная функция выявляет сумму по строкам
def mst(arr,q):
    ms=0 #сумма по столбацам
    mx=[] # массив сумм
    k=0
    while k<q:
        for i in range(q):
            ms+=arr[i][k]
        mx+=[ms]#добавляем
        ms=0
        k+=1 #повышаем индекс столбца
    
                   
    return max(mx) #возвращаем максимальную сумму из массива
#данная функция выявляет сумму по столбцам


m=int(input('Вводи, а то как в прошлый раз '))
#эта хуйня просит ввести количество строк и столбцов ака матрица m*n
a=[[0 for i in range(m)] for j in range(m)]
for i in range(m):
    for j in range(m):
        a[i][j]=int(random.uniform(0, 9))
        # здесь крч мы создаём эту ссаную матрицу размером m*m и заполняем
        # рандомными цифрами от 0 до 9
        #ну я хз какой диапозон чиел тебе нужен меняй если чо в рандоме 
        
mxs=0
mxst=0
#максимальный элемент по строкам и столбцам
mxs=ms(a,m)
mxst=mst(a,m)
p(a,m)
print(f'Сумма по сторокам {mxs},Сумма по столбцам {mxst}')



