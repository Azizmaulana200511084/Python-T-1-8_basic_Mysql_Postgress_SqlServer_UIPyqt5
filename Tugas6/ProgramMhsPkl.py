print ("\n\t\t||========================================||\n\t\t|| Program Mendata Mahasiswa Yang Ikut PKL||\n\t\t||****Universitas Muhammadiyah Cirebon****||\n\t\t||========================================||") #Aziz Maulana(200511084) R4 Semester 3
aziz_maulana = open("document_mahasiswa_pkl.txt", "r+")
teks = aziz_maulana.read()
print(teks)
while True:
    try:
        na = input("Masukan Nama\t\t\t\t: ")
        ni = int(input("Masukan Nomor Nim\t\t\t: "))
        no = int(input("Masukan Nomor Handphone\t\t\t: "))
        fap = input("Dari Fakultas beserta Prodi mana\t: ")
        alp = input("Masukan Alamat PKL\t\t\t: ")
        dolp = input("Masukan Nama Dosen Pendamping Lapangan\t: ")
        break
    except:
        print("Maaf yang anda masukan bukan nomor...!\n")
teks = "\nNama                          : {}\nNim                           : {}\nNo.Hp                         : {}\nFakultas & Prodi              : {}\nAlamat Praktik Kerja Lapangan : {}\nDosen Pendamping Lapangan     : {}\n\t\t\t".format(na, ni, no, fap, alp, dolp)
aziz_maulana.write(teks)
aziz_maulana.close()
####################################################################
#Aziz Maulana
#200511084
#Kelas R4
#Teknik Informatika
###################################################################