def full_prima(N):
    if N == 1:
          print("True")
    
    if N > 1:
         for n in range (2,N):
              if N % 2 == 0:
                   return "True"
              elif N == 2:
                   return "True"
              elif N <= 2:
                   return "False"
         else:
              for i in range (3, int(N**0.5) + 1, 2):
                   if N % i == 0:
                        return "False"
                   if N % i <=3:
                        return "True"
              return "True"

    return ''

if __name__ == '__main__':
    print(full_prima(2)) # True
    print(full_prima(3)) # True
    print(full_prima(11)) # False
    print(full_prima(13)) # False
    print(full_prima(23)) # True
    print(full_prima(29)) # False
    print(full_prima(37)) # True
    print(full_prima(41)) # False
    print(full_prima(43)) # False
    print(full_prima(53)) # True