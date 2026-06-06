from abc import ABC, abstractmethod

class Activity:
    def __init__(self, title, category, description):
        self.title = title
        self.category = category
        self.description = description

    def __repr__(self):
        return f"{self.title} ({self.category}) - {self.description}"

class ActivityFilterStrategy(ABC):
    @abstractmethod
    def filter(self, activities):
        pass

class AcademicActivityStrategy(ActivityFilterStrategy):
    def filter(self, activities):
        return [
            a for a in activities
            if a.category.lower() == "akademik"
        ]

class SeminarStrategy(ActivityFilterStrategy):
    def filter(self, activities):
        return [
            a for a in activities
            if a.category.lower() == "seminar"
        ]

class OrganizationActivityStrategy(ActivityFilterStrategy):
    def filter(self, activities):
        return [
            a for a in activities
            if a.category.lower() == "organisasi"
        ]

class ActivitySearchContext:
    def __init__(self, activities):
        self.activities = activities
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def search(self):
        if self.strategy is None:
            print("Strategi belum dipilih.")
            return []
        return self.strategy.filter(self.activities)


activities = [
    Activity("Seminar Artificial Intelligence dalam Industri 4.0", "Seminar", "Seminar tentang penerapan AI dalam revolusi industri 4.0, menghadirkan pembicara dari perusahaan teknologi terkemuka."),
    Activity("Workshop Web Development dengan React", "Akademik", "Workshop intensif selama 2 hari tentang pengembangan web modern menggunakan React dan TypeScript."),
    Activity("Rapat Koordinasi HMTC", "Organisasi", "Rapat koordinasi bulanan pengurus HMTC untuk evaluasi program kerja."),
]

def tampilkan_hasil(hasil, label):
    print(f"\nHasil pencarian {label}:")
    if hasil:
        for item in hasil:
            print("->", item)
    else:
        print("Tidak ada kegiatan ditemukan.")

ctx = ActivitySearchContext(activities)

ctx.set_strategy(AcademicActivityStrategy())
tampilkan_hasil(ctx.search(), "Kegiatan Akademik")

ctx.set_strategy(SeminarStrategy())
tampilkan_hasil(ctx.search(), "Seminar")

ctx.set_strategy(OrganizationActivityStrategy())
tampilkan_hasil(ctx.search(), "Kegiatan Organisasi")
