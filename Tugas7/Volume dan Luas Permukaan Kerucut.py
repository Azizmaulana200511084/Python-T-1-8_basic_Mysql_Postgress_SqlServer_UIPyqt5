Tinggi = int(input("Masukan Tinggi Kerucut\t\t: "))
import math
class Kerucut():
  def __init__(aziz, tinggi, jari_Jari):
    aziz.TinggiAziz = tinggi
    aziz.JariMaulana = jari_Jari
  def luas(aziz):
    pelukis=math.sqrt((aziz.JariMaulana*aziz.JariMaulana)+(aziz.TinggiAziz*aziz.TinggiAziz))
    luas=int(3.14*aziz.JariMaulana*(aziz.JariMaulana+pelukis))
    return luas
  def volume(aziz):
    volume=int((1/3)*3.14*(aziz.JariMaulana*aziz.JariMaulana)*aziz.TinggiAziz)
    return volume
jari_jari = int(input("Masukan Jari-jari Kerucut\t: "))
maulana = Kerucut(Tinggi,jari_jari)
Volume = maulana.volume()
Luas = maulana.luas()
print ("\nVolume Kerucut\t\t\t: ",Volume)
print("Luas Kerucut\t\t\t: ",Luas)