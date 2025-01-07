Alas = int(input("\nMasukan Alas \t\t=> "))
Tinggi = int(input("Masukan Tinggi \t\t=> "))
A = int(input("Masukan sisi pertama \t=> "))
B = int(input("Masukan sisi kedua \t=> "))
C = int(input("Masukan sisi ketiga \t=> "))
class Segitiga:
  def __init__(maulana,aziz,Maulana,a,b,c):
    maulana.alas = aziz
    maulana.tinggi = Maulana
    maulana.a = a
    maulana.b = b
    maulana.c = c
  def Luas(maulana):
    return 0.5*(maulana.alas*maulana.tinggi)
  def Keliling(maulana):
    return (maulana.a + maulana.b + maulana.c)
Maulana = Segitiga(Alas,Tinggi,A,B,C)
keliling = Maulana.Keliling()
luas = Maulana.Luas()
print("\nLuas Segitiga\t\t= ",luas)
print ("Keliling Segitiga\t= ",keliling)