numbers = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
ten = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
             "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
tens = ["", "десять ", "двадцать ", "тридцать ", "сорок ", "пятьдесят ", "шестьдесят ",
            "семьдесят ", "восемьдесят ", "девяносто "]
hundreds = ["", "сто ", "двести ", "триста ", "четыреста ", "пятьсот ", "шестьсот ",
                "семьсот ", "восемьсот ", "девятьсот "]
n=int(input('Введите число от 1 до 999 '))
while n<1 or n>999:
        print('Chislo nevernoe, vvedite zanovo')
        n = int(input('Введите число от 1 до 999 '))
else:
    n1=n//100
    n2=(n-n1*100)//10
    n3=n-(n1*100+n2*10)
    b1=hundreds[n1]
    b3=numbers[n3]
    if n2==1 and n3!=0:
        b23=ten[n3]
        print(b1+b23)
    else:
        b2 = tens[n2]
        print(b1+b2+b3)





















































