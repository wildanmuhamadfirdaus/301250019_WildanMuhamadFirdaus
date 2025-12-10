# Import modul yang diperlukan
from datetime import datetime

# SOAL 1: Menyimpan dan Membaca Biodata
def soal_1():
    # 1. Minta input dari pengguna
    nama  = input("Masukkan Nama: ")
    nim   = input("Masukkan NIM: ")
    prodi = input("Masukkan Prodi: ")
    
    # 2. Simpan data ke file biodata.txt (mode 'w' = tulis baru, akan menimpa jika sudah ada)
    with open('biodata.txt', 'w') as file:
        # Tulis dalam format: Nama,NIM,Prodi
        file.write(f"{nama},{nim},{prodi}\n")
    
    # 3. Baca kembali file tersebut
    with open('biodata.txt', 'r') as file:
        # Baca seluruh isi file dan hapus spasi/enter di akhir
        data = file.read().strip()
        # Pecah string berdasarkan koma menjadi list
        bagian = data.split(',')
        
        # Ambil masing-masing nilai
        nama_baca  = bagian[0]
        nim_baca   = bagian[1]
        prodi_baca = bagian[2]
    
    print("Nama: ", nama_baca)
    print("NIM: ", nim_baca)
    print("Prodi: ", prodi_baca)

# SOAL 2: Log Aktivitas Sederhana (Append Mode)
def soal_2():
    # 1. Ambil waktu saat ini
    waktu_sekarang = datetime.now()
    # Format waktu menjadi [HH:MM]
    waktu_format = waktu_sekarang.strftime("%H:%M")
    
    # 2. Buat baris log yang akan ditulis
    baris_log = f"[{waktu_format}] Program dijalankan\n"
    
    # 3. Tulis ke file log.txt dengan mode 'a' (append = tambah di akhir file)
    with open('log.txt', 'a') as file:
        file.write(baris_log)

# SOAL 3: Rekap Nilai Mahasiswa (Format CSV Sederhana)
def soal_3():
    # 1. Minta jumlah mahasiswa
    jumlah = int(input("Masukkan jumlah mahasiswa: "))
    
    # 2. Buat file baru untuk menyimpan data (mode 'w')
    with open('nilai_mahasiswa.txt', 'w') as file:
        for i in range(jumlah):
            print(f"\nMahasiswa ke-{i+1}")
            nama   = input("Nama          : ")
            tugas  = int(input("Nilai Tugas   : "))
            uts    = int(input("Nilai UTS     : "))
            uas    = int(input("Nilai UAS     : "))
            
            # Tulis ke file dalam format CSV
            file.write(f"{nama},{tugas},{uts},{uas}\n")
    
    # 3. Baca kembali file dan hitung rekap
    daftar_mahasiswa = []
    with open('nilai_mahasiswa.txt', 'r') as file:
        for baris in file:
            # Hapus enter dan pecah berdasarkan koma
            data = baris.strip().split(',')
            nama   = data[0]
            tugas  = int(data[1])
            uts    = int(data[2])
            uas    = int(data[3])
            
            # Hitung rata-rata
            rata_rata = (tugas + uts + uas) / 3
            
            # Simpan sebagai tuple
            daftar_mahasiswa.append((nama, tugas, uts, uas, rata_rata))
    
    # 4. Tampilkan rekap dalam format yang diminta
    print("\n=== REKAP NILAI MAHASISWA ===")
    print("Nama\t\tTugas\tUTS\tUAS\tRata-rata")
    for nama, tugas, uts, uas, rata in daftar_mahasiswa:
        print(f"{nama}\t{tugas}\t{uts}\t{uas}\t{rata:.2f}")

# Bagian utama program (jalankan semua soal)
if __name__ == "__main__":
    print("=== MENYIMPAN DAN MEMBACA BIODATA ===")
    soal_1()
    
    print("\n=== LOG AKTIVITAS SEDERHANA ===")
    soal_2()
    
    print("\n=== REKAP NILAI MAHASISWA ===")
    soal_3()