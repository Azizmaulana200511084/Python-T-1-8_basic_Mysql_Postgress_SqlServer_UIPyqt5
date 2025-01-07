import math

def luas_bola(jari):
    phi=22/7
    luas=int(4*phi*(jari*jari))
    return luas
def volume_bola(jari):
    phi=22/7
    volume=int((4/3)*phi*(jari*jari*jari))
    return volume

def luas_volume_bola():
    print("       <<<Luas & Permukaan Volume Bola>>>")
    print("<<<<Mahasiswa Universitas Muhammadiyah Cirebon>>>>")
    jari=int(input("\nInput Jari-jari Bola \t: "))
    print("\nHasil nya kuyy..........:")
    print ("Volume Bola \t\t\t= ",volume_bola(jari))
    print ("Luas Bola \t\t\t= ",luas_bola(jari))
    print("Jangan lupa bahagiaaaa........................")
luas_volume_bola()