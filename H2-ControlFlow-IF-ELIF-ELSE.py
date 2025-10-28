# control flow if

"""
if (kondisi => True):
    blok kode yang akan dieksekusi
"""

nilai_siswa = 90
if nilai_siswa >= 90: # ini true
    print("grade A")

# if else
nilai_siswa = 85 

if nilai_siswa >= 90:
    print("grade A")
else:
    print("kurang gacor cuy")

# if elif else
nilai_siswa = int(input("masukan nilai kamu: "))

if nilai_siswa >= 90:
    print("grade A")
elif nilai_siswa < 90 and nilai_siswa >= 80:
    print("grade B")
elif nilai_siswa < 80 and nilai_siswa >= 70:
    print("grade C")
else:
    print("kurang gacorrrr cuy")

# lower, upper
teks = "saya ingin belajar bahasa python"
print(teks.lower())
print(teks.upper())
print(teks.capitalize())

nilai = 10 

# increment 
nilai += 3 # => nilai = 10 + 3
print(nilai)

