from abc import ABC, abstractmethod
from typing import List

# ==========================================
# 1. ENTITAS (Data Model)
# ==========================================
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


# ==========================================
# 2. STRATEGY INTERFACE
# ==========================================
class ViewStrategy(ABC):
    """
    Antarmuka (Interface) untuk semua strategi penampilan data di NavIF.
    Semua tipe data (Denah, Kegiatan, Ebook) wajib mengimplementasikan ini.
    """
    @abstractmethod
    def tampilkan_data(self, data) -> None:
        pass

    @abstractmethod
    def cari_data(self, data, keyword: str) -> None:
        pass


# ==========================================
# 3. CONCRETE STRATEGY (Untuk Use Case: Melihat Denah Gedung)
# ==========================================
class DenahViewStrategy(ViewStrategy):
    """
    Logika spesifik untuk memproses, menampilkan, dan mencari Denah Gedung.
    """
    def tampilkan_data(self, denah: Denah) -> None:
        print(f"\n=== Menampilkan Denah: {denah.nama_gedung} ===")
        if not denah.daftar_ruangan:
            print("Belum ada data ruangan.")
            return
        
        for ruangan in denah.daftar_ruangan:
            print(ruangan)
        print("==================================================")

    def cari_data(self, denah: Denah, keyword: str) -> None:
        print(f"\n=== Hasil Pencarian Ruangan '{keyword}' ===")
        # Logika filter khusus untuk denah gedung
        hasil = [r for r in denah.daftar_ruangan if keyword.lower() in r.nama.lower()]
        
        if hasil:
            for r in hasil:
                print(r)
        else:
            print(f"Ruangan dengan kata kunci '{keyword}' tidak ditemukan di {denah.nama_gedung}.")
        print("==================================================")


# ==========================================
# 4. CONTEXT (Sistem Utama / Controller)
# ==========================================
class NavIFSystem:
    """
    Kelas utama pengontrol aplikasi NavIF. 
    Sistem tidak perlu tahu detail cara data ditampilkan, 
    cukup mendelegasikannya ke strategy yang sedang aktif.
    """
    def __init__(self):
        self._strategy: ViewStrategy = None
    
    def set_strategy(self, strategy: ViewStrategy):
        """Mengganti algoritma/strategi saat runtime"""
        self._strategy = strategy

    def lihat_informasi(self, data):
        if not self._strategy:
            print("Error: Strategi tampilan belum diatur!")
            return
        self._strategy.tampilkan_data(data)
    
    def cari_informasi(self, data, keyword: str):
        if not self._strategy:
            print("Error: Strategi tampilan belum diatur!")
            return
        self._strategy.cari_data(data, keyword)


# ==========================================
# 5. SIMULASI SKENARIO USE CASE
# ==========================================
if __name__ == "__main__":
    # A. Persiapan Data (Database Mockup Gedung Teknik Informatika ITS)
    gedung_if = Denah("Gedung Teknik Informatika ITS")
    gedung_if.tambah_ruangan(Ruangan("IF-101", "Ruang Tata Usaha", 1, "Pusat administrasi departemen"))
    gedung_if.tambah_ruangan(Ruangan("IF-105", "Laboratorium Pemrograman", 1, "Lab praktikum mahasiswa"))
    gedung_if.tambah_ruangan(Ruangan("IF-201", "Kelas Teori A", 2, "Ruang perkuliahan reguler"))

    # B. Inisialisasi Sistem NavIF
    sistem_navif = NavIFSystem()

    # C. Skenario: User masuk ke menu "Denah Gedung"
    # Sistem secara dinamis memasang strategi khusus Denah
    sistem_navif.set_strategy(DenahViewStrategy())

    # D. Skenario: User memilih untuk melihat keseluruhan denah gedung
    sistem_navif.lihat_informasi(gedung_if)

    # E. Skenario: User mencari ruangan spesifik (contoh mencari "Laboratorium")
    sistem_navif.cari_informasi(gedung_if, "Kelas")