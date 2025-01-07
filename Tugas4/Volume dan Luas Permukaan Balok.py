def luas_permukaan_balok(p,l,t):
    L = 2 * ( (p*l) + (p*t) + (l*t) )
    return L
def volume_balok(p,l,t):
    V = p * l * t
    return V

def luas_volume_balok():
    print("          <<<Volume Dan Luas Balok>>>")
    print("<<<<Mahasiswa Universitas Muhammadiyah Cirebon>>>>")
    p=int(input('\nMasukan panjang balok \t: '))
    l=int(input('Masukan lebar balok \t: '))
    t=int(input('Masukan tinggi balok \t: '))
    print("\nHasil nya kuyy..........:")
    print('Balok tersebut dengan ukuran panjang:{}, lebar:{}, tinggi:{} \nMempunyai luas:{} , volume:{}'.format(p,l,t, luas_permukaan_balok(p,l,t), volume_balok(p,l,t)))
    print("Jangan lupa bahagiaaaa.....................................")
luas_volume_balok()