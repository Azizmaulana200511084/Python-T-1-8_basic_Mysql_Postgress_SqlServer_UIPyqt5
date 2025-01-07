import psycopg2
import os
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "buka"
DB_HOST = "localhost"
DB_PORT = "5432"
try:
    db = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)
    print("\nServer Telah Terkoneksi Di Database\n")
except:
    print("\nServer Belum Terkoneksi Di Database\n")
cur = db.cursor()
def create_tabel(db):
    cur.execute("""
                CREATE TABLE Universitas
                (
                    Nim VARCHAR PRIMARY KEY NOT NULL,
                    Nama TEXT NOT NULL,
                    JenisKelamin TEXT NOT NULL,
                    Prodi TEXT NOT NULL
                    )
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
  sql = "INSERT INTO Universitas (Nim, Nama, JenisKelamin, Prodi) VALUES (%s, %s, %s, %s)"
  cursor.execute(sql, val)
  db.commit()
  print("{} Selamat Data Telah Tersimpan".format(cursor.rowcount))
def show_data(db):
  cursor = db.cursor()
  sql = "SELECT * FROM Universitas"
  cursor.execute(sql)
  results = cursor.fetchall()
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)
def update_data(db):
  cursor = db.cursor()
  show_data(db)
  Nim = input("\nPilih Nim> ")
  Nama = input("Nama baru: ")
  JenisKelamin = input("Masukan Jenis Kelamin: ")
  Prodi = input("Dari ProgramStudy Mana: ")
  sql = "UPDATE Universitas SET Nama=%s, JenisKelamin=%s, Prodi=%s WHERE Nim=%s"
  val = (Nama, JenisKelamin, Prodi, Nim)
  cursor.execute(sql, val)
  db.commit()
  print("{} Selamat Data Telah TerUpdate".format(cursor.rowcount))
def delete_data(db):
  cursor = db.cursor()
  show_data(db)
  Nim = input("\nPilih Nim> ")
  sql = "DELETE FROM Universitas WHERE Nim=%s"
  val = (Nim,)
  cursor.execute(sql, val)
  db.commit()
  print("{} Selamat Data Telah Terhapus".format(cursor.rowcount))
def search_data(db):
  cursor = db.cursor()
  keyword = input("Kata kunci: ")
  sql = "SELECT * FROM Universitas WHERE Nama LIKE %s OR Nim LIKE %s"
  val = ("%{}%".format(keyword), "%{}%".format(keyword))
  cursor.execute(sql, val)
  results = cursor.fetchall()
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)
def show_menu(db):
  print("\n=== APLIKASI DATABASE PYTHON ===")
  print("1. Membuat Tabel Universitas")
  print("2. Insert Data")
  print("3. Tampilkan Data")
  print("4. Update Data")
  print("5. Hapus Data")
  print("6. Cari Data")
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
  elif menu == "6":
    search_data(db)
  elif menu == "0":
    exit()
  else:
    print("Menu salah!")
if __name__ == "__main__":
  while(True):
    show_menu(db)