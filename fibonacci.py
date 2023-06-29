"""

Fibonacci

"""
a = 1
b = 1

fibonacci = [a,b]

sayi = int(input("Listede Kaç İndex Olmasını İstediğinizi Giriniz:"))

for i in range(1,sayi-1):
    a,b = b,a+b
    fibonacci.append(b)

print(fibonacci)