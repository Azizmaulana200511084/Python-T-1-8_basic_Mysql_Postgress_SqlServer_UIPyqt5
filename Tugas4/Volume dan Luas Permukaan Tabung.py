def luas_tabung(jari,tinggi):
    phi=22/7
    luas=int(2*phi*jari*(tinggi+jari))
    return luas
def volume_tabung(jari,tinggi):
    phi=22/7
    volume=int((phi*(jari*jari))*tinggi)
    return volume

def luas_volume_tabung():
    print("      <<<Volume & Luas Permukaan Tabung>>>")
    print("<<<<Mahasiswa Universitas Muhammadiyah Cirebon>>>>")
    tinggi=int(input("\nMasukan Tinggi \t\t\t: "))
    jari=int(input("Masukan Jari-jari Lingkaran \t: "))
    print("\nHasil nya kuyy..........:")
    print ("Volume Tabung \t\t\t= ",volume_tabung(jari,tinggi))
    print ("Luas Tabung \t\t\t= ",luas_tabung(jari,tinggi))
    print("Jangan lupa bahagiaaaa........................")
luas_volume_tabung()