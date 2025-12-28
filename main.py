class Vazifa:
    def __init__(self, nom, bajarildi=False):
        self.nom = nom
        self.bajarildi = bajarildi

    def holat(self):
        if self.bajarildi:
            return "✅ Bajarildi"
        else:
            return "❌ Bajarilmadi"


class TodoList:
    def __init__(self):
        self.vazifalar = []

    def qoshish(self, vazifa):
        self.vazifalar.append(vazifa)

    def chiqarish(self):
        if not self.vazifalar:
            print("Vazifalar yo‘q")
        else:
            for i, v in enumerate(self.vazifalar, start=1):
                print(f"{i}. {v.nom} - {v.holat()}")


todo = TodoList()

todo.qoshish(Vazifa("Python o‘rganish"))
todo.qoshish(Vazifa("Uy vazifasini qilish", True))
todo.qoshish(Vazifa("Kitob o‘qish"))

print("Vazifalar ro‘yxati:")
todo.chiqarish()
