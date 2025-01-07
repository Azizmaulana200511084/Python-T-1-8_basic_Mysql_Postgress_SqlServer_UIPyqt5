print("      <<<Volume & Luas Permukaan Kerucut>>>")
print("<<<<Mahasiswa Universitas Muhammadiyah Cirebon>>>>")

import math
tinggi=int(input("Input Tinggi \t\t\t: "))
jari=int(input("Input Jari-jari Lingkaran \t: "))

phi=22/7
pelukis=math.sqrt((jari*jari)+(tinggi*tinggi))
luas=int(phi*jari*(jari+pelukis))
volume=int((1/3)*phi*(jari*jari)*tinggi)

print("\nHasil nya kuyy..................:")
print ("Volume Kerucut \t\t\t= ", volume)
print ("Luas Kerucut \t\t\t= ", luas)
print("Jangan lupa bahagiaaaa.................")