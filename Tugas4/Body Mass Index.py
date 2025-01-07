def bmi(berat,tinggi):
    data = berat / tinggi**2
    return data

def body_mass_index():
    print("      <<<Berat badan,tinggi,ideal (BMI)>>>")
    print("<<<<Mahasiswa Universitas Muhammadiyah Cirebon>>>>")
    berat=int(input("\nmasukan berat badan anda \t: "))
    tinggi=int(input("masukan tinggi badan anda \t: "))
    print("\nHasil nya kuyy..........:")
    print ("Hasil BMI \t\t\t= ",bmi(berat,tinggi))
    print("Jangan lupa bahagiaaaa........................")
body_mass_index()