def luas_segitiga(a,t):
    return 0.5*(a*t)
def keliling_segitiga(b,c,d):
    return (b + c + d)

def luas_keliling_segitiga():
    print("       <<<Luas Dan Keliling Segitiga>>>")
    print("<<<<Mahasiswa Universitas Muhammadiyah Cirebon>>>>")
    a=int(input("\nMasukan Alas \t\t= "))
    t=int(input("Masukan Tinggi \t\t= "))
    b=int(input("Masukan sisi pertama \t= "))
    c=int(input("Masukan sisi kedua \t= "))
    d=int(input("Masukan sisi ketiga \t= "))
    print("\nHasil nya kuyy..........:")
    print("Luas Segitiga \t\t=",luas_segitiga(a,t))
    print("Keliling Segitiga \t=",keliling_segitiga(b,c,d))
    print("Jangan lupa bahagiaaaa.........")
luas_keliling_segitiga()