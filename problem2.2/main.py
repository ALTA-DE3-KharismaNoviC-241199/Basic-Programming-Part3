bilangan = int(input("masukkan angka =  "))

faktorial = [ ]
for i in range (1 , bilangan + 1):
        if bilangan % i == 0:
            faktorial.append(i)

print("faktorial dari" , bilangan , "sebagai berikut" )
for i in range(len(faktorial)-1,-1,-1):
        print(faktorial[i])