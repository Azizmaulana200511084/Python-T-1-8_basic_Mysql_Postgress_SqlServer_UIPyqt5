#Aziz Maulana
#Nim 200511084
#Kelas R4
mk = []
xbreak = False
aziz = 0
while(not xbreak):
    mata_kuliah = input("Masukkan nama matakuliah ke-{}: ".format(aziz))
    mk.append(mata_kuliah)
    aziz += 1
    tanya = input("Mau isi lagi? (y/t): ")
    if(tanya == "t"): 
        xbreak = True
print ("=" * 10)
print ("Kamu memiliki {} matakuliah".format(len(mk)))
for kuliah in mk:
    print ("- {}".format(kuliah))
#Teknik Informatika Universitas Muhammadiyah Cirebon