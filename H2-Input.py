# input

nama = input("masukan nama kamu: ")
usia = int(input("masukan usia kamu"))
hobi = input("apa hobi kamu: ")
# \n => new line
print(f"data diri\nnama: {nama}\nusia:{usia}\nhobi:{hobi}")

# control flow
# aritmetika
a = 10
b = 5
print(a + b) # operator tambah (+)
print(a - b) # operator kurang (-)
print(a / b) # operator bagi (/)
print(a * b) # operator kali (*)
print(a ** b) # operator pangkat (**)
print(a % b) # operator sisa hasil bagi/modulus (%)

phi = 3.14
r = 7 
luas_lingkaran = phi * (r ** 2)
print("luas_lingkaran: ", luas_lingkaran)

# operator comparison
print(a > b) # True
print(a < b) # False
print(a >= b) # True
print(a <= b) # False
print(a == b) # False
print(a != b) # True

# logical operator (and , or , not)
print(a > b and a >= b) # true dan true
print(a > b and a < b) # true dan false
print(a > b or a < b) # true atau false
print(not(a > b and a >= b)) # ini akan false

