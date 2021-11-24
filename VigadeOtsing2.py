print("*** IGRI S CHISLAMI ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = (abs(int(input("Vvedite celoe chislo => ")))) #добавлены скобки и все строки переставлены на правильную позицию
        break
    except ValueError:
        print("Eto ne celoe chislo")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Net smisla nichego delat s nulem")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Opredelyaem, skolko v chisle chetnih i skolko nechetnih cifr")
print()
c==b==a
paaris ==0
paaritu == 0
while b > 0:
    if b % 2 == 0:
        paaris =+ 1
    else:
        paaritu =+ 1
b = b // 10   
print("Chetnih cifr:", paaris)
print("Nechetnih cifr:", paaritu)
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("*Perevorachivaem* vvedenoe chislo")
print()
b=0
while a > 0:
        number = a % 10
        a = a // 10
        b = b * 10
        b =+ number
print("*Perevernutoe* chislo", b)
print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("Proveryaem gipotezu Sirakuz")
print()
if c % 2 == 0:
        print("c - chetnoe chislo. Delim na 2.")
else:
        print("c - nechetnoe chislo. Umnozhaem na 3, pribavlyaem 1 i delim na 2.")
while c != 1:
            if c % 2 == 0:
                    c == c / 2
            else:
                    c == (3*c + 1) / 2
            print(c, end=" ")
print()
print("Gipoteza verna")

