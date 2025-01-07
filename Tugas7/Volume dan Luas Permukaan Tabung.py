Tinggi = int(input("Masukan Tinggi Tabung\t\t: "))
import math
class Tabung():
  def __init__(aziz, tinggi, jari_Jari):
    aziz.TinggiAziz = tinggi
    aziz.JariMaulana = jari_Jari
  def luas(aziz):
    return int(2*3.14*aziz.JariMaulana*(aziz.TinggiAziz+aziz.JariMaulana))
  def volume(aziz):
    return int((3.14*(aziz.JariMaulana*aziz.JariMaulana))*aziz.TinggiAziz)
jari_jari = int(input("Masukan Jari-jari Tabung\t: "))
maulana = Tabung(Tinggi,jari_jari)
Volume = maulana.volume()
Luas = maulana.luas()
print ("\nVolume Tabung\t\t\t: ",Volume)
print("Luas Tabung\t\t\t: ",Luas)