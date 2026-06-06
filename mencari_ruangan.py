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
        return f"[{self.id_ruangan}] {self.nama} (Lantai {self.lantai})\n    Deskripsi: {self.deskripsi}\n"


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

    @abstractmethod
    def cari_data(self, data, keyword: str) -> None:
        pass


# CONCRETE STRATEGY (Use Case: Denah Gedung)
class DenahViewStrategy(ViewStrategy):
    def tampilkan_data(self, denah: Denah) -> None:
        print(f" MENAMPILKAN DENAH: {denah.nama_gedung.upper()} ")
        
        if not denah.daftar_ruangan:
            print("Belum ada data ruangan di gedung ini.")
            return
        
        # kelompokkan berdasarkan lantai agar rapi
        lantai_dict = {}
        for ruangan in denah.daftar_ruangan:
            if ruangan.lantai not in lantai_dict:
                lantai_dict[ruangan.lantai] = []
            lantai_dict[ruangan.lantai].append(ruangan)
            
        for lantai in sorted(lantai_dict.keys()):
            print(f" LANTAI {lantai}")
            for ruangan in lantai_dict[lantai]:
                print(ruangan)

    def cari_data(self, denah: Denah, keyword: str) -> None:
        print(f"\n HASIL PENCARIAN RUANGAN: '{keyword.upper()}' ")
        
        # mencari berdasarkan kecocokan nama ruangan atau ID ruangan
        hasil_pencarian = [
            ruangan for ruangan in denah.daftar_ruangan 
            if keyword.lower() in ruangan.nama.lower() or keyword.lower() in ruangan.id_ruangan.lower()
        ]
        
        if not hasil_pencarian:
            print(f"Ruangan dengan kata kunci '{keyword}' tidak ditemukan.")
        else:
            print(f"Ditemukan {len(hasil_pencarian)} ruangan yang cocok:\n")
            for ruangan in hasil_pencarian:
                print(ruangan)

# CONTEXT (Sistem Utama)
class NavIFSystem:
    def __init__(self):
        self._strategy: ViewStrategy = None
    
    def set_strategy(self, strategy: ViewStrategy):
        self._strategy = strategy

    def lihat_informasi(self, data):
        if not self._strategy:
            print("Error: Strategi belum diatur!")
            return
        self._strategy.tampilkan_data(data)

    def cari_informasi(self, data, keyword: str):
        if not self._strategy:
            print("Error: Strategi belum diatur!")
            return
        self._strategy.cari_data(data, keyword)


if __name__ == "__main__":
    # persiapan data gedung
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
    sistem_navif.set_strategy(DenahViewStrategy())

    # skenario 1: Melihat Keseluruhan Denah
    sistem_navif.lihat_informasi(gedung_if)

    # skenario 2: Melakukan Pencarian Ruangan "KCV"
    sistem_navif.cari_informasi(gedung_if, "KCV")

    # skenario 3: Melakukan Pencarian Ruangan "Toilet" (Akan memunculkan semua toilet dari L1-L3)
    sistem_navif.cari_informasi(gedung_if, "Toilet")

    # skenario 4: Melakukan Pencarian dengan ID Ruangan langsung (Contoh: "IF-105")
    sistem_navif.cari_informasi(gedung_if, "IF-105")