class Flower:
    def __init__(self, name, price, freshness, stem_length, lifespan):
        self.name = name
        self.price = price
        self.freshness = freshness
        self.stem_length = stem_length
        self.lifespan = lifespan


class Rose(Flower):
    def __init__(self, price, freshness, stem_length):
        super().__init__("Роза", price, freshness, stem_length, 7)


class Tulip(Flower):
    def __init__(self, price, freshness, stem_length):
        super().__init__("Тюльпан", price, freshness, stem_length, 5)


class Lily(Flower):
    def __init__(self, price, freshness, stem_length):
        super().__init__("Лилия", price, freshness, stem_length, 10)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def get_cost(self):
        return sum(f.price for f in self.flowers)

    def get_wilting_time(self):
        if not self.flowers:
            return 0
        return sum(f.lifespan for f in self.flowers) / len(self.flowers)

    def sort_by(self, parameter):
        self.flowers.sort(key=lambda x: getattr(x, parameter), reverse=True)

    def find_by_lifespan(self, days):
        return [f.name for f in self.flowers if f.lifespan == days]


bouquet = Bouquet()
bouquet.add_flower(Rose(150, 9, 50))
bouquet.add_flower(Tulip(80, 10, 30))
bouquet.add_flower(Lily(200, 8, 40))

print(f"Стоимость букета: {bouquet.get_cost()} руб.")
print(f"Среднее время увядания: {bouquet.get_wilting_time():.1f} дней")

bouquet.sort_by("price")
print(f"Самый дорогой цветок: {bouquet.flowers[0].name}")
print(f"Самый дешевый цветок: {bouquet.flowers[-1].name}")

found = bouquet.find_by_lifespan(7)
print(f"Цветы со сроком жизни 7 дней: {found}")
