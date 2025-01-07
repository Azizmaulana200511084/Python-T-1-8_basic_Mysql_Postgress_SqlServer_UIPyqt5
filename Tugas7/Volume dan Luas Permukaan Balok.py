Panjang = int(input("\nMasukan Panjang \t=> "))
Lebar = int(input("Masukan Lebar \t\t=> "))
Tinggi = int(input("Masukan Tinggi \t\t=> "))
class Balok:
  def __init__(maulana,panjang,lebar,tinggi):
    maulana.aziz = panjang
    maulana.azizm = lebar
    maulana.lana = tinggi
  def Luas(maulana):
    return 2 * ((maulana.aziz*maulana.azizm) + (maulana.aziz*maulana.lana) + (maulana.azizm*maulana.lana))
  def Volume(maulana):
    return maulana.aziz * maulana.azizm * maulana.lana
Maulana = Balok(Panjang,Lebar,Tinggi)
volume = Maulana.Volume()
luas = Maulana.Luas()
print ("\nVolume Balok\t\t= ",volume)
print("Luas Balok\t\t= ",luas)