import math

def luas_lingkaran(r):
    return math.pi*(r*r)
def keliling_lingkaran(r):
    return 2*(math.pi*r)

def luas_keliling_lingkaran():
    print("       <<<Luas & Keliling Lingkaran>>>")
    print("<<<<Mahasiswa Universitas Muhammadiyah Cirebon>>>>")
    r=int(input("\nMasukan Jari-jari \t: "))
    print("\nHasil nya kuyy..........:")
    print("Luas Lingkaran \t\t= ",luas_lingkaran(r))
    print("Keliling Lingkaran\t= ",keliling_lingkaran(r))
    print("Jangan lupa bahagiaaaa........................")
luas_keliling_lingkaran()