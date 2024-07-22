try:
    n = int (input ('Vvedite chislo: '))
    while n > 9:
        n = sum([int(i) for i in str(n)])
    print('Final summ:', n)
except Exception:
        print ('incorrect inpur')