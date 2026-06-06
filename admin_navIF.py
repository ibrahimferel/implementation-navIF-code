from abc import ABC, abstractmethod

class SystemData:
    def __init__(self, title, data_type):
        self.title = title
        self.data_type = data_type

    def __repr__(self):
        return f"{self.title} ({self.data_type})"

class DataManagementStrategy(ABC):
    @abstractmethod
    def execute(self, data_list, data):
        pass

class AddDataStrategy(DataManagementStrategy):
    def execute(self, data_list, data):
        data_list.append(data)
        print(f"Data '{data.title}' berhasil ditambahkan.")

class EditDataStrategy(DataManagementStrategy):
    def execute(self, data_list, data):
        for item in data_list:
            if item.title == data.title:
                item.data_type = data.data_type
                print(f"Data '{data.title}' berhasil diperbarui.")
                return
        print("Data tidak ditemukan.")

class DeleteDataStrategy(DataManagementStrategy):
    def execute(self, data_list, data):
        for item in data_list:
            if item.title == data.title:
                data_list.remove(item)
                print(f"Data '{data.title}' berhasil dihapus.")
                return
        print("Data tidak ditemukan.")

class DataManagementContext:
    def __init__(self, data_list):
        self.data_list = data_list
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def execute(self, data):
        if self.strategy is None:
            print("Strategi belum dipilih.")
            return
        self.strategy.execute(self.data_list, data)


data_list = [
    SystemData("Denah Gedung IF", "Denah Ruangan"),
    SystemData("Seminar AI", "Informasi Akademik"),
    SystemData("Career Planning", "E-Book")
]

def tampilkan_data():
    print("\nDaftar Data Sistem:")
    for data in data_list:
        print("->", data)


ctx = DataManagementContext(data_list)

tampilkan_data()

ctx.set_strategy(AddDataStrategy())
ctx.execute(SystemData("Workshop Python", "Informasi Akademik"))

ctx.set_strategy(EditDataStrategy())
ctx.execute(SystemData("Career Planning", "E-Book Karir"))

ctx.set_strategy(DeleteDataStrategy())
ctx.execute(SystemData("Seminar AI", ""))

tampilkan_data()
