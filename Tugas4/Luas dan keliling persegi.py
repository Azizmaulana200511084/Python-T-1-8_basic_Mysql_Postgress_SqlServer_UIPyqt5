def luas_persegi(panjang,lebar):
    return panjang*lebar
def keliling_persegi(panjang,lebar):
    return 2*(panjang+lebar)

def luas_keliling_persegi():
    print("\t<<<Luas Dan Keliling Persegi>>>")
    print("<<<<Mahasiswa Universitas Muhammadiyah Cirebon>>>>")
    panjang=int(input('\nMasukkan panjang\t= '))
    lebar=int(input('Masukkan lebar\t\t= '))
    print('\nLuas persegi\t\t=',luas_persegi(panjang,lebar))
    print('Keliling persegi\t=',keliling_persegi(panjang,lebar))
    print("Jangan lupa bahagiaaaa.............................................")
luas_keliling_persegi()