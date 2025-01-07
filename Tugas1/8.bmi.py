print("      <<<Berat badan,tinggi,ideal (BMI)>>>")
print("<<<<Mahasiswa Universitas Muhammadiyah Cirebon>>>>")

bb = input("Berapa berat badan anda \t: ")
bbKonversi = int(bb)
tb = input("Berapa tinggi badan anda \t: ")
tbKonversi = float(tb)
rumusTb = tbKonversi / 100
kuadrat_tb = (rumusTb ** 2)
hasil = bbKonversi / kuadrat_tb

print("\nHasil nya kuyy..................:", hasil)
if hasil < 18.5:
    print("\t<<<<<Banyakin makan atuh>>>>>")
elif (hasil >= 18.5 and hasil <= 24.9):
    print("\t\t<<<<<Normal>>>>>")
elif (hasil >= 25 and hasil <= 29.9):
    print("\t<<<<<Mulai gendutan, minggu depan harus diet yah>>>>>")
elif hasil >= 30:
    print("\t<<<<<Wuaduhh bahaya kamu terlalu gendut amat bangeet>>>>>")
else:
    pass
print("Jangan lupa bahagiaaaa...........")