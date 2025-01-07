import math

def luas_kerucut(jari,tinggi):
    phi=22/7
    pelukis=math.sqrt((jari*jari)+(tinggi*tinggi))
    luas=int(phi*jari*(jari+pelukis))
    return luas
def volume_kerucut(jari,tinggi):
    phi=22/7
    volume=int((1/3)*phi*(jari*jari)*tinggi)
    return volume

def luas_volume_kerucut():
    print("      <<<Volume & Luas Permukaan Kerucut>>>")
    print("<<<<Mahasiswa Universitas Muhammadiyah Cirebon>>>>")
    tinggi=int(input("\nInput Tinggi \t\t\t: "))
    jari=int(input("Input Jari-jari Lingkaran \t: "))
    print("\nHasil nya kuyy..........:")
    print ("Volume Kerucut \t\t\t= ",volume_kerucut(jari,tinggi))
    print ("Luas Kerucut \t\t\t= ",luas_kerucut(jari,tinggi))
    print("Jangan lupa bahagiaaaa........................")
luas_volume_kerucut()