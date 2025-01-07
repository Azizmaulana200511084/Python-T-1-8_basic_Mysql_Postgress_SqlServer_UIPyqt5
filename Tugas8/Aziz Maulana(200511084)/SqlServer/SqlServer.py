import pyodbc
import os
D = "Sql Server Native Client 11.0"
S = "AZIZ-MAULANA"
Da = "kipasanangin"
T = "yes"
try:
    db = pyodbc.connect(Driver = D, Server = S, Database = Da, Trusted_Connection = T)
    print("\nServer Telah Terkoneksi Di Database\n")
except:
    print("\nServer Belum Terkoneksi Di Database\n")
cur = db.cursor()
def create_tabel(db):
    cur.execute("""
                CREATE TABLE Universitas
                (
                  Nim INT,
                  Nama VARCHAR(100),
                  JenisKelamin VARCHAR(100),
                  Prodi VARCHAR(100));
                    """)
    db.commit()
    print("Selamat Anda Telah Berhasil Membuat Tabel...")
def insert_data(db):
  Nim = input("\nMasukan Nim: ")
  Nama = input("Masukan Nama: ")
  JenisKelamin = input("Masukan Jenis Kelamin: ")
  Prodi = input("Dari ProgramStudi Mana: ")
  val = (Nim, Nama, JenisKelamin, Prodi)
  cursor = db.cursor()
  cursor.execute(
        "insert into Universitas (Nim, Nama, JenisKelamin, Prodi) values(?,?,?,?)",
        (val))
  db.commit()
  print("{} Selamat Data Telah Tersimpan".format(cursor.rowcount))
def show_data(db):
  cursor = db.cursor()
  cursor.execute("select * from Universitas")
  for row in cursor:
        print(f'{row}')
def update_data(db):
  show_data(db)
  Nim = input("\nPilih Nim> ")
  Nama = input("Nama baru: ")
  JenisKelamin = input("Masukan Jenis Kelamin: ")
  Prodi = input("Dari ProgramStudy Mana: ")
  val = (Nama, JenisKelamin, Prodi, Nim)
  cursor = db.cursor()
  cursor.execute(
        "update Universitas set Nama=?, JenisKelamin=?, Prodi=? where Nim=?",
        (val))
  db.commit()
  print("{} Selamat Data Telah Tersimpan".format(cursor.rowcount))
def delete_data(db):
  cursor = db.cursor()
  show_data(db)
  Nim = input("\nPilih Nim> ")
  val = (Nim)
  cursor.execute(
        "delete from Universitas where Nim=?",
        (val))
  db.commit()
  print("{} Selamat Data Telah Terhapus".format(cursor.rowcount))
def show_menu(db):
  print("\n=== APLIKASI DATABASE PYTHON ===")
  print("1. Membuat Tabel Universitas")
  print("2. Insert Data")
  print("3. Tampilkan Data")
  print("4. Update Data")
  print("5. Hapus Data")
  print("0. Keluar")
  print("------------------")
  menu = input("Pilih menu> ")
  os.system("cls")
  if menu == "1":
    create_tabel(db)
  elif menu == "2":
    insert_data(db)
  elif menu == "3":
    show_data(db)
  elif menu == "4":
    update_data(db)
  elif menu == "5":
    delete_data(db)
  elif menu == "0":
    exit()
  else:
    print("Menu salah!")
if __name__ == "__main__":
  while(True):
    show_menu(db)