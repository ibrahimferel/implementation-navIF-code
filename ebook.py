from abc import ABC, abstractmethod

class Ebook:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category

    def __repr__(self):
        return f"{self.title} - {self.author} ({self.category})"

class SearchStrategy(ABC):
    @abstractmethod
    def search(self, ebooks, keyword):
        pass

class SearchByTitle(SearchStrategy):
    def search(self, ebooks, keyword):
        return [
            ebook for ebook in ebooks
            if keyword.lower() in ebook.title.lower()
        ]

class SearchByAuthor(SearchStrategy):
    def search(self, ebooks, keyword):
        return [
            ebook for ebook in ebooks
            if keyword.lower() in ebook.author.lower()
        ]

class SearchByCategory(SearchStrategy):
    def search(self, ebooks, keyword):
        return [
            ebook for ebook in ebooks
            if keyword.lower() in ebook.category.lower()
        ]

class EbookSearchContext:
    def __init__(self, ebooks):
        self.ebooks = ebooks
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def execute_search(self, keyword):
        if self.strategy is None:
            print("Strategi belum dipilih.")
            return []
        return self.strategy.search(self.ebooks, keyword)


ebooks = [
    Ebook("Panduan Karir di Industri Tech", "Alumni TC 2020", "Karir"),
    Ebook("Beasiswa S2 Luar Negeri", "Alumni TC 2019", "Beasiswa"),
    Ebook("Journey Membangun Startup", "Alumni TC 2018", "Entrepreneurship"),
]


def tampilkan_hasil(hasil, label):
    print(f"\nHasil pencarian '{label}':")

    if hasil:
        for ebook in hasil:
            print("->", ebook)
    else:
        print("-> Tidak ditemukan.")


ctx = EbookSearchContext(ebooks)

ctx.set_strategy(SearchByTitle())
hasil = ctx.execute_search("Industri Tech")
tampilkan_hasil(hasil, "Industri Tech")

ctx.set_strategy(SearchByAuthor())
hasil = ctx.execute_search("2020")
tampilkan_hasil(hasil, "2020")

ctx.set_strategy(SearchByCategory())
hasil = ctx.execute_search("Beasiswa")
tampilkan_hasil(hasil, "Beasiswa")
