def prime_number(num):
    num = int(input("Enter the number :  "))

    if num == 1:
          print("Not Prime")
    
    if num > 1:
         for n in range (2,num):
              if num % 2 == 0:
                   return "Not Prime"
              elif num == 2:
                   return "Prime"
              elif num <= 2:
                   return "Not Prime"
         else:
              for i in range (3, int(num**0.5) + 1, 2):
                   if num % i == 0:
                        return "Not Prime"
              return "Prime"

if __name__ == '__main__':
    print(prime_number(11)) # "Prime"
    print(prime_number(13)) # "Prime"
    print(prime_number(17)) # "Prime"
    print(prime_number(20)) # "Not Prime"
    print(prime_number(35)) # "Not Prime"