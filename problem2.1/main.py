bilangan = int(input("masukkan angka =  "))

def faktorial(bilangan):
    for i in range (1 , (bilangan + 1)):
        if bilangan % i == 0:
            print (i)

print(faktorial(bilangan))