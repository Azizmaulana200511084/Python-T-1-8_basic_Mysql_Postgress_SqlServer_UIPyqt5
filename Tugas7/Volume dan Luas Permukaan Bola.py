import math
class Bola():
  def __init__(aziz, jari_Jari):
    aziz.JariMaulana = jari_Jari
  def luas(aziz):
    return int(4*3.14*(aziz.JariMaulana*aziz.JariMaulana))
  def volume(aziz):
    return int((4/3)*3.14*(aziz.JariMaulana*aziz.JariMaulana*aziz.JariMaulana))
jari_jari = int(input("Masukan jari-jari\t: "))
Volume = Bola(jari_jari)
Luas = Bola(jari_jari)
print("\nVolume Bola\t\t: %0.2f" % Volume.volume())
print("Luas Bola\t\t: %0.2f" % Luas.luas())