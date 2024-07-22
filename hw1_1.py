l1 = ' '
s1 = '*'
n = int(input('Введите число строк'))
for i in range(1,n+1):
    s=s1+(i-1)*s1*2
    l=(n-i)*l1
    print(l+s)
