# inheritance = Pewarisan
# => kemapuan sebuah kelas (anak) untuk mewarisi atribut dan method dari kelas lain (parent/induk) kasih akses
# => kita tidak perlu menuliskan ulang kode, cukup gunakan kode dari induk kelas

# parent kelas
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print(f" {self.nama} sedang makan")

# child/anak kelas
class Kucing(Hewan): # mewarisi dari hewan
    def suara(self):
        print(f"{self.nama} meong-meong")

# child/anak kelas
class Anjing(Hewan): # mewarisi dari hewan
    def suara(self):
        print(f"{self.nama} guk-guk")

# membuat object
mimi = Kucing("mimi")
mimi.makan()
mimi.suara()

# cek poliforfisme
leki = Anjing("Leki")
leki.suara()
mimi.suara()

