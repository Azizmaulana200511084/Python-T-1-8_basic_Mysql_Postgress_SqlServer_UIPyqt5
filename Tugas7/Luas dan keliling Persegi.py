Panjang = int(input("Masukan Panjang\t: "))
Lebar = int(input("Masukan Lebar\t: "))
Aziz = (Panjang)
Maulana = (Lebar)
class Persegi:
  def __init__(self, panjang, lebar):
    self.panjang = panjang
    self.lebar = lebar
  def keliling(self):
    return 2 * (self.panjang + self.lebar)
  def luas(self):
    return self.panjang * self.lebar
maulana = Persegi(Aziz,Maulana)
ObjKeliling = maulana.keliling()
ObjLuas = maulana.luas()
print("\nLuas Persegi\t: ",ObjLuas)
print ("Keliling Persegi: ",ObjKeliling)