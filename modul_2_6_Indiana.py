import random
n = random.randint (3, 20) # случайное число от 3 до 20

print('Тебе выпал камень с числом: ', n)
password = []
for i in range (1, n-1):
    for j in range (i+1, n ) :
        summ = i+j
        if n % summ == 0:
            password.append(i) # первое число пары
            password.append(j) # второе число пары
print ('Твой пароль :')
print (*password)

