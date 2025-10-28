# Encapsulation
# => menyembunyikan data (atribut) agar tidak bisa diakses secara bebas dari luar kelas
# biasanya digunakan agar tidak sembarangan di ubah dari luar kelas

class AkunBank:
    # atribut2
    def __init__ (self, nama, saldo):
        self.nama = nama # atribut publik
        self.__saldo = saldo # atribut private
        # ketika kita membuat __ di depan atribut ia akan bersifat private

    # method setter dan getter
    def setSaldo(self, saldo):
        self.__saldo = saldo

    def getSaldo(self):
        return self.__saldo
        

# buat object
akun1 = AkunBank("heri", 8000)
akun1.setSaldo(9000)
print("saldo akun pertama: ", akun1.getSaldo())
# print(akun1.saldo)


