from abc import ABC, abstractmethod
from typing import List

# entitas
class Ruangan:
    def __init__(self, id_ruangan: str, nama: str, lantai: int, deskripsi: str):
        self.id_ruangan = id_ruangan
        self.nama = nama
        self.lantai = lantai
        self.deskripsi = deskripsi

    def __str__(self):
        return f"[{self.id_ruangan}] {self.nama} (Lantai {self.lantai}) - {self.deskripsi}"

class Denah:
    def __init__(self, nama_gedung: str):
        self.nama_gedung = nama_gedung
        self.daftar_ruangan: List[Ruangan] = []

    def tambah_ruangan(self, ruangan: Ruangan):
        self.daftar_ruangan.append(ruangan)


# Strategi Interface
class ViewStrategy(ABC):
    @abstractmethod
    def tampilkan_data(self, data) -> None:
        pass


# CONCRETE STRATEGY (Use Case: Melihat Denah Gedung)
class DenahViewStrategy(ViewStrategy):
    def tampilkan_data(self, denah: Denah) -> None:
        print(f"\nMenampilkan Denah: {denah.nama_gedung}")
        if not denah.daftar_ruangan:
            print("Belum ada data ruangan di gedung ini.")
            return
        
        # logika menyusun dan menampilkan ruangan
        for ruangan in denah.daftar_ruangan:
            print(ruangan)


# CONTEXT (Sistem Utama)
class NavIFSystem:
    def __init__(self):
        self._strategy: ViewStrategy = None
    
    def set_strategy(self, strategy: ViewStrategy):
        self._strategy = strategy

    def lihat_informasi(self, data):
        if not self._strategy:
            print("Error: Strategi tampilan belum diatur!")
            return
        
        # memanggil fungsi dari strategy pattern
        self._strategy.tampilkan_data(data)

# melihat denah gedung
if __name__ == "__main__":
    # persiapan data (menyiapkan objek denah dan isinya)
    gedung_if = Denah("Gedung Teknik Informatika ITS")

    # LANTAI 1 
    for i in range(1, 13):
        nomor_kelas = f"1{i:02d}" 
        gedung_if.tambah_ruangan(Ruangan(f"IF-{nomor_kelas}", f"Ruang Kelas IF-{nomor_kelas}", 1, "Ruang perkuliahan reguler Departemen Teknik Informatika"))
    
    gedung_if.tambah_ruangan(Ruangan("PLZ-01", "Plaza Supeno", 1, "Area terbuka untuk kegiatan mahasiswa dan titik kumpul"))
    gedung_if.tambah_ruangan(Ruangan("LAP-01", "Lapangan Voli", 1, "Fasilitas olahraga bola voli"))
    gedung_if.tambah_ruangan(Ruangan("TLT-L1", "Toilet Lantai 1", 1, "Fasilitas sanitasi pria dan wanita lantai 1"))

    # LANTAI 2
    gedung_if.tambah_ruangan(Ruangan("TU-01", "Ruang Tata Usaha 1", 2, "Ruang administrasi akademik dan kemahasiswaan"))
    gedung_if.tambah_ruangan(Ruangan("TU-02", "Ruang Tata Usaha 2", 2, "Ruang administrasi umum dan keuangan"))
    gedung_if.tambah_ruangan(Ruangan("AULA", "Aula Handayani", 2, "Ruang serbaguna untuk seminar, yudisium, dan acara departemen"))
    gedung_if.tambah_ruangan(Ruangan("TLT-L2", "Toilet Lantai 2", 2, "Fasilitas sanitasi pria dan wanita lantai 2"))

    # LANTAI 3
    gedung_if.tambah_ruangan(Ruangan("LAB-KCV", "Laboratorium Komputasi Cerdas dan Visi (KCV)", 3, "Lab untuk penelitian dan praktikum Kecerdasan Buatan & Computer Vision"))
    gedung_if.tambah_ruangan(Ruangan("LAB-RPL", "Laboratorium Rekayasa Perangkat Lunak (RPL)", 3, "Lab untuk pengembangan, desain, dan arsitektur perangkat lunak"))
    gedung_if.tambah_ruangan(Ruangan("LAB-AJK", "Laboratorium Arsitektur dan Jaringan Komputer (AJK)", 3, "Lab untuk riset jaringan, keamanan siber, dan infrastruktur IT"))
    gedung_if.tambah_ruangan(Ruangan("LAB-MI", "Laboratorium Manajemen Informasi (MI)", 3, "Lab untuk basis data, data mining, dan sistem informasi"))
    gedung_if.tambah_ruangan(Ruangan("LAB-IGS", "Laboratorium Interaksi, Grafika, dan Seni (IGS)", 3, "Lab untuk grafika komputer, game development, dan HCI"))
    gedung_if.tambah_ruangan(Ruangan("LAB-LP", "Laboratorium Pemrograman (LP)", 3, "Lab komputasi dasar dan praktikum algoritma pemrograman"))
    gedung_if.tambah_ruangan(Ruangan("LAB-NCC", "Network and Computing Center (NCC)", 3, "Pusat komputasi terdistribusi dan layanan server departemen"))
    gedung_if.tambah_ruangan(Ruangan("LAB-DI", "Laboratorium Dasar Ilmu Komputer", 3, "Lab untuk riset komputasi teoretik dan dasar ilmu komputer"))
    gedung_if.tambah_ruangan(Ruangan("TLT-L3", "Toilet Lantai 3", 3, "Fasilitas sanitasi pria dan wanita lantai 3"))

    # inisialisasi sistem
    sistem_navif = NavIFSystem()

    # skenario: sistem mengatur strategi khusus untuk denah
    sistem_navif.set_strategy(DenahViewStrategy())

    # skenario: user memicu aksi "melihat denah gedung"
    sistem_navif.lihat_informasi(gedung_if)