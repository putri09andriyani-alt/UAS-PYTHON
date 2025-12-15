class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    def display(self):
        return f"{self.name} | {self.category} | Rp {self.price}"
