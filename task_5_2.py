n = int(input())
suma = 0
mult = 1
 
while n > 0:
    digit = n % 10
    suma = suma + digit
    mult = mult * digit
    n = n // 10
 
print(f'Сумма:{suma}')
print(f'Произведение:{mult}')