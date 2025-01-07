Berat = int(input("Masukan Berat Badan Anda\t: "))
Tinggi = float(input("Masukan Tinggi Badan Anda\t: "))
class BMI():
  def __init__(aziz, berat, tinggi):
    aziz.beratMaulana = berat
    aziz.tinggiMaulana = tinggi
  def bmi(aziz):
    maulana = aziz.tinggiMaulana / 100
    lana = (maulana ** 2)
    hasilnya = aziz.beratMaulana / lana
    return hasilnya
maulana = BMI(Berat,Tinggi)
Aziz = maulana.bmi()
print ("Hasil Body Mass Index Nya: ",Aziz)