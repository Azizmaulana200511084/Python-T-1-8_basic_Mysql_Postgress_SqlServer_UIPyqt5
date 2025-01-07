jari_jari = float(input("\nInput jari-jari\t\t: "))
import math
class Lingkaran():
  def __init__(aziz, jari_jari):
    aziz.jari = jari_jari
  def luas(aziz):
    return math.pi*(aziz.jari*aziz.jari)
  def keliling(aziz):
    return 2*(math.pi * aziz.jari)
Keliling = Lingkaran(jari_jari)
Luas = Lingkaran(jari_jari)
print("\nLuas Lingkaran\t\t: %0.2f" % Luas.luas())
print("Keliling Lingkaran\t: %0.2f" % Keliling.keliling())